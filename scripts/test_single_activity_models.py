#!/usr/bin/env python3
# -*- coding: utf8 -*-

import tflscripts
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

activities = [
    "Dishes",
    "Microwave",
    "Coffee",
    "Null",
    "Kettle",
    "Chopping food",
    "Conversation",
    "Eating popcorn",
    "Knocking",
    "Phone vibrating",
    "Microwave button press",
    "Microwave door opened",
    "Microwave door closed"
]

configuration = tflscripts.read_configuration()
activities_i = [configuration['activities'].index(a) for a in activities]

tflscripts.set_dataset_folder('/home/giotto/transfer-learning-playground/datasets/')


devices = [
    ['synergy-final-iter1', '128.237.254.195'],  # sink
    ['synergy-final-iter1', '128.237.246.127'],  # coffee
    ['synergy-final-iter1', '128.237.248.186'],  # table
    ['synergy-final-iter2', '128.237.248.186'],  # sink
    ['synergy-final-iter2', '128.237.254.195'],  # coffee
    ['synergy-final-iter2', '128.237.246.127'],  # table
#     ['synergy-final-iter3', '128.237.237.122', 'Synergy 3 sink'], # sink
#     ['synergy-final-iter3', '128.237.239.234', 'Synergy 3 coffee'], # coffee
#     ['synergy-final-iter3', '128.237.234.0', 'Synergy 3 table'], # table
    ['scott-final-iter1', '128.237.248.186'],  # left
    ['scott-final-iter1', '128.237.247.134'],  # right
    ['robotics-final', '128.237.246.127'],  # coffee
    ['robotics-final', '128.237.247.134'],  # sink
    ['robotics-final', '128.237.248.186'],  # entrance
]
pipelines = []

features_to_use = [
    '.*',
    'MICROPHONE',
    'ACCEL',
    'EMI',
    'MICROPHONE|ACCEL_'
]

classifiers = [
    'SVM',
    'RandomForestClassifier',
    'LogisticRegression'
]


test_set = tflscripts.TestSet(name='single_activity_models')


for source in devices:
    source_dataset = source[0]
    source_device = source[1]

    df_source, df_source_labels = tflscripts.read_and_filter_dataset(
            source_dataset + '-1s',
            source_device,
            use_features='.*',
            use_activities=activities_i,
            scale=True,
            with_feature_selection=False)

    df_source = df_source.loc[df_source.index.isin(df_source_labels.index)]
    df_source_labels = df_source_labels.loc[df_source_labels.index.isin(df_source.index)]

    for label in df_source_labels.label.unique():
        for features in features_to_use:
            x_train = df_source.filter(regex=features)
            y_train = tflscripts.get_y_for_label(df_source_labels, label)

            for classifier in classifiers:
                if classifier == 'SVM':
                    clf = svm.SVC(kernel='linear', decision_function_shape='ovr')
                elif classifier == 'RandomForestClassifier':
                    clf = RandomForestClassifier()
                elif classifier == 'LogisticRegression':
                    clf = LogisticRegression()

                ppl = Pipeline([
                    ('impute', Imputer()),
                    ('clf', clf)
                ])

                ppl.fit(x_train, y_train)

                for target in devices:
                    target_dataset = target[0]
                    target_device = target[1]

                    if source_dataset == target_dataset and source_device == target_device:
                        continue

                    label_pipelines = {}

                    df_target, df_target_labels = tflscripts.read_and_filter_dataset(
                        target_dataset + '-1s',
                        target_device,
                        use_features='.*',
                        use_activities=activities_i,
                        scale=True,
                        with_feature_selection=False)

                    df_target = df_target.loc[df_target.index.isin(df_target_labels.index)]

                    y_test = tflscripts.get_y_for_label(df_target_labels, label)
                    x_test = df_target[x_train.columns]

                    predicted = ppl.predict(x_test)
                    result = tflscripts.TestResult(
                        source_dataset=source_dataset,
                        source_device=source_device,

                        target_dataset=target_dataset,
                        target_device=target_device,

                        predicted=predicted,
                        actual=y_test.values,
                        actual_with_all_labels=df_target_labels.label.values,

                        classifier=classifier,
                        window_size='1s',
                        label=label,
                        columns=x_train.columns,
                        features=features
                    )

                    test_set.add_result(result)
