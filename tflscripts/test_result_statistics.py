import pandas as pd
import numpy as np
import json
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score

dataset_folder = '../datasets/'

longer_activities = [
    "Dishes",
    "Microwave",
    "Coffee",
    "Faucet",
    "Kettle",
    "Chopping food",
    "Conversation",
    "Eating popcorn",
    "Making popcorn in microwave",
    "Frequency sweep",
    "Phone vibrating",
    "Vacuum cleaning",
    "Blender running",
    "Alarm"
]

def get_longer_activities_i(configuration):
    return [configuration['activities'].index(a) for a in longer_activities]

def get_null_i(configuration):
    return configuration['activities'].index("Null")

class TestResultStatistics:
    def __init__(self, result, configuration):
        self.result = result
        self.configuration = configuration

    def actual_labels(self):
        return np.array([l if l == self.result.label else -1 for l in self.result.actual_with_all_labels])

    def accuracy(self):
        predicted = self.result.predicted
        actual = self.actual_labels()
        return accuracy_score(actual, predicted)

    def specificity(self):
        predicted = self.result.predicted
        actual = self.actual_labels()
        mask_negative = actual == -1
        return accuracy_score(actual[mask_negative], predicted[mask_negative])

    def specificity_some_activities(self, num_additional_activities):
        null_i = get_null_i(self.configuration)
        longer_activities_i = get_longer_activities_i(self.configuration)

        predicted = self.result.predicted
        actual = self.result.actual_with_all_labels
        wanted_activities = [null_i]
        if num_additional_activities > 0:
            available_additional = np.unique(self.result.actual_with_all_labels)
            available_additional = np.setdiff1d(available_additional, [null_i, self.result.label])
            available_additional = np.intersect1d(available_additional, longer_activities_i)
            available_additional = np.random.choice(available_additional, num_additional_activities)

            wanted_activities = np.append(wanted_activities, available_additional).tolist()

        mask_negative = [i in wanted_activities for i in actual]

#         mask_negative = actual == -1
        actual = self.actual_labels()

        return accuracy_score(actual[mask_negative], predicted[mask_negative])

    def specificity_with_additional_activities(self, additional_activities):
        null_i = get_null_i(self.configuration)

        predicted = self.result.predicted
        actual = self.result.actual_with_all_labels
        wanted_activities = [null_i]
        wanted_activities = np.append(wanted_activities, additional_activities).tolist()

        mask_negative = [i in wanted_activities for i in actual]

#         mask_negative = actual == -1
        actual = self.actual_labels()

        return accuracy_score(actual[mask_negative], predicted[mask_negative])


    def recall(self):
        predicted = self.result.predicted
        actual = self.actual_labels()
        return recall_score(actual, predicted, pos_label=self.result.label, average='binary')

    def precision(self):
        predicted = self.result.predicted
        actual = self.actual_labels()
        return precision_score(actual, predicted, pos_label=self.result.label, average='binary')

    def f1(self):
        predicted = self.result.predicted
        actual = self.actual_labels()
        return f1_score(actual, predicted, pos_label=self.result.label, average='binary')

    def all_activities(self):
        labels = np.unique(self.result.actual_with_all_labels)
        return [self.configuration['activities'][l] for l in labels]

    def source_device_name(self):
        result = self.result
        return self.configuration['device_roles'][result.source_dataset][result.source_device]

    def target_device_name(self):
        result = self.result
        return self.configuration['device_roles'][result.target_dataset][result.target_device]

    def source_room(self):
        return self.result.source_dataset.split('-')[0]

    def target_room(self):
        return self.result.target_dataset.split('-')[0]

    def source_placement(self):
        return self.source_device_name().split(' ')[2]

    def target_placement(self):
        return self.target_device_name().split(' ')[2]

    def source_device_type(self):
        return self.source_device_name().split(' ')[0]

    def target_device_type(self):
        return self.target_device_name().split(' ')[0]

    def source_device(self):
        return ' '.join(self.source_device_name().split(' ')[0:2])

    def target_device(self):
        return ' '.join(self.target_device_name().split(' ')[0:2])

    def classifier_name(self):
        return self.result.classifier

    def features_name(self):
        feature_types = {
            '.*': 'All',
            'MICROPHONE_|microphone': 'Microphone',
            'ACCEL_|accel_': 'Accelerometer',
            'ACCEL_|accel_|mag_': 'Accelerometer & magnetometer',
            'temperature|pressure|humidity': 'Environmental',
            'EMI|IRMOTION': 'EMI & motion',
            'MICROPHONE|microphone|ACCEL_|accel_': 'Microphone & accelerometer'
        }
        return feature_types[self.result.features]

    def type_of_transfer(self):
        result = self.result
        same_room = self.source_room() == self.target_room()

        source_device_split = self.source_device_name().split(' ')
        target_device_split = self.target_device_name().split(' ')

        same_device_type = source_device_split[0] == target_device_split[0]
        same_device = same_device_type and source_device_split[1] == target_device_split[1]

        if same_room:
            same_place = source_device_split[2] == target_device_split[2]

            if result.source_dataset == result.target_dataset and \
                same_device:
                return 'No transfer'

            if same_device and same_place:
                return 'Same device in same place'

            if same_place and same_device_type:
                return 'Same device type in same place'

            if same_place:
                return 'Different device in same place'

            if same_device:
                return 'Same device in different place'

            if same_device_type:
                return 'Same device type in different place'

            return 'Different device in different place'

        else:
            if same_device:
                return 'Same device across spaces'

            if same_device_type:
                return 'Same device type across spaces'

            return 'Different device across spaces'
