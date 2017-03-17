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


def split_with_training_subsplit(df_source, df_target, df_labels,
                                 ratio=0.7, subsplit_ratio=0.7):

    all_training_i, testing_i = split_labels_indexes(df_labels, ratio)

    training_split = round(subsplit_ratio * len(all_training_i))

    source_training_i = all_training_i[:training_split]
    target_training_i = all_training_i[training_split:]

    X_train_source = df_source.loc[df_source.index.isin(source_training_i)]
    X_train_target = df_target.loc[df_target.index.isin(target_training_i)]
    X_train = pd.concat([X_train_source, X_train_target])

    X_test = df_target.loc[df_target.index.isin(testing_i)]

    y_train, y_test = create_y_train_and_y_test(df_labels, all_training_i,
                                                testing_i)

    return X_sort(X_train), y_train, X_sort(X_test), y_test
