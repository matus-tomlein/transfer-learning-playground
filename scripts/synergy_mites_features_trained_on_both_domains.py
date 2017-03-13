#!/usr/bin/env python3
# -*- coding: utf8 -*-

import numpy as np
import pandas as pd
from tsfresh.transformers import RelevantFeatureAugmenter
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

dataset_path = '../datasets/synergy-kitchen-mites-processed/'


def train_test_split_labels(df_labels):
    indexes = df_labels.index.tolist()
    np.random.shuffle(indexes)
    split = int(round(0.7*len(indexes)))
    training_i = indexes[:split]
    testing_i = indexes[split:]

    y_train = df_labels.loc[df_labels.index.isin(training_i)]
    y_test = df_labels.loc[df_labels.index.isin(testing_i)]

    y_train = y_train['label']
    y_test = y_test['label']

    return y_train, y_test


def classify(df_train, X_train, y_train, df_test, X_test, y_test, clf_name):
    df_complete = pd.concat([df_train, df_test])
    X_complete = pd.concat([X_train, X_test])
    y_complete = pd.concat([y_train, y_test])

    augmenter = RelevantFeatureAugmenter(column_id='id')
    augmenter.timeseries_container = df_complete
    augmenter.fit(X_complete, y_complete)

    augmenter.timeseries_container = df_train
    X_train = augmenter.fit_transform(X_train, y_train)

    if clf_name == 'RandomForestClassifier':
        clf = RandomForestClassifier()
    elif clf_name == 'SVC':
        clf = svm.SVC()
    elif clf_name == 'GaussianNB':
        clf = GaussianNB()
    elif clf_name == 'DecisionTreeClassifier':
        clf = tree.DecisionTreeClassifier()

    ppl = Pipeline([
        ('impute', Imputer()),
        ('scale', StandardScaler()),
        ('clf', clf)
    ])

    ppl.fit(X_train, y_train)

    augmenter.timeseries_container = df_test
    transformed_X_test = augmenter.transform(X_test)

    y_pred = ppl.predict(transformed_X_test)

    results = [accuracy_score(y_test, y_pred)]
    f1 = precision_recall_fscore_support(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    results += [item for sublist in f1 for item in sublist]
    results += [item for sublist in matrix for item in sublist]

    return results


def test(source, target, use_features, clf_name):
    df_train = pd.DataFrame.from_csv(dataset_path + source + '.csv')
    df_test = pd.DataFrame.from_csv(dataset_path + target + '.csv')

    df_labels = pd.DataFrame.from_csv(dataset_path + 'activity_labels.csv')

    y_train, y_test = train_test_split_labels(df_labels)
    X_train = pd.DataFrame(index=y_train.index)
    X_test = pd.DataFrame(index=y_test.index)

    df_train = df_train.filter(regex=(use_features))
    df_test = df_test.filter(regex=(use_features))

    r = classify(df_train, X_train, y_train, df_test, X_test, y_test, clf_name)
    return r


devices = [
    '128.237.246.127',
    '128.237.248.186',
    '128.237.253.157',
    '128.237.242.0'
]

features = [
    "ACCEL_sst_*|id",
    "MICROPHONE_sst_*|id"
    # "MAGNETOMETER_sst_*|id"
]

classifiers = [
    'RandomForestClassifier',
    'SVC'
    # 'DecisionTreeClassifier',
    # 'GaussianNB'
]

for repeat in range(20):
    for source_i in range(len(devices)):
        for target_i in range(len(devices)):
            if source_i != target_i:
                source = devices[source_i]
                target = devices[target_i]

                for feature_i in range(len(features)):
                    feature = features[feature_i]

                    for clf_i in range(len(classifiers)):
                        clf_name = classifiers[clf_i]

                        report = test(source, target, feature, clf_name)
                        report = [
                            source_i, target_i, feature_i, clf_i
                        ] + report
                        report = [str(i) for i in report]

                        with open("results_train_on_both.csv", "a") as f:
                            f.write(','.join(report) + "\n")
