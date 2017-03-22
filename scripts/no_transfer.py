#!/usr/bin/env python3
# -*- coding: utf8 -*-

import numpy as np
import pandas as pd
from tsfresh.transformers import RelevantFeatureAugmenter
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score, precision_recall_fscore_support
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

dataset_path = '../datasets/synergy-kitchen-mites-processed/'
output_file = 'results_no_transfer.csv'


def train_test_split(df, df_labels):
    indexes = df_labels.index.tolist()
    np.random.shuffle(indexes)
    split = int(round(0.7*len(indexes)))
    training_i = indexes[:split]
    testing_i = indexes[split:]

    y_train = df_labels.loc[df_labels.index.isin(training_i)]
    y_test = df_labels.loc[df_labels.index.isin(testing_i)]

    y_train = y_train['label']
    y_test = y_test['label']

    X_train = pd.DataFrame(index=y_train.index)
    X_test = pd.DataFrame(index=y_test.index)

    return X_train, y_train, X_test, y_test


def classify(df, X_train, y_train, X_test, y_test, clf_name):
    if clf_name == 'RandomForestClassifier':
        clf = RandomForestClassifier()
    elif clf_name == 'SVC':
        clf = svm.SVC()
    elif clf_name == 'GaussianNB':
        clf = GaussianNB()
    elif clf_name == 'DecisionTreeClassifier':
        clf = tree.DecisionTreeClassifier()

    ppl = Pipeline([
        ('fresh', RelevantFeatureAugmenter(column_id='id')),
        ('impute', Imputer()),
        ('scale', StandardScaler()),
        ('clf', clf)
    ])

    ppl.set_params(fresh__timeseries_container=df)
    ppl.fit(X_train, y_train)

    y_pred = ppl.predict(X_test)

    results = [accuracy_score(y_test, y_pred)]
    f1 = precision_recall_fscore_support(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    results += [item for sublist in f1 for item in sublist]
    results += [item for sublist in matrix for item in sublist]

    return results


def test(device, use_features, clf_name):
    df = pd.DataFrame.from_csv(dataset_path + device + '.csv')
    df_labels = pd.DataFrame.from_csv(dataset_path + 'activity_labels.csv')

    df = df.filter(regex=(use_features))
    X_train, y_train, X_test, y_test = train_test_split(df, df_labels)

    return classify(df, X_train, y_train, X_test, y_test, clf_name)


devices = [
    '128.237.246.127',
    '128.237.248.186',
    '128.237.253.157',
    '128.237.242.0'
]

features = [
    "ACCEL_sst_*|id",
    "MICROPHONE_sst_*|id",
    "MAGNETOMETER_sst_*|id",
    "ACCEL_sst_*|MICROPHONE_sst_*|id",
    "ACCEL_sst_*|MAGNETOMETER_sst_*|id",
    "MICROPHONE_sst_*|MAGNETOMETER_sst_*|id",
    "ACCEL_sst_*|MICROPHONE_sst_*|MAGNETOMETER_sst_*|id"
]

classifiers = [
    'RandomForestClassifier',
    'BernoulliNB',
    'SVC',
    'LogisticRegression'
]

headers = [
    'device', 'feature', 'clf', 'accuracy'
]
headers += [str(i) for i in range(60)]
with open(output_file, "w") as f:
    f.write(','.join(headers) + "\n")

for repeat in range(20):
    for device_i in range(len(devices)):
        device = devices[device_i]

        for feature_i in range(len(features)):
            feature = features[feature_i]

            for clf_i in range(len(classifiers)):
                clf_name = classifiers[clf_i]

                report = test(device, feature, clf_name)
                report = [
                    device_i, feature_i, clf_i
                ] + report
                report = [str(i) for i in report]

                with open(output_file, "a") as f:
                    f.write(','.join(report) + "\n")
