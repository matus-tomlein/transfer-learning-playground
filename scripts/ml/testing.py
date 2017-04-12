import pandas as pd
import numpy as np
from ml.classification import classify, log_of_classification_results
from ml.filtering import filter_by_features, filter_by_activities
from ml.data_split import X_sort, take_percentage_of_data


def add_empty_columns_if_missing(df, columns):
    for column in columns:
        if column not in df:
            df[column] = np.nan


# test the performance of classification
# use_features: filter features by the regular expression
# use_columns: use columns with names in the list
# force_columns: keep the given columns and if they are not present, create them
# with empty values
def test_transfer(source_device, target_device,
                  source_dataset_path, target_dataset_path,
                  use_features=None,
                  force_columns=None,
                  use_columns=None,
                  use_activities=None,
                  with_feature_selection=False,
                  clf_name='RandomForestClassifier'):
    source_file_name = source_device + '_selected' if with_feature_selection else source_device

    # read features
    df_source = pd.read_pickle(source_dataset_path + source_file_name + '.p')
    df_target = pd.read_pickle(target_dataset_path + target_device + '.p')

    # read labels
    df_source_labels = pd.read_pickle(source_dataset_path + source_device + '_labels.p')
    df_target_labels = pd.read_pickle(target_dataset_path + target_device + '_labels.p')

    # filter features
    if use_features is not None:
        df_source, df_target = filter_by_features(df_source, df_target,
                                                  use_features)
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
            filter_by_activities(
                df_source, df_source_labels, df_target,
                df_target_labels, use_activities)
        if df_source is None:
            return None

    # filter samples
    ratio = 0.6
    df_source, df_source_labels = take_percentage_of_data(
            df_source,
            df_source_labels, ratio)
    df_target, df_target_labels = take_percentage_of_data(
            df_target,
            df_target_labels, ratio)

    y_source = df_source_labels['label']
    y_target = df_target_labels['label']

    # sort feature columns
    X_source = X_sort(df_source)
    X_target = X_sort(df_target)

    try:
        y_target_pred = classify(X_source, y_source, X_target, clf_name)
    except ValueError as ex:
        print(ex)
        return None

    r = log_of_classification_results(y_target, y_target_pred)
    return r
