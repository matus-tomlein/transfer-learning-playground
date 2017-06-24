import tflscripts
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split

activities = [
    "Dishes",
    "Microwave",
    "Coffee",
    "Null",
    "Kettle",
    "Chopping food",
    "Conversation",
    "Eating popcorn",
    "Microwave door opened",
    "Microwave door closed",
    "Cupboard door opened",
    "Cupboard door closed",
    "Microwave button press",
    "Taking ice",
    "Knocking",
    "Phone vibrating",
    "Vacuum cleaning",
    "Blender running",
    "Alarm",
    "Soap dispensed",
    "Microwave done chime"
]

configuration = tflscripts.read_configuration()
activities_i = [configuration['activities'].index(a) for a in activities]

tflscripts.set_dataset_folder('/home/giotto/transfer-learning-playground/datasets/')


pipelines = []

features_to_use = [
    '.*',
    'MICROPHONE_fft',
    'microphone',
    'ACCEL_fft',
    'accel_|ACCEL_sst',
    'temperature|pressure|humidity',
    'EMI',
    'IRMOTION',
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


def devices_in_dataset(dataset):
    devices = configuration['device_roles'][dataset]
    devices = [d for d in devices if devices[d].split(' ')[0] in device_types]
    return devices


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


def test_for_source(source_dataset, source_device):
    test_set = tflscripts.TestSet(name='_'.join([source_dataset,
                                                 source_device]))

    df_source, df_source_labels = read_dataset(dataset=source_dataset,
                                               device=source_device)

    for label in df_source_labels.label.unique():
        for features in features_to_use:
            x_train = df_source.filter(regex=features)
            y_train = tflscripts.get_y_for_label(df_source_labels, label)

            for classifier in classifiers:
                print(source_dataset, source_device, classifier, features, label)

                # test on the same domain
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
                    test_set.add_result(result)
                else:
                    print('Couldnt split so that label is both in train and test set')

                ppl = fit_pipeline(classifier, x_train, y_train)

                # test with transfer
                for target_dataset in datasets:
                    for target_device in devices_in_dataset(target_dataset):
                        if source_dataset == target_dataset and source_device == target_device:
                            continue

                        print('   ', target_dataset, target_device)

                        df_target, df_target_labels = read_dataset(dataset=target_dataset,
                                                                   device=target_device)

                        if label not in df_target_labels['label'].values:
                            print('Label not in target')
                            continue

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

                        test_set.add_result(result)
