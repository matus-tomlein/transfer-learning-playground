#!/usr/bin/env python3
# -*- coding: utf8 -*-

import random
import json
import csv

from ml.parallelization import start_workers
from ml.testing import test_transfer

output_file = '/'.join([
    'results',
    'results_transfer_complete_features.csv'
])

datasets = [
    'synergy-final-iter1',
    'synergy-final-iter2',
    'scott-final-iter1',
    'scott-final-iter2',
    'robotics-final'
]

devices_to_use = [
    '128.237.246.127',
    '128.237.248.186',
    '128.237.247.134',
    '128.237.254.195',
    'Matrix b827eb96f31a',
    'Matrix b827ebe6e0f8',
    'Matrix b827eb41f96f',
    'DialogIoT 591844595',
    'DialogIoT 591844599',
    'DialogIoT 591844765',
    'TI SensorTag 604',
    'TI SensorTag 690',
    'TI SensorTag 85',
    'xdk_1',
    'xdk_2',
    'xdk_3'
]

classifiers = [
    'RandomForestClassifier'
]

use_activities_with_length = [
    11
]

# the configuration file is used to find indices to represent devices and other
with open('configuration.json') as f:
    configuration = json.load(f)

with open('tsfresh_feature_types.json') as f:
    tsfresh_feature_types = json.load(f)

sensor_streams = [
   'accel_x',
   'accel_y',
   'accel_z',
   'gyro_x',
   'gyro_y',
   'gyro_z',
   'mag_x',
   'mag_y',
   'mag_z',
   'humidity',
   'light',
   'pressure',
   'temperature',
   'microphone'
]

force_columns = [stream + '__' + feature for feature in
                 tsfresh_feature_types for stream in sensor_streams]


# write headers to the CSV file
headers = [
    'source_device', 'target_device',
    'source_dataset', 'target_dataset',
    'activities',
    'feature', 'clf', 'feature_selection',
    'scaled_independently',
    'accuracy', 'precision_recall_fscore_support',
    'confusion_matrix'
]
with open(output_file, "w") as f:
    writer = csv.writer(f,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)

feature_i = 17


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
                if source_device not in devices_to_use:
                    continue

                target_roles = configuration['device_roles'][target_dataset]
                for target_device in target_roles:
                    if target_device not in devices_to_use:
                        continue

                    source_i = configuration['devices'].index(source_device)
                    target_i = configuration['devices'].index(target_device)

                    if source_dataset == target_dataset and source_device == \
                            target_device:
                        continue

                    for activity_i, activities in \
                            enumerate(configuration['activity_sets']):
                        activities_i = [configuration['activities'].index(a)
                                        for a in activities]

                        if not len(activities) in use_activities_with_length:
                            continue

                        for clf_name in classifiers:
                            clf_i = configuration['classifiers'].index(clf_name)

                            for repeat in range(10):
                                scale_independently = repeat % 2 == 0

                                try:
                                    report = test_transfer(
                                            source_device=source_device,
                                            target_device=target_device,
                                            source_dataset_path=source_dataset_path,
                                            target_dataset_path=target_dataset_path,
                                            force_columns=force_columns,
                                            use_activities=activities_i,
                                            scale_domains_independently=scale_independently,
                                            clf_name=clf_name)
                                    if report is None:
                                        continue

                                    report = [
                                        source_i, target_i,
                                        source_dataset_i, target_dataset_i,
                                        activity_i,
                                        feature_i,
                                        clf_i,
                                        0,  # feature selection
                                        1 if scale_independently else 0
                                    ] + report
                                    report = [str(i) for i in report]

                                    q.put(report)
                                except Exception as error:
                                    print(str(error))


start_workers(worker=worker, output_file=output_file, num_jobs=2)
