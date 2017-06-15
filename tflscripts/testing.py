from .classification import classify, log_of_classification_results, \
    fit_pipeline
import pickle
from .data_split import take_percentage_of_data, \
        take_multiple_percentages_of_data
from .domain_adaptation import easy_domain_adaptation_update_dataframes
from .configuration import read_configuration
from .datasets import read_and_filter_dataset, concat_and_reindex


configuration = read_configuration()
dataset_folder = '../datasets/'


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
    df, df_labels = read_and_filter_dataset(
            dataset,
            device,
            use_features=use_features,
            force_columns=force_columns,
            use_columns=use_columns,
            use_activities=use_activities,
            scale=False,
            with_feature_selection=with_feature_selection)

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
    df_source, df_source_labels = read_and_filter_dataset(
            source_dataset,
            source_device,
            use_features=use_features,
            force_columns=force_columns,
            use_columns=use_columns,
            use_activities=use_activities,
            scale=scale_domains_independently,
            with_feature_selection=with_feature_selection)
    df_target, df_target_labels = read_and_filter_dataset(
            target_dataset,
            target_device,
            use_features=use_features,
            force_columns=force_columns,
            use_columns=use_columns,
            use_activities=use_activities,
            scale=scale_domains_independently,
            with_feature_selection=False)

    if df_source is None or df_target is None:
        return None

    # select the features
    try:
        df_target = df_target[df_source.columns]
    except KeyError as ex:
        print('Target doesnt provide the same columns as source')
        return None

    # do easy domain adaptation
    if use_easy_domain_adaptation:
        df_source, df_target = easy_domain_adaptation_update_dataframes(
                df_source, df_target)

    df_source, df_source_labels, df_target, df_target_labels = \
        split_transfer_datasets(
                    df_source, df_source_labels,
                    df_target, df_target_labels,
                    training_source_data_ratio=training_source_data_ratio,
                    testing_target_data_ratio=testing_target_data_ratio,
                    training_target_data_ratio=training_target_data_ratio)

    try:
        ppl = build_pipeline(
                df=df_source,
                df_labels=df_source_labels,
                scale=not scale_domains_independently,
                clf_name=clf_name)

        if ppl is None:
            return None

        y_target = df_target_labels['label']

        y_target_pred = ppl.predict(df_target)
        r = log_of_classification_results(y_target, y_target_pred)
        return r
    except ValueError as ex:
        print('in classification', ex)
        return None


def split_transfer_datasets(df_source, df_source_labels,
                            df_target, df_target_labels,
                            training_source_data_ratio=0.6,
                            testing_target_data_ratio=0.6,
                            training_target_data_ratio=0.0):
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

    return df_source, df_source_labels, df_target, df_target_labels


def build_pipeline(df, df_labels,
                   scale=True,
                   clf_name='RandomForestClassifier'):
    y = df_labels['label']

    ppl = fit_pipeline(df, y, clf_name, scale=scale)

    return ppl


class TestResult:
    def __init__(self,

                 source_device=None,
                 source_dataset=None,

                 target_device=None,
                 target_dataset=None,

                 label=None,
                 columns=None,

                 predicted=None,
                 actual=None,
                 actual_with_all_labels=None,
                 window_size=None,
                 classifier=None,

                 features=None):
        self.source_device = source_device
        self.source_dataset = source_dataset
        self.target_device = target_device
        self.target_dataset = target_dataset

        self.label = label
        self.columns = columns
        self.window_size = window_size
        self.features = features
        self.classifier = classifier

        self.predicted = predicted
        self.actual = actual
        self.actual_with_all_labels = actual_with_all_labels

    def label_name(self):
        return configuration['activities'][self.label]


class TestSet:
    def __init__(self, name,
                 path='/home/giotto/transfer-learning-playground/results/'):
        self.name = name
        self.file_name = path + self.name + '.pkl'

    def add_result(self, result):
        output = open(self.file_name, 'ab')
        pickle.dump(result, output)
        output.close()
        print('Added result from', result.source_device,
              result.source_dataset,
              'to', result.target_device,
              result.target_dataset)

    def get_results(self):
        input = open(self.file_name, 'rb')
        results = []
        try:
            while True:
                result = pickle.load(input)
                results.append(result)

        except (EOFError) as e:
            input.close()

        return results
