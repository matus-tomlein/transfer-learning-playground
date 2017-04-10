#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import random
import json
import csv

from ml.data_split import X_sort, take_percentage_of_data
from ml.classification import classify, log_of_classification_results
from ml.filtering import filter_by_features, filter_by_activities
from ml.parallelization import start_workers

output_file = '/'.join([
    'results',
    'results_transfer_2.csv'
])

datasets = [
    'synergy-final-iter1',
    'synergy-final-iter2',
    'scott-final-iter1',
    'scott-final-iter2',
    'robotics-final'
]

mite_features = [
    "accel_",
    "mag_",
    "accel_|mag_",
    "microphone",
    "accel_|microphone",
    "temperature",
    "temperature|accel_|microphone"
]

matrix_features = mite_features

dialog_features = [
    "accel_",
    "mag_",
    "accel_|mag_"
]

sensortag_features = dialog_features
bosch_features = dialog_features + [
    "microphone",
    "accel_|microphone",
    "temperature",
    "temperature|accel_|microphone"
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

use_activities_with_length = [
    11, 5
]


# test the performance of classification
def test(source_device, target_device, source_dataset_path,
         target_dataset_path,
         use_features, use_activities, with_feature_selection, clf_name):
    # print(source_device, target_device, source_dataset_path, target_dataset_path)
    source_file_name = source_device + '_selected' if with_feature_selection else source_device

    # read features
    df_source = pd.read_pickle(source_dataset_path + source_file_name + '.p')
    df_target = pd.read_pickle(target_dataset_path + target_device + '.p')

    # read labels
    df_source_labels = pd.read_pickle(source_dataset_path + source_device + '_labels.p')
    df_target_labels = pd.read_pickle(target_dataset_path + target_device + '_labels.p')

    # filter features
    df_source, df_target = filter_by_features(df_source, df_target,
                                              use_features)
    if df_source is None:
        return None

    # filter activities
    df_source, df_source_labels, df_target, df_target_labels = \
        filter_by_activities(
            df_source, df_source_labels, df_target,
            df_target_labels, use_activities)
    if df_source is None:
        return None

    # filter samples
    ratio = 0.6
    df_source, df_source_labels = take_percentage_of_data(
            df_source,
            df_source_labels, ratio)
    df_target, df_target_labels = take_percentage_of_data(
            df_target,
            df_target_labels, ratio)

    y_source = df_source_labels['label']
    y_target = df_target_labels['label']

    # sort feature columns
    X_source = X_sort(df_source)
    X_target = X_sort(df_target)

    # feature_hash = get_feature_hash(df_source)

    try:
        y_target_pred = classify(X_source, y_source, X_target, clf_name)
    except ValueError as ex:
        print(ex)
        return None

    r = log_of_classification_results(y_target, y_target_pred)
    return r


# the configuration file is used to find indices to represent devices and other
with open('configuration.json') as f:
    configuration = json.load(f)


# write headers to the CSV file
headers = [
    'source_device', 'target_device',
    'source_dataset', 'target_dataset',
    'activities',
    'feature', 'clf', 'feature_selection',
    'accuracy', 'precision_recall_fscore_support',
    'confusion_matrix'
]
with open(output_file, "w") as f:
    writer = csv.writer(f,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)


def worker(q):
    ds = random.sample(datasets, len(datasets))

    # main loop that goes through all the combinations of inputs and computes
    # the classification performance
    for ds_i, source_dataset in enumerate(ds):
        source_dataset_i = configuration['datasets'].index(source_dataset)
        source_dataset_path = '../datasets/' + source_dataset + '-features/'

        for target_dataset in ds:
            target_dataset_i = configuration['datasets'].index(target_dataset)
            target_dataset_path = '../datasets/' + target_dataset + '-features/'

            source_roles = configuration['device_roles'][source_dataset]
            for source_device in source_roles:

                target_roles = configuration['device_roles'][target_dataset]
                for target_device in target_roles:
                    source_i = configuration['devices'].index(source_device)
                    target_i = configuration['devices'].index(target_device)

                    if source_dataset == target_dataset and source_device == \
                            target_device:
                        continue

                    for activity_i, activities in \
                            enumerate(configuration['activity_sets']):
                        activities_i = [configuration['activities'].index(a) for a in activities]

                        if not len(activities) in use_activities_with_length:
                            continue

                        features = device_features[source_device]
                        for use_features in features:
                            feature_i = configuration['features'].index(use_features)

                            for clf_name in classifiers:
                                clf_i = configuration['classifiers'].index(clf_name)

                                for repeat in range(10):
                                    with_feature_selection = repeat % 2 == 0

                                    try:
                                        report = test(
                                                source_device=source_device,
                                                target_device=target_device,
                                                source_dataset_path=source_dataset_path,
                                                target_dataset_path=target_dataset_path,
                                                use_features=use_features,
                                                use_activities=activities_i,
                                                with_feature_selection=with_feature_selection,
                                                clf_name=clf_name)
                                        if report is None:
                                            continue

                                        report = [
                                            source_i, target_i,
                                            source_dataset_i, target_dataset_i,
                                            activity_i,
                                            feature_i, clf_i,
                                            1 if with_feature_selection else 0
                                        ] + report
                                        report = [str(i) for i in report]

                                        q.put(report)
                                    except Exception as error:
                                        print(str(error))

        print(str(ds_i) + ' out of ' + str(len(ds)))


start_workers(worker=worker, output_file=output_file, num_jobs=2)
