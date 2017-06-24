import hashlib
import numpy as np


def filter_by_activities_transfer(df_source, df_source_labels, df_target,
                                  df_target_labels, use_activities):

    df_source, df_source_labels = filter_by_activities(df_source,
                                                       df_source_labels,
                                                       use_activities)
    df_target, df_target_labels = filter_by_activities(df_target,
                                                       df_target_labels,
                                                       use_activities)

    if df_source is None or df_target is None:
        return None, None, None, None

    return df_source, df_source_labels, df_target, df_target_labels


def filter_by_activities(df, df_labels, use_activities,
        check_all_activities=True):
    df_labels = df_labels.loc[df_labels.label.isin(use_activities)]
    df = df.loc[df.index.isin(df_labels.index)]

    df_activities = np.sort(df_labels.label.unique().tolist()).tolist()
    activities = np.sort(use_activities).tolist()
    if check_all_activities and activities != df_activities:
        print('Source or target dont provide the activities')
        return None, None

    return df, df_labels


def filter_by_features(df_source, use_features, df_target=None):
    # filter features to be used on the source domain
    df_source = df_source.filter(regex=(use_features))
    if len(df_source.columns) == 0:
        print('No features found for source')
        return None, None

    if df_target is not None:
        # filter features on the target to be the same as on the source
        try:
            df_target = df_target[df_source.columns]
        except KeyError as ex:
            print('Target doesnt provide the same columns as source')
            return None, None

    return df_source, df_target


def get_feature_hash(df):
    df.columns
    features = np.sort(df.columns.unique().tolist()).tolist()
    return hashlib.md5(';'.join(features).encode('utf-8')).hexdigest()
