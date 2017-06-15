import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from .filtering import filter_by_features, filter_by_activities
from .data_split import X_sort
from .configuration import read_configuration


configuration = read_configuration()
dataset_folder = '../datasets/'


def add_empty_columns_if_missing(df, columns):
    for column in columns:
        if column not in df:
            df[column] = -1


def read_complete_dataset(dataset,
                          device,
                          sensor_streams,
                          activities,
                          anomaly_percentile=100):

    global dataset_folder

    dataset_path = dataset_folder + dataset + '-complete/'
    df = pd.read_pickle(dataset_path + device + '.p')
    df = df.filter(regex=sensor_streams + '|label')

    value_columns = df.filter(regex=sensor_streams).columns

    null_df = df.loc[df.label == configuration['activities'].index('Null')]

    null_mean = null_df[value_columns].mean()
    null_std = null_df[value_columns].std()
    df[value_columns] = (df[value_columns] - null_mean) / null_std
    df = df.replace([np.inf, -np.inf, np.nan], 0)

    if anomaly_percentile < 100:
        anomalies = (df[value_columns] ** 2).sum(axis=1).apply(np.sqrt)
        df['anomalies'] = anomalies

    df[value_columns] = StandardScaler().fit_transform(df[value_columns])

    activities_i = [configuration['activities'].index(a) for a in activities]
    df = df.loc[df.label.isin(activities_i)]

    if anomaly_percentile < 100:
        anomaly_threshold = np.percentile(df.anomalies.values, 100 - anomaly_percentile)
        print(anomaly_threshold)
        df = df.loc[df.anomalies > anomaly_threshold]

    return df[value_columns].values, df.label.values


def get_anomalies(df, value_columns):
    null_df = df.loc[df.label == configuration['activities'].index('Null')]
    null_mean = null_df[value_columns].mean()
    null_std = null_df[value_columns].std()

    anomalies = (((df[value_columns] - null_mean) / null_std) ** 2).sum(axis=1).apply(np.sqrt)
    return anomalies


def read_and_filter_dataset(datasets, devices,
                            use_features=None,
                            force_columns=None,
                            use_columns=None,
                            use_activities=None,
                            scale=True,
                            with_feature_selection=False):
    # read datasets
    df, df_labels = read_dataset(
            datasets,
            devices,
            with_feature_selection=with_feature_selection)

    # filter features
    if use_features is not None:
        df, __ = filter_by_features(df_source=df,
                                    use_features=use_features)
        if df is None:
            return None, None

    if force_columns is not None:
        use_columns = force_columns
        add_empty_columns_if_missing(df, force_columns)

    # filter specific columns
    if use_columns is not None:
        try:
            df = df[use_columns]
        except KeyError as ex:
            print('No such columns found')
            return None, None

    # filter activities
    if use_activities is not None:
        df, df_labels = filter_by_activities(df, df_labels, use_activities)
        if df is None:
            print('Activities not found')
            return None, None
    # sort feature columns
    df = X_sort(df)

    # scale domains
    if scale:
        df[df.columns] = StandardScaler().fit_transform(df[df.columns])

    return df, df_labels


def read_dataset(datasets, devices, with_feature_selection=False):
    dfs = []
    dfs_labels = []

    global dataset_folder

    for dataset in datasets.split(','):
        dataset_path = dataset_folder + dataset + '-features/'

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


def set_dataset_folder(folder):
    global dataset_folder
    dataset_folder = folder


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
