#!/usr/bin/env python3
# -*- coding: utf8 -*-

import csv
import traceback

from tflscripts import start_workers, test_with_or_without_transfer, \
        read_configuration

output_file = '/'.join([
    '..',
    'results',
    'results_transfer.csv'
])

datasets = {
    'synergy-final-iter1',
    'synergy-final-iter2',
    'synergy-final-iter3',
    'scott-final-iter1',
    'robotics-final'
}

# devices = [
#     'ALL'
# ]

features = [
    "accel_",
    "microphone",
    "accel_|microphone|mag_",
    "accel_|mag_",
    "temperature|accel_|gyro_|microphone|humidity|pressure|light"
]

classifiers = [
    'RandomForestClassifier'
]

use_activities_with_length = [
    11
]


# the configuration file is used to find indices to represent devices and other
configuration = read_configuration()


# write headers to the CSV file
headers = [
    'source_device', 'target_device',
    'source_dataset', 'target_dataset',
    'activities',
    'feature', 'clf', 'feature_selection',
    'scaled_independently', 'target_training_data',
    'source_training_data',
    'easy_domain_adaptation',
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
    # main loop that goes through all the combinations of inputs and computes
    # the classification performance
    for source_dataset in datasets:
        source_dataset_i = configuration['datasets'].index(source_dataset)

        for target_dataset in datasets:
            target_dataset_i = configuration['datasets'].index(target_dataset)

            for source_device in configuration['device_roles'][source_dataset]:

                for target_device in configuration['device_roles'][target_dataset]:

                    source_i = configuration['devices'].index(source_device)
                    target_i = configuration['devices'].index(target_device)

                    # source_device_type = configuration['device_types'][source_i]
                    # target_device_type = configuration['device_types'][target_i]

                    for activity_i, activities in \
                            enumerate(configuration['activity_sets']):
                        activities_i = [configuration['activities'].index(a) for a in activities]

                        if not len(activities) in use_activities_with_length:
                            continue

                        for use_features in features:
                            feature_i = configuration['features'].index(use_features)

                            for clf_name in classifiers:
                                clf_i = configuration['classifiers'].index(clf_name)

                                target_data_ratio = 0.0
                                source_training_data = 0.6

                                for repeat in range(10):
                                    with_feature_selection = repeat % 2 == 0
                                    scale_independently = False
                                    use_easy_domain_adaptation = False

                                    try:
                                        report = test_with_or_without_transfer(
                                                source_device=source_device,
                                                target_device=target_device,
                                                source_dataset=source_dataset,
                                                target_dataset=target_dataset,
                                                use_features=use_features,
                                                use_activities=activities_i,
                                                training_source_data_ratio=source_training_data,
                                                training_target_data_ratio=target_data_ratio,
                                                with_feature_selection=with_feature_selection,
                                                scale_domains_independently=scale_independently,
                                                use_easy_domain_adaptation=use_easy_domain_adaptation,
                                                clf_name=clf_name)
                                        if report is None:
                                            continue

                                        report = [
                                            source_i, target_i,
                                            source_dataset_i, target_dataset_i,
                                            activity_i,
                                            feature_i, clf_i,
                                            1 if with_feature_selection else 0,
                                            1 if scale_independently else 0,
                                            target_data_ratio,
                                            source_training_data,
                                            1 if use_easy_domain_adaptation else 0
                                        ] + report
                                        report = [str(i) for i in report]

                                        q.put(report)
                                    except Exception as error:
                                        print('ex', str(error))
                                        # traceback.print_exc()


start_workers(worker=worker, output_file=output_file, num_jobs=2)
