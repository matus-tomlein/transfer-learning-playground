#!/usr/bin/env python3
# -*- coding: utf8 -*-

import random
import json
import csv

from ml.parallelization import start_workers
from ml.testing import test_transfer

output_file = '/'.join([
    'results',
    'results_transfer.csv'
])

datasets = [
    'synergy-final-iter1',
    'synergy-final-iter2',
    'scott-final-iter1',
    'scott-final-iter2',
    'robotics-final'
]

features = [
    "accel_.*index_mass_quantile",
    "mag_.*index_mass_quantile",
    "microphone.*index_mass_quantile",
    "accel_.*index_mass_quantile|microphone.*index_mass_quantile|mag_.*index_mass_quantile",
    "accel_.*index_mass_quantile|mag_.*index_mass_quantile",
    "temperature.*index_mass_quantile|accel_.*index_mass_quantile|gyro_.*index_mass_quantile|microphone.*index_mass_quantile|humidity.*index_mass_quantile|pressure.*index_mass_quantile|light.*index_mass_quantile"
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

                        for use_features in features:
                            feature_i = configuration['features'].index(use_features)

                            for clf_name in classifiers:
                                clf_i = configuration['classifiers'].index(clf_name)

                                for repeat in range(10):
                                    with_feature_selection = False
                                    scale_independently = False

                                    try:
                                        report = test_transfer(
                                                source_device=source_device,
                                                target_device=target_device,
                                                source_dataset_path=source_dataset_path,
                                                target_dataset_path=target_dataset_path,
                                                use_features=use_features,
                                                use_activities=activities_i,
                                                with_feature_selection=with_feature_selection,
                                                scale_domains_independently=scale_independently,
                                                clf_name=clf_name)
                                        if report is None:
                                            continue

                                        report = [
                                            source_i, target_i,
                                            source_dataset_i, target_dataset_i,
                                            activity_i,
                                            feature_i, clf_i,
                                            1 if with_feature_selection else 0,
                                            1 if scale_independently else 0
                                        ] + report
                                        report = [str(i) for i in report]

                                        q.put(report)
                                    except Exception as error:
                                        print(str(error))


start_workers(worker=worker, output_file=output_file, num_jobs=2)
