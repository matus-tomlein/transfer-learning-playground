#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import json

from ml.data_split import split
from ml.classification import classify, log_of_classification_results

dataset_path = '../datasets/synergy-mites-colocated-features/'
output_file = '/'.join([
    'synergy-mites-colocated',
    'results',
    'results_transfer.csv'
])

devices = [
    '128.237.246.127',
    '128.237.248.186',
    '128.237.253.157',
    '128.237.242.0'
]

features = [
    "ACCEL_sst_*",
    "MICROPHONE_sst_*",
    "MAGNETOMETER_sst_*",
    "ACCEL_sst_*|MICROPHONE_sst_*",
    "ACCEL_sst_*|MAGNETOMETER_sst_*",
    "MICROPHONE_sst_*|MAGNETOMETER_sst_*",
    "ACCEL_sst_*|MICROPHONE_sst_*|MAGNETOMETER_sst_*"
]

classifiers = [
    'RandomForestClassifier',
    'BernoulliNB',
    'SVC',
    'LogisticRegression'
]


def test(source, target, use_features, clf_name):
    df_train = pd.read_pickle(dataset_path + source + '.p')
    df_test = pd.read_pickle(dataset_path + target + '.p')

    df_labels = pd.DataFrame.from_csv(dataset_path + 'activity_labels.csv')

    df_train = df_train.filter(regex=(use_features))
    df_test = df_test.filter(regex=(use_features))

    X_train, y_train, X_test, y_test = split(df_train, df_test, df_labels, 0.7)
    y_pred = classify(X_train, y_train, X_test, clf_name)
    r = log_of_classification_results(y_test, y_pred)
    return r


with open('configuration.json') as f:
    configuration = json.load(f)

headers = [
    'source', 'target', 'feature', 'clf', 'accuracy'
]
headers += [str(i) for i in range(60)]
with open(output_file, "w") as f:
    f.write(','.join(headers) + "\n")


for repeat in range(20):
    for source in devices:
        for target in devices:
            if source == target:
                continue

            source_i = configuration['devices'].index(source)
            target_i = configuration['devices'].index(target)

            for feature in features:
                feature_i = configuration['features'].index(feature)

                for clf_name in classifiers:
                    clf_i = configuration['classifiers'].index(clf_name)

                    report = test(source, target, feature, clf_name)
                    report = [
                        source_i, target_i, feature_i, clf_i
                    ] + report
                    report = [str(i) for i in report]

                    with open(output_file, "a") as f:
                        f.write(','.join(report) + "\n")
