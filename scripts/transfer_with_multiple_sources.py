#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import numpy as np
import json
from itertools import combinations

from ml.data_split import split_with_multiple_sources
from ml.classification import classify, log_of_classification_results

dataset_path = '../datasets/synergy-kitchen-mites-features/'
output_file = '/'.join([
    'synergy-mites-kitchen',
    'results',
    'results_transfer_with_multiple_sources.csv'
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
    "ACCEL_sst_*|MICROPHONE_sst_*",
    "ACCEL_sst_*|MICROPHONE_sst_*|MAGNETOMETER_sst_*"
]

classifiers = [
    'RandomForestClassifier',
    'BernoulliNB',
    'SVC',
    'LogisticRegression'
]


def test(sources, target, use_features, clf_name):
    df_sources = [pd.read_pickle(dataset_path + source + '.p') for source in
                  sources]
    df_target = pd.read_pickle(dataset_path + target + '.p')

    df_labels = pd.DataFrame.from_csv(dataset_path + 'activity_labels.csv')

    df_sources = [df.filter(regex=(use_features)) for df in df_sources]
    df_target = df_target.filter(regex=(use_features))

    X_train, y_train, X_test, y_test = \
        split_with_multiple_sources(df_sources, df_target, df_labels, 0.7)

    y_pred = classify(X_train, y_train, X_test, clf_name)
    r = log_of_classification_results(y_test, y_pred)
    return r


with open('configuration.json') as f:
    configuration = json.load(f)

headers = [
    'sources', 'target', 'feature', 'clf', 'accuracy'
]
headers += [str(i) for i in range(60)]
with open(output_file, "w") as f:
    f.write(','.join(headers) + "\n")


sources_combs = list(combinations(devices, 3))
sources_combs += list(combinations(devices, 2))

for repeat in range(20):
    for sources in sources_combs:
        sources = [s for s in sources]

        targets = [t for t in devices if t not in sources]

        for target in targets:
            sources_i = [configuration['devices'].index(s) for s in sources]
            sources_i = np.sort(sources_i)
            sources_i = [str(i) for i in sources_i]
            target_i = configuration['devices'].index(target)

            for feature in features:
                feature_i = configuration['features'].index(feature)

                for clf_name in classifiers:
                    clf_i = configuration['classifiers'].index(clf_name)

                    report = test(sources, target, feature, clf_name)
                    report = [
                        '_'.join(sources_i), target_i, feature_i, clf_i
                    ] + report
                    report = [str(i) for i in report]

                    with open(output_file, "a") as f:
                        f.write(','.join(report) + "\n")
