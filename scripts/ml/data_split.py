import numpy as np
import pandas as pd


def split_labels_indexes(df_labels, ratio=0.7):
    indexes = df_labels.index.tolist()
    np.random.shuffle(indexes)
    split = int(round(ratio * len(indexes)))
    training_i = indexes[:split]
    testing_i = indexes[split:]

    return training_i, testing_i


def create_y_train_and_y_test(df_labels, training_i, testing_i):
    y_train = df_labels.loc[df_labels.index.isin(training_i)]
    y_test = df_labels.loc[df_labels.index.isin(testing_i)]

    y_train = y_train['label']
    y_test = y_test['label']

    return y_train, y_test


def X_sort(X):
    return X.reindex_axis(sorted(X.columns), axis=1)


def split(df_train, df_test, df_labels, ratio=0.7):
    training_i, testing_i = split_labels_indexes(df_labels, ratio)
    y_train, y_test = create_y_train_and_y_test(df_labels, training_i,
                                                testing_i)

    X_train = df_train.loc[df_train.index.isin(training_i)]
    X_test = df_test.loc[df_test.index.isin(testing_i)]

    return X_sort(X_train), y_train, X_sort(X_test), y_test


def split_one_df(df, df_labels, ratio=0.7):
    training_i, testing_i = split_labels_indexes(df_labels, ratio)
    y_train, y_test = create_y_train_and_y_test(df_labels, training_i,
                                                testing_i)

    X_train = df.loc[df.index.isin(training_i)]
    X_test = df.loc[df.index.isin(testing_i)]

    return X_sort(X_train), y_train, X_sort(X_test), y_test


def train_test_split_labels(df_labels, ratio=0.7):
    training_i, testing_i = split_labels_indexes(df_labels, ratio)
    y_train, y_test = create_y_train_and_y_test(df_labels, training_i,
                                                testing_i)

    return y_train, y_test


def split_with_target_training_data(df_source, df_target, df_labels,
                                    ratio=0.7, target_data_ratio=0.7):

    df_source = X_sort(df_source)
    df_target = X_sort(df_target)

    all_training_i, testing_i = split_labels_indexes(df_labels, ratio)

    target_training_len = round(target_data_ratio * len(all_training_i))
    target_training_i = all_training_i[:target_training_len]

    max_i = df_labels.index.max()

    X_train_source = df_source.loc[df_source.index.isin(all_training_i)]
    X_train_target = df_target.loc[df_target.index.isin(target_training_i)]

    X_train_target.index += max_i + 1
    X_train = pd.concat([X_train_source, X_train_target])

    y_train_source = df_labels.loc[df_labels.index.isin(all_training_i)]
    y_train_target = df_labels.loc[df_labels.index.isin(target_training_i)]

    y_train_target.index += max_i + 1
    y_train = pd.concat([y_train_source, y_train_target])

    X_test = df_target.loc[df_target.index.isin(testing_i)]
    y_test = df_labels.loc[df_labels.index.isin(testing_i)]

    y_train = y_train['label']
    y_test = y_test['label']

    return X_train, y_train, X_test, y_test


def split_with_multiple_sources(df_sources, df_target, df_labels, ratio=0.7):

    df_target = X_sort(df_target)

    training_i, testing_i = split_labels_indexes(df_labels, ratio)

    max_i = df_labels.index.max() + 1

    X_trains = []
    y_trains = []

    for df_source in df_sources:
        df_source = X_sort(df_source)

        X_train = df_source.loc[df_source.index.isin(training_i)]
        X_train.index += max_i + 1

        y_train = df_labels.loc[df_labels.index.isin(training_i)]
        y_train.index += max_i + 1

        X_trains.append(X_train)
        y_trains.append(y_train)

        max_i = X_train.index.max() + 1

    X_train = pd.concat(X_trains)
    y_train = pd.concat(y_trains)

    X_test = df_target.loc[df_target.index.isin(testing_i)]
    y_test = df_labels.loc[df_labels.index.isin(testing_i)]

    y_train = y_train['label']
    y_test = y_test['label']

    return X_train, y_train, X_test, y_test
