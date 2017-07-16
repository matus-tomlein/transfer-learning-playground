#!/usr/bin/env python3
# -*- coding: utf8 -*-

import tflscripts
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
import sys
import os
import pickle

tested_devices = [

    ['synergy-final-iter1', '128.237.254.195'],  # sink
    ['synergy-final-iter1', '128.237.246.127'],  # coffee
    ['synergy-final-iter1', '128.237.248.186'],  # table

    ['synergy-final-iter1', 'Matrix b827eb96f31a'],
    ['synergy-final-iter1', 'Matrix b827ebe6e0f8'],
    ['synergy-final-iter1', 'Matrix b827eb41f96f'],

    ['synergy-final-iter1', 'xdk_1'],
    ['synergy-final-iter1', 'xdk_2'],
    ['synergy-final-iter1', 'xdk_3'],

    ['synergy-final-iter2', '128.237.248.186'],  # sink
    ['synergy-final-iter2', '128.237.254.195'],  # coffee
    ['synergy-final-iter2', '128.237.246.127'],  # table

    ['synergy-final-iter2', 'Matrix b827eb96f31a'],
    ['synergy-final-iter2', 'Matrix b827ebe6e0f8'],
    ['synergy-final-iter2', 'Matrix b827eb41f96f'],

    ['synergy-final-iter2', 'xdk_1'],
    ['synergy-final-iter2', 'xdk_2'],
    ['synergy-final-iter2', 'xdk_3'],

    ['synergy-final-iter4', '128.237.247.190'],  # table
    ['synergy-final-iter4', '128.237.227.76'],  # sink
    ['synergy-final-iter4', '128.237.250.218'],  # coffee

    ['synergy-final-iter4', 'Matrix b827eb96f31a'],
    ['synergy-final-iter4', 'Matrix b827ebe6e0f8'],
    ['synergy-final-iter4', 'Matrix b827eb41f96f'],

    ['synergy-final-iter4', 'xdk_1'],
    ['synergy-final-iter4', 'xdk_2'],
    ['synergy-final-iter4', 'xdk_3'],

    ['synergy-final-iter5', '128.237.247.190'],  # table
    ['synergy-final-iter5', '128.237.227.76'],  # coffee
    ['synergy-final-iter5', '128.237.250.218'],  # sink

    ['synergy-final-iter5', 'Matrix b827eb96f31a'],
    ['synergy-final-iter5', 'Matrix b827ebe6e0f8'],
    ['synergy-final-iter5', 'Matrix b827eb41f96f'],

    ['synergy-final-iter5', 'xdk_1'],
    ['synergy-final-iter5', 'xdk_2'],
    ['synergy-final-iter5', 'xdk_3'],

    ['scott-final-iter1', '128.237.248.186'],  # left
    ['scott-final-iter1', '128.237.247.134'],  # right
    ['scott-final-iter1', '128.237.246.127'],  # pantry

    ['scott-final-iter1', 'Matrix b827eb96f31a'],
    ['scott-final-iter1', 'Matrix b827ebe6e0f8'],
    ['scott-final-iter1', 'Matrix b827eb41f96f'],

    ['scott-final-iter1', 'xdk_1'],
    ['scott-final-iter1', 'xdk_2'],
    ['scott-final-iter1', 'xdk_3'],

    ['scott-final-iter3', '128.237.227.76'],  # left
    ['scott-final-iter3', '128.237.250.218'],  # right
    ['scott-final-iter3', '128.237.247.190'],  # pantry

    ['scott-final-iter3', 'Matrix b827eb96f31a'],
    ['scott-final-iter3', 'Matrix b827ebe6e0f8'],
    ['scott-final-iter3', 'Matrix b827eb41f96f'],

    ['scott-final-iter3', 'xdk_1'],
    ['scott-final-iter3', 'xdk_2'],
    ['scott-final-iter3', 'xdk_3'],

    ['robotics-final', '128.237.248.186'],  # entrance
    ['robotics-final', '128.237.246.127'],  # coffee
    ['robotics-final', '128.237.247.134'],  # sink

    ['robotics-final', 'Matrix b827eb96f31a'],
    ['robotics-final', 'Matrix b827ebe6e0f8'],
    ['robotics-final', 'Matrix b827eb41f96f'],

    ['robotics-final', 'xdk_1'],
    ['robotics-final', 'xdk_2'],
    ['robotics-final', 'xdk_3'],
]

configuration = tflscripts.read_configuration()

activities = configuration['analysed_activities']
activities_i = [configuration['activities'].index(a) for a in activities]

tflscripts.set_dataset_folder('/home/giotto/transfer-learning-playground/datasets/')


pipelines = []

features_to_use = [
    '.*',
    'MICROPHONE_|microphone',
    'ACCEL_|accel_|mag_',
    'temperature|pressure|humidity',
    'EMI|IRMOTION',
    'MICROPHONE|microphone|ACCEL_|accel_'
]

classifiers = [
    'SVM',
    'RandomForestClassifier',
    'LogisticRegression'
]

datasets = [
    "synergy-final-iter1",
    "synergy-final-iter2",
    "scott-final-iter1",
    "robotics-final",
    "synergy-final-iter4",
    "synergy-final-iter5"
]

device_types = [
    'Mite'
]


def read_dataset(device, dataset):
    df, df_labels = tflscripts.read_and_filter_dataset(
            dataset + '-1s',
            device,
            use_features='.*',
            use_activities=activities_i,
            check_all_activities=False,
            scale=True,
            with_feature_selection=False)

    df = df.loc[df.index.isin(df_labels.index)]
    df_labels = df_labels.loc[df_labels.index.isin(df.index)]

    return df, df_labels


def classifier_with_label(classifier):
    if classifier == 'SVM':
        return svm.SVC(kernel='linear', decision_function_shape='ovr')
    elif classifier == 'RandomForestClassifier':
        return RandomForestClassifier()
    elif classifier == 'LogisticRegression':
        return LogisticRegression()


def fit_pipeline(classifier, x_train, y_train):
    clf = classifier_with_label(classifier)

    ppl = Pipeline([
        ('impute', Imputer()),
        ('clf', clf)
    ])

    ppl.fit(x_train, y_train)

    return ppl

def test_with_transfer(target_dataset, target_device,
        source_device, source_dataset,
        df_source, df_source_labels,
        df_target, df_target_labels,
        label, features,
        classifier, done_tests):

    key = get_test_key(source_dataset=source_dataset,
            source_device=source_device,
            target_device=target_device,
            target_dataset=target_dataset,
            label=label,
            features=features,
            classifier=classifier)

    if key in done_tests:
        print('Skipping test')
        return

    if label not in df_target_labels['label'].values:
        print('Label not in target')
        return

    c1 = df_source.filter(regex=features).columns.tolist()
    c2 = df_target.filter(regex=features).columns.tolist()
    columns = [i for i in c1 if i in c2]
    if len(columns) == 0:
        print('No common columns for the features found')
        return

    x_train = df_source[columns]
    y_train = tflscripts.get_y_for_label(df_source_labels, label)

    ppl = fit_pipeline(classifier, x_train, y_train)

    x_test = df_target[x_train.columns]

    predicted = ppl.predict(x_test)
    result = tflscripts.TestResult(
        source_dataset=source_dataset,
        source_device=source_device,

        target_dataset=target_dataset,
        target_device=target_device,

        predicted=predicted,
        actual_with_all_labels=df_target_labels.label.values,

        classifier=classifier,
        window_size='1s',
        label=label,
        columns=x_train.columns,
        features=features
    )

    test_set = tflscripts.TestSet(name='_'.join([source_dataset,
                                                 source_device]))
    test_set.add_result(result)


def test_without_transfer(df_source, df_source_labels, classifier, label,
        source_device, source_dataset, features, done_tests):

    key = get_test_key(source_dataset=source_dataset,
            source_device=source_device,
            target_device=source_device,
            target_dataset=source_dataset,
            label=label,
            features=features,
            classifier=classifier)
    if key in done_tests:
        print('Skipping test')
        return

    x_train = df_source.filter(regex=features)
    if len(x_train.columns) == 0:
        print('No columns found')
        return
    y_train = tflscripts.get_y_for_label(df_source_labels, label)

    x_train_s, x_test_s, y_train_sl, y_test_sl = train_test_split(
            x_train, df_source_labels['label'], test_size=0.33)
    y_train_s = tflscripts.get_y_for_label_series(y_train_sl,
                                                    label)

    if label in y_test_sl.values and label in y_train_sl.values:
        ppl = fit_pipeline(classifier, x_train_s, y_train_s)
        predicted = ppl.predict(x_test_s)

        result = tflscripts.TestResult(
            source_dataset=source_dataset,
            source_device=source_device,

            target_dataset=source_dataset,
            target_device=source_device,

            predicted=predicted,
            actual_with_all_labels=y_test_sl.values,

            classifier=classifier,
            window_size='1s',
            label=label,
            columns=x_train_s.columns,
            features=features
        )
        test_set = tflscripts.TestSet(name='_'.join([source_dataset,
                                                     source_device]))
        test_set.add_result(result)
    else:
        print('Couldnt split so that label is both in train and test set')


def get_test_key(source_dataset, source_device, target_dataset, target_device,
        label, features, classifier):
    return '-'.join([source_device, source_dataset, target_device,
        target_dataset, str(label), features, classifier])


def previously_done_tests(source_dataset, source_device):
    test_set = tflscripts.TestSet(name='_'.join([source_dataset,
                                                 source_device]))

    tests = {}
    if test_set.exists():
        for r in test_set.get_results():
            key = get_test_key(source_device=r.source_device,
                    source_dataset=r.source_dataset,
                    target_dataset=r.target_dataset,
                    target_device=r.target_device,
                    label=r.label,
                    features=r.features,
                    classifier=r.classifier)
            tests[key] = True

    return tests


def test_for_source_and_target(source_dataset, source_device,
        target_dataset, target_device):
    df_source, df_source_labels = read_dataset(dataset=source_dataset,
                                               device=source_device)
    df_target, df_target_labels = read_dataset(dataset=target_dataset,
                                               device=target_device)

    done_tests = previously_done_tests(source_device=source_device,
            source_dataset=source_dataset)

    l1 = configuration['compared_activities'][source_dataset]
    l2 = configuration['compared_activities'][target_dataset]
    labels = [l for l in l1 if l in l2]
    labels = [configuration['activities'].index(a) for a in labels]

    for label in labels:
        for features in features_to_use:
            for classifier in classifiers:
                test_without_transfer(
                        df_source=df_source,
                        df_source_labels=df_source_labels,
                        source_device=source_device,
                        source_dataset=source_dataset,
                        classifier=classifier,
                        label=label,
                        features=features,
                        done_tests=done_tests)

                test_with_transfer(target_dataset=target_dataset,
                        target_device=target_device,
                        source_device=source_device,
                        source_dataset=source_dataset,
                        df_source=df_source,
                        df_source_labels=df_source_labels,
                        df_target=df_target,
                        df_target_labels=df_target_labels,
                        label=label,
                        features=features,
                        classifier=classifier,
                        done_tests=done_tests)


def test_for_source(source_dataset, source_device):
    for target_dataset_device in tested_devices:
        target_dataset = target_dataset_device[0]
        target_device = target_dataset_device[1]

        if source_dataset == target_dataset and source_device == target_device:
            continue

        os.system('./single_activity_models.py "{}" "{}" "{}" "{}"'.format(
            source_dataset,
            source_device,
            target_dataset,
            target_device
        ))


def test_for_source_dataset(source_dataset):
    for dataset_device in tested_devices:
        dataset = dataset_device[0]
        device = dataset_device[1]

        if dataset == source_dataset:
            os.system('./single_activity_models.py "{}" "{}"'.format(
                source_dataset,
                device
            ))


if __name__ == "__main__":
    # start all analysis
    if len(sys.argv) == 1:

        for source_dataset_device in tested_devices:
            source_dataset = source_dataset_device[0]
            source_device = source_dataset_device[1]

            os.system('./single_activity_models.py "{}" "{}"'.format(
                source_dataset,
                source_device
            ))

    # started with source dataset
    elif len(sys.argv) == 2:
        source_dataset = sys.argv[1]
        print('source dataset', source_dataset)

        test_for_source_dataset(source_dataset=source_dataset)


    # started with source dataset and device
    elif len(sys.argv) == 3:
        source_dataset = sys.argv[1]
        source_device = sys.argv[2]

        print('source dataset', source_dataset)
        print('source device', source_device)

        test_for_source(source_dataset=source_dataset,
                        source_device=source_device)


    # started with source and target dataset and device
    elif len(sys.argv) == 5:
        source_dataset, source_device, target_dataset, \
        target_device = sys.argv[1:5]

        test_for_source_and_target(source_dataset=source_dataset,
                source_device=source_device,
                target_dataset=target_dataset,
                target_device=target_device)

    else:
        print('Wrong number of arguments')
