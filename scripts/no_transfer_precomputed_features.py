#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import json

from ml.data_split import split_one_df
from ml.classification import classify, log_of_classification_results

dataset_path = '../datasets/synergy-mites-colocated-features/'
output_file = '/'.join([
    'synergy-mites-colocated',
    'results',
    'results_no_transfer.csv'
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
    "ACCEL_sst_*|MICROPHONE_sst_*"
]

classifiers = [
    'RandomForestClassifier'
]


def test(device, use_features, clf_name):
    df = pd.read_pickle(dataset_path + device + '.p')

    df_labels = pd.DataFrame.from_csv(dataset_path + 'activity_labels.csv')

    df = df.filter(regex=(use_features))

    X_train, y_train, X_test, y_test = split_one_df(df, df_labels, 0.7)
    y_pred = classify(X_train, y_train, X_test, clf_name)
    r = log_of_classification_results(y_test, y_pred)

    return r


with open('configuration.json') as f:
    configuration = json.load(f)

for repeat in range(20):
    for device in devices:
        device_i = configuration['devices'].index(device)

        for feature in features:
            feature_i = configuration['features'].index(feature)

            for clf_name in classifiers:
                clf_i = configuration['classifiers'].index(clf_name)

                report = test(device, feature, clf_name)
                report = [
                    device_i, feature_i, clf_i
                ] + report
                report = [str(i) for i in report]

                with open(output_file, "a") as f:
                    f.write(','.join(report) + "\n")
