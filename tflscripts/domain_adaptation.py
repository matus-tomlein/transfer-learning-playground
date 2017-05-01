def easy_domain_adaptation_update_dataframes(df_source, df_target):
    for column in df_source.columns.tolist():
        df_source['source_' + column] = df_source[column]
        df_source['target_' + column] = 0

    for column in df_target.columns.tolist():
        df_target['source_' + column] = 0
        df_target['target_' + column] = df_target[column]

    return df_source, df_target
