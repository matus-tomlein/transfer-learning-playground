from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

from ml.impute_inf import ImputeInf


def classifier_by_name(clf_name):
    if clf_name == 'RandomForestClassifier':
        clf = RandomForestClassifier()
    elif clf_name == 'SVC':
        clf = svm.SVC()
    elif clf_name == 'GaussianNB':
        clf = GaussianNB()
    elif clf_name == 'DecisionTreeClassifier':
        clf = tree.DecisionTreeClassifier()

    return clf


def fit_pipeline(X_train, y_train, clf_name):
    clf = classifier_by_name(clf_name)

    ppl = Pipeline([
        ('impute', Imputer()),
        ('imput_inf', ImputeInf()),
        ('scale', StandardScaler()),
        ('clf', clf)
    ])

    ppl.fit(X_train, y_train)
    return ppl


def classify(X_train, y_train, X_test, clf_name='RandomForestClassifier'):
    ppl = fit_pipeline(X_train, y_train, clf_name)
    y_pred = ppl.predict(X_test)

    return y_pred


def log_of_classification_results(y_test, y_pred):
    results = [accuracy_score(y_test, y_pred)]
    f1 = precision_recall_fscore_support(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    results += [item for sublist in f1 for item in sublist]
    results += [item for sublist in matrix for item in sublist]

    return results
