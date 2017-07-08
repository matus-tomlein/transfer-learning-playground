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
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score


NEGATIVE_ACCURACY_THRESHOLD = 0.95
POSITIVE_ACCURACY_THRESHOLD = 0.0

configuration = tflscripts.read_configuration()


def classifier_with_label(classifier):
    if classifier == 'SVM':
        return svm.SVC(kernel='linear', decision_function_shape='ovr')
    elif classifier == 'RandomForestClassifier':
        return RandomForestClassifier()
    elif classifier == 'LogisticRegression':
        return LogisticRegression()


def key_for_test_result(result):
    return result.source_dataset + result.source_device + \
            result.target_dataset + result.target_device + \
            result.label_name() + result.features + result.classifier


def accuracy_positive(y, predicted, label):
    y_positive = y[y == label]
    predicted_positive = predicted[y == label]
    return accuracy_score(y_positive, predicted_positive)


def accuracy_negative(y, predicted, label):
    y_negative = y[y != label]
    y_negative = np.array([-1] * len(y_negative))
    predicted_negative = predicted[y != label]
    return accuracy_score(y_negative, predicted_negative)


def recallibrate_test_result(result):
    if result.source_device == result.target_device and \
        result.source_dataset == result.target_dataset:
        return None

    label = result.label
    negative_ok = accuracy_negative(result.actual_with_all_labels, result.predicted, label) > NEGATIVE_ACCURACY_THRESHOLD
    positive_ok = accuracy_positive(result.actual_with_all_labels, result.predicted, label) > POSITIVE_ACCURACY_THRESHOLD

    use_features = '.*'

    if negative_ok and positive_ok:
        df, df_labels = tflscripts.read_and_filter_dataset(
                result.target_dataset + '-1s',
                result.target_device,
                use_features=use_features,
                use_activities=np.unique(result.actual_with_all_labels),
                check_all_activities=False,
                scale=True,
                with_feature_selection=False
        )

        df = df.loc[df.index.isin(df_labels.index)]
        df_labels = df_labels.loc[df_labels.index.isin(df.index)]

        predicted = pd.Series(result.predicted)
        predicted.index = df.index

        negative_index = df[df_labels.label != label].index
        positive_predictions = predicted[predicted != -1]
        positive_predictions_index = positive_predictions.index
        included_index = np.unique(negative_index.tolist() + positive_predictions_index.tolist())

        x_train = df.loc[df.index.isin(included_index)]

        y_train = pd.Series(-1, index=x_train.index)
        y_train[positive_predictions.index] = label

        ppl = Pipeline([
            ('impute', Imputer()),
            ('clf', classifier_with_label(result.classifier))
            ])

        ppl.fit(x_train, y_train)
        repredicted = ppl.predict(df)

        recallibrated_result = tflscripts.RecalibratedTestResult(test_result=result,
                features=use_features,
                classifier=result.classifier,
                predicted=repredicted)

        return recallibrated_result

    return None


def previously_recallibrated_tests(test_set):
    tests = {}

    if test_set.exists():
        for result in test_set.get_results():
            key = key_for_test_result(result.test_result)
            tests[key] = True

    return tests


def recallibrate_results_for(dataset, device):
    test_set = tflscripts.TestSet(name='_'.join([dataset, device]))

    recallibrated_test_set_name = '_'.join([dataset, device]) + '_recallibrated'
    recallibrated_test_set = tflscripts.TestSet(name=recallibrated_test_set_name)

    done_tests = previously_recallibrated_tests(recallibrated_test_set)

    if test_set.exists():
        for result in test_set.get_results():
            key = key_for_test_result(result)
            if key in done_tests:
                continue

            recallibrated_result = recallibrate_test_result(result)

            if recallibrated_result is not None:
                recallibrated_test_set.add_result(recallibrated_result)

    else:
        print('Test set doesnt exist')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Wrong number of arguments')
    else:
        dataset = sys.argv[1]
        device = sys.argv[2]

        print('dataset', dataset)
        print('device', device)

        recallibrate_results_for(dataset=dataset,
                                 device=device)
