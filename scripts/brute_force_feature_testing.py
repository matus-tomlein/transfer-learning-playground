#!/usr/bin/env python3
# -*- coding: utf8 -*-

import random
import json
import csv

from tflscripts import read_configuration
from tflscripts import start_workers
from tflscripts import test_with_or_without_transfer

output_file = '/'.join([
    '..',
    'results',
    'results_feature_testing_1.csv'
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

number_of_samples = 30000

with open('tsfresh_feature_types.json') as f:
    tsfresh_feature_types = json.load(f)


# the configuration file is used to find indices to represent devices and other
configuration = read_configuration()


# write headers to the CSV file
headers = [
    'source_device', 'target_device',
    'source_dataset', 'target_dataset',
    'activities', 'feature',
    'scaled_independently',
    'accuracy', 'precision_recall_fscore_support',
    'confusion_matrix'
]
headers += tsfresh_feature_types

features = {
    "accel_": ['accel_x', 'accel_y', 'accel_z'],
    "microphone": ['microphone'],
    "mag_": ['mag_x', 'mag_y', 'mag_z']
}

with open(output_file, "w") as f:
    writer = csv.writer(f,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)


def worker(q):
    for sample_i in range(number_of_samples):
        feature_types = random.sample(tsfresh_feature_types,
                                      len(tsfresh_feature_types))[:10]

        for feature_key in features:
            feature_i = configuration['features'].index(feature_key)

            use_columns = []
            for f in features[feature_key]:
                use_columns += [f + '__' + t for t in feature_types]

            ds = random.sample(datasets, len(datasets))
            # main loop that goes through all the combinations of inputs and
            # computes the classification performance
            for ds_i, source_dataset in enumerate(ds):
                source_dataset_i = configuration['datasets'].index(source_dataset)

                for target_dataset in ds:
                    target_dataset_i = configuration['datasets'].index(target_dataset)

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

                            for activity_i, activities in \
                                    enumerate(configuration['activity_sets']):
                                activities_i = [configuration['activities'].index(a) for a in activities]

                                if not len(activities) in use_activities_with_length:
                                    continue

                                for repeat in range(10):
                                    scale_independently = False

                                    try:
                                        report = test_with_or_without_transfer(
                                                source_device=source_device,
                                                target_device=target_device,
                                                source_dataset=source_dataset,
                                                target_dataset=target_dataset,
                                                use_columns=use_columns,
                                                use_activities=activities_i)
                                        if report is None:
                                            continue

                                        report = [
                                            source_i, target_i,
                                            source_dataset_i, target_dataset_i,
                                            activity_i, feature_i,
                                            1 if scale_independently else 0
                                        ] + report

                                        report += [1 if f in feature_types else 0 for f in tsfresh_feature_types]

                                        report = [str(i) for i in report]

                                        q.put(report)
                                    except Exception as error:
                                        print(str(error))


start_workers(worker=worker, output_file=output_file, num_jobs=2)
