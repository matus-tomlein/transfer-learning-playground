#!/usr/bin/env python3
# -*- coding: utf8 -*-

import random
import json
import csv

from ml.parallelization import start_workers
from ml.testing import test_transfer

output_file = '/'.join([
    'results',
    'results_feature_testing.csv'
])

datasets = [
    'synergy-final-iter1',
    'synergy-final-iter2',
    'scott-final-iter1'
]

devices_to_use = [
    '128.237.248.186',
    'Matrix b827ebe6e0f8',
    'DialogIoT 591844765',
    'TI SensorTag 690',
    'xdk_1',
]

classifiers = [
    'RandomForestClassifier'
]

use_activities_with_length = [
    11
]

number_of_samples = 100000

with open('tsfresh_feature_types.json') as f:
    tsfresh_feature_types = json.load(f)


# the configuration file is used to find indices to represent devices and other
with open('configuration.json') as f:
    configuration = json.load(f)


# write headers to the CSV file
headers = [
    'source_device', 'target_device',
    'source_dataset', 'target_dataset',
    'activities', 'feature',
    'accuracy', 'precision_recall_fscore_support',
    'confusion_matrix'
]
headers += tsfresh_feature_types

with open(output_file, "w") as f:
    writer = csv.writer(f,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)


def worker(q):
    ds = random.sample(datasets, len(datasets))

    for sample_i in range(number_of_samples):
        feature_types = random.sample(tsfresh_feature_types,
                                      len(tsfresh_feature_types))[:10]

        use_columns = ['accel_x__' + t for t in feature_types]
        use_columns += ['accel_y__' + t for t in feature_types]
        use_columns += ['accel_z__' + t for t in feature_types]

        # main loop that goes through all the combinations of inputs and
        # computes the classification performance
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
                            activities_i = [configuration['activities'].index(a) for a in activities]

                            if not len(activities) in use_activities_with_length:
                                continue

                            for repeat in range(10):
                                try:
                                    report = test_transfer(
                                            source_device=source_device,
                                            target_device=target_device,
                                            source_dataset_path=source_dataset_path,
                                            target_dataset_path=target_dataset_path,
                                            use_columns=use_columns,
                                            use_activities=activities_i)
                                    if report is None:
                                        continue

                                    report = [
                                        source_i, target_i,
                                        source_dataset_i, target_dataset_i,
                                        activity_i, 7
                                    ] + report

                                    report += [1 if f in feature_types else 0 for f in tsfresh_feature_types]

                                    report = [str(i) for i in report]

                                    q.put(report)
                                except Exception as error:
                                    print(str(error))


start_workers(worker=worker, output_file=output_file, num_jobs=2)