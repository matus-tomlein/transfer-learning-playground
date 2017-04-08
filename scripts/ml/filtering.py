import numpy as np

def filter_by_activities(df_source, df_source_labels, df_target,
        df_target_labels, use_activities):
    df_source_labels = df_source_labels.loc[df_source_labels.label.isin(use_activities)]
    df_source = df_source.loc[df_source.index.isin(df_source_labels.index)]
    df_target_labels = df_target_labels.loc[df_target_labels.label.isin(use_activities)]
    df_target = df_target.loc[df_target.index.isin(df_target_labels.index)]

    source_activities = np.sort(df_source_labels.label.unique().tolist()).tolist()
    target_activities = np.sort(df_target_labels.label.unique().tolist()).tolist()
    activities = np.sort(use_activities).tolist()
    if activities != source_activities or activities != target_activities:
        print('Source or target dont provide the activities')
        return None, None, None, None

    return df_source, df_source_labels, df_target, df_target_labels

def filter_by_features(df_source, df_target, use_features):
    ## filter features to be used on the source domain
    df_source = df_source.filter(regex=(use_features))
    if len(df_source.columns) == 0:
        print('No features found for source')
        return None, None

    ## filter features on the target to be the same as on the source
    try:
        df_target = df_target[df_source.columns]
    except KeyError as ex:
        print('Target doesnt provide the same columns as source')
        return None, None

    return df_source, df_target
