#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import json

from ml.data_split import split_with_target_training_data
from ml.classification import classify, log_of_classification_results

dataset_path = '../datasets/synergy-kitchen-mites-features/'
output_file = '/'.join([
    'synergy-mites-kitchen',
    'results',
    'results_transfer_with_labeled_target_data.csv'
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


def test(source, target, use_features, clf_name, target_data_ratio):
    df_train = pd.read_pickle(dataset_path + source + '.p')
    df_test = pd.read_pickle(dataset_path + target + '.p')

    df_labels = pd.DataFrame.from_csv(dataset_path + 'activity_labels.csv')

    df_train = df_train.filter(regex=(use_features))
    df_test = df_test.filter(regex=(use_features))

    X_train, y_train, X_test, y_test = \
        split_with_target_training_data(df_source=df_train,
                                        df_target=df_test,
                                        df_labels=df_labels,
                                        ratio=0.7,
                                        target_data_ratio=target_data_ratio)

    y_pred = classify(X_train, y_train, X_test, clf_name)
    r = log_of_classification_results(y_test, y_pred)
    return r


with open('configuration.json') as f:
    configuration = json.load(f)

headers = [
    'source', 'target', 'feature', 'clf', 'target_training_data', 'accuracy'
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

                    for r in range(11):
                        target_data_ratio = r / 10.0

                        report = test(source, target, feature, clf_name,
                                      target_data_ratio)
                        report = [
                            source_i, target_i, feature_i, clf_i,
                            target_data_ratio
                        ] + report
                        report = [str(i) for i in report]

                        with open(output_file, "a") as f:
                            f.write(','.join(report) + "\n")
