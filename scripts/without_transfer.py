#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import os
import json

from ml.data_split import split_one_df
from ml.classification import classify, log_of_classification_results

datasets = [
    'synergy-final-iter1',
    'synergy-final-iter2',
    'scott-final-iter1',
    'scott-final-iter2',
    'robotics-final'
]

mite_features = [
    "accel_*",
    "mag*",
    "accel_*|mag*"
    "microphone",
    "accel_*|microphone",
    "temperature",
    "temperature|accel_*|microphone"
]

matrix_features = mite_features

dialog_features = [
    "accel_*",
    "mag*",
    "accel_*|mag*"
]

sensortag_features = dialog_features
bosch_features = dialog_features + [
    'microphone',
    "accel_*|microphone",
    'temperature',
    "temperature|accel_*|microphone"
]

device_features = {
    '128.237.246.127': mite_features,
    '128.237.248.186': mite_features,
    '128.237.247.134': mite_features,
    '128.237.254.195': mite_features,
    'Matrix b827eb96f31a': matrix_features,
    'Matrix b827ebe6e0f8': matrix_features,
    'Matrix b827eb41f96f': matrix_features,
    'DialogIoT 591844595': dialog_features,
    'DialogIoT 591844599': dialog_features,
    'DialogIoT 591844765': dialog_features,
    'TI SensorTag 604': sensortag_features,
    'TI SensorTag 690': sensortag_features,
    'TI SensorTag 85': sensortag_features,
    'xdk_1': bosch_features,
    'xdk_2': bosch_features,
    'xdk_3': bosch_features
}

classifiers = [
    'RandomForestClassifier'
]


def test(device, use_features, clf_name, with_feature_selection,
        activities_to_use, dataset_path):
    print(device,
          use_features,
          clf_name,
          str(with_feature_selection),
          dataset_path)
    file_name = device
    if with_feature_selection:
        file_name += '_selected'
    df = pd.read_pickle(dataset_path + file_name + '.p')

    df_labels = pd.read_pickle(dataset_path + device + '_labels.p')

    ## filter activities
    df_labels = df_labels.loc[df_labels.label.isin(activities_to_use)]
    df = df.loc[df.index.isin(df_labels.index)]

    ## filter features
    df = df.filter(regex=(use_features))
    if len(df.columns) == 0:
        print('No features found for')
        return None

    X_train, y_train, X_test, y_test = split_one_df(df, df_labels, 0.7)
    try:
        y_pred = classify(X_train, y_train, X_test, clf_name)
    except ValueError as ex:
        print(ex)
        return None

    r = log_of_classification_results(y_test, y_pred)

    return r


with open('configuration.json') as f:
    configuration = json.load(f)

output_file = '/'.join([
    'results',
    'results_no_transfer.csv'
])
os.makedirs(os.path.dirname(output_file), exist_ok=True)

headers = [
    'dataset', 'device', 'feature', 'clf', 'feature_selection', 'accuracy'
]
headers += [str(i) for i in range(165)]
with open(output_file, "w") as f:
    f.write(','.join(headers) + "\n")

activities = [
    'Dishes',
    'Microwave',
    'Coffee',
    'Null',
    'Faucet',
    'Kettle',
    'Chopping food',
    'Conversation',
    'Eating popcorn',
    'Making popcorn in microwave',
    'Phone vibrating'
]

activities = [configuration['activities'].index(a) for a in activities]

for dataset in datasets:
    dataset_i = configuration['datasets'].index(dataset)
    dataset_path = '../datasets/' + dataset + '-features/'

    roles = configuration['device_roles'][dataset]
    for device in roles:
        device_i = configuration['devices'].index(device)

        features = device_features[device]
        for feature in features:
            feature_i = configuration['features'].index(feature)

            for clf_name in classifiers:
                clf_i = configuration['classifiers'].index(clf_name)

                for repeat in range(40):
                    with_feature_selection = repeat % 2 == 0

                    report = test(device=device,
                            use_features=feature,
                            clf_name=clf_name,
                            with_feature_selection=with_feature_selection,
                            activities_to_use=activities,
                            dataset_path=dataset_path)
                    if report is None:
                        continue

                    report = [
                        dataset_i, device_i, feature_i, clf_i,
                        1 if with_feature_selection else 0
                    ] + report
                    report = [str(i) for i in report]

                    with open(output_file, "a") as f:
                        f.write(','.join(report) + "\n")
