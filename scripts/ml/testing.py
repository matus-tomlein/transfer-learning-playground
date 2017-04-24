import pandas as pd
from ml.data_split import split_one_df
from sklearn.preprocessing import StandardScaler
from ml.classification import classify, log_of_classification_results
from ml.filtering import filter_by_features, filter_by_activities, \
    filter_by_activities_transfer
from ml.data_split import X_sort, take_percentage_of_data, \
        take_multiple_percentages_of_data
from ml.domain_adaptation import easy_domain_adaptation_update_dataframes
import json


with open('configuration.json') as f:
    configuration = json.load(f)


def add_empty_columns_if_missing(df, columns):
    for column in columns:
        if column not in df:
            df[column] = -1


def test_with_or_without_transfer(source_device, target_device,
                                  source_dataset, target_dataset,
                                  use_features=None,
                                  force_columns=None,
                                  use_columns=None,
                                  use_activities=None,
                                  training_source_data_ratio=0.6,
                                  training_target_data_ratio=0.0,
                                  with_feature_selection=False,
                                  scale_domains_independently=False,
                                  use_easy_domain_adaptation=False,
                                  clf_name='RandomForestClassifier'):

    if source_device == target_device and source_dataset == \
            target_dataset:
        return test_without_transfer(
                device=source_device,
                dataset=source_dataset,
                use_features=use_features,
                force_columns=force_columns,
                use_columns=use_columns,
                use_activities=use_activities,
                with_feature_selection=with_feature_selection,
                training_source_data_ratio=training_source_data_ratio,
                clf_name=clf_name)

    else:
        return test_transfer(
                source_device=source_device,
                target_device=target_device,
                source_dataset=source_dataset,
                target_dataset=target_dataset,
                use_features=use_features,
                force_columns=force_columns,
                use_columns=use_columns,
                use_activities=use_activities,
                with_feature_selection=with_feature_selection,
                scale_domains_independently=scale_domains_independently,
                training_source_data_ratio=training_source_data_ratio,
                training_target_data_ratio=training_target_data_ratio,
                use_easy_domain_adaptation=use_easy_domain_adaptation,
                clf_name=clf_name)


def test_without_transfer(device,
                          dataset,
                          use_features=None,
                          force_columns=None,
                          use_columns=None,
                          use_activities=None,
                          with_feature_selection=False,
                          training_source_data_ratio=0.7,
                          clf_name='RandomForestClassifier'):
    # read dataset
    df, df_labels = read_dataset(
            dataset,
            device,
            with_feature_selection=with_feature_selection)

    # filter features
    if use_features is not None:
        df, __ = filter_by_features(df_source=df,
                                    use_features=use_features)
        if df is None:
            return None

    if force_columns is not None:
        use_columns = force_columns
        add_empty_columns_if_missing(df, force_columns)

    # filter specific columns
    if use_columns is not None:
        try:
            df = df[use_columns]
        except KeyError as ex:
            print('No such columns found')
            return None

    # filter activities
    if use_activities is not None:
        df, df_labels = filter_by_activities(df, df_labels, use_activities)
        if df is None:
            return None
    # X_train, y_train, X_test, y_test = split_one_df(df, df_labels, 0.7)

    # split into training and testing
    testing_source_data_ratio = 0.4
    dfs = take_multiple_percentages_of_data(
            df, df_labels,
            [training_source_data_ratio, testing_source_data_ratio])

    X_train, y_train = dfs[0]
    X_test, y_test = dfs[1]

    y_train = y_train['label']
    y_test = y_test['label']

    try:
        y_pred = classify(X_train, y_train, X_test, clf_name, scale=True)
    except ValueError as ex:
        print('in classification', ex)
        return None

    r = log_of_classification_results(y_test, y_pred)

    return r


# test the performance of classification
# use_features: filter features by the regular expression
# use_columns: use columns with names in the list
# force_columns: keep the given columns and if they are not present, create
# them with empty values
def test_transfer(source_device, target_device,
                  source_dataset, target_dataset,
                  use_features=None,
                  force_columns=None,
                  use_columns=None,
                  use_activities=None,
                  with_feature_selection=False,
                  scale_domains_independently=False,
                  training_source_data_ratio=0.6,
                  testing_target_data_ratio=0.6,
                  training_target_data_ratio=0.0,
                  use_easy_domain_adaptation=False,
                  clf_name='RandomForestClassifier'):
    # read datasets
    df_source, df_source_labels = read_dataset(
            source_dataset,
            source_device,
            with_feature_selection=with_feature_selection)
    df_target, df_target_labels = read_dataset(
            target_dataset,
            target_device,
            with_feature_selection=with_feature_selection)

    # filter features
    if use_features is not None:
        df_source, df_target = filter_by_features(df_source=df_source,
                                                  df_target=df_target,
                                                  use_features=use_features)
        if df_source is None:
            return None

    if force_columns is not None:
        use_columns = force_columns
        add_empty_columns_if_missing(df_source, force_columns)
        add_empty_columns_if_missing(df_target, force_columns)

    # filter specific columns
    if use_columns is not None:
        try:
            df_source = df_source[use_columns]
            df_target = df_target[use_columns]
        except KeyError as ex:
            print('No such columns found')
            return None

    # filter activities
    if use_activities is not None:
        df_source, df_source_labels, df_target, df_target_labels = \
            filter_by_activities_transfer(
                df_source, df_source_labels, df_target,
                df_target_labels, use_activities)
        if df_source is None:
            return None

    # do easy domain adaptation
    if use_easy_domain_adaptation:
        df_source, df_target = easy_domain_adaptation_update_dataframes(
                df_source, df_target)

    # filter samples
    df_source, df_source_labels = take_percentage_of_data(
            df_source,
            df_source_labels,
            training_source_data_ratio)

    # split the target data to testing and training if necessary
    if training_target_data_ratio > 0.0:
        dfs_target = take_multiple_percentages_of_data(
                df_target,
                df_target_labels,
                [training_target_data_ratio, testing_target_data_ratio])

        df_target_train, df_target_train_labels = dfs_target[0]
        df_target, df_target_labels = dfs_target[1]

        df_source, df_source_labels = concat_and_reindex(
                [df_source, df_target_train],
                [df_source_labels, df_target_train_labels])
    else:
        df_target, df_target_labels = take_percentage_of_data(
                df_target,
                df_target_labels,
                testing_target_data_ratio)

    # sort feature columns
    X_source = X_sort(df_source)
    X_target = X_sort(df_target)

    # scale domains
    if scale_domains_independently:
        df_source = StandardScaler().fit_transform(df_source)
        df_target = StandardScaler().fit_transform(df_target)

    y_source = df_source_labels['label']
    y_target = df_target_labels['label']

    try:
        y_target_pred = classify(X_source, y_source, X_target, clf_name,
                                 scale=not scale_domains_independently)
    except ValueError as ex:
        print('in classification', ex)
        return None

    r = log_of_classification_results(y_target, y_target_pred)
    return r


def read_dataset(datasets, devices, with_feature_selection=False):
    dfs = []
    dfs_labels = []

    for dataset in datasets.split(','):
        dataset_path = '../datasets/' + dataset + '-features/'

        device_list = []
        if devices == 'ALL':
            device_roles = configuration['device_roles'][dataset]
            device_list = device_roles.keys()
        else:
            device_list = devices.split(',')

        for device in device_list:
            file_name = device + '_selected' if with_feature_selection else \
                    device

            df = pd.read_pickle(dataset_path + file_name + '.p')
            df_labels = pd.read_pickle(dataset_path + device + '_labels.p')

            df = df.reset_index(drop=True)
            df_labels = df_labels.reset_index(drop=True)

            dfs.append(df)
            dfs_labels.append(df_labels)

    return concat_and_reindex(dfs, dfs_labels)


def concat_and_reindex(dfs, dfs_labels):
    if len(dfs) == 1:
        return dfs[0], dfs_labels[0]

    max_index = -1

    dfs_reindexed = []
    dfs_labels_reindexed = []

    for i, df in enumerate(dfs):
        df_labels = dfs_labels[i]

        df = df.reset_index(drop=True)
        df_labels = df_labels.reset_index(drop=True)

        df.index += max_index + 1
        df_labels.index += max_index + 1

        max_index = df.index.max()

        dfs_reindexed.append(df)
        dfs_labels_reindexed.append(df_labels)

    return pd.concat(dfs_reindexed), pd.concat(dfs_labels_reindexed)
