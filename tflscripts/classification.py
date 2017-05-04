import json
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn import tree
from sklearn.linear_model import LogisticRegression

from .impute_inf import ImputeInf


def classifier_by_name(clf_name):
    if clf_name == 'RandomForestClassifier':
        clf = RandomForestClassifier()
    elif clf_name == 'SVC':
        clf = svm.SVC(kernel='linear', decision_function_shape='ovr')
    elif clf_name == 'LinearSVC':
        clf = svm.LinearSVC()
    elif clf_name == 'GaussianNB':
        clf = GaussianNB()
    elif clf_name == 'BernoulliNB':
        clf = BernoulliNB()
    elif clf_name == 'DecisionTreeClassifier':
        clf = tree.DecisionTreeClassifier()
    elif clf_name == 'LogisticRegression':
        clf = LogisticRegression()

    return clf


def fit_pipeline(X_train, y_train, clf_name, scale=False):
    clf = classifier_by_name(clf_name)

    if scale:
        ppl = Pipeline([
            ('impute', Imputer()),
            ('imput_inf', ImputeInf()),
            ('scale', StandardScaler()),
            ('clf', clf)
        ])
    else:
        ppl = Pipeline([
            ('impute', Imputer()),
            ('imput_inf', ImputeInf()),
            ('clf', clf)
        ])

    ppl.fit(X_train, y_train)
    return ppl


def classify(X_train, y_train, X_test, clf_name='RandomForestClassifier',
             scale=False):
    ppl = fit_pipeline(X_train, y_train, clf_name, scale)
    y_pred = ppl.predict(X_test)

    return y_pred


def log_of_classification_results(y_test, y_pred):
    f1 = [i.tolist() for i in precision_recall_fscore_support(y_test, y_pred)]
    matrix = confusion_matrix(y_test, y_pred).tolist()
    return [accuracy_score(y_test, y_pred), json.dumps(f1), json.dumps(matrix)]