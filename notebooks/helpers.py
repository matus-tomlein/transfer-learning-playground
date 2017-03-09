import numpy as np
import pandas as pd
from tsfresh.transformers import RelevantFeatureAugmenter, FeatureAugmenter
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

def train_test_split_labels(df_labels):
    indexes = df_labels.index.tolist()
    np.random.shuffle(indexes)
    split = round(0.7*len(indexes))
    training_i = indexes[:split]
    testing_i = indexes[split:]

    y_train = df_labels.loc[df_labels.index.isin(training_i)]
    y_test = df_labels.loc[df_labels.index.isin(testing_i)]

    y_train = y_train['label']
    y_test = y_test['label']
    
    return y_train, y_test

# training and testing split
def train_test_split(df, df_labels):
    indexes = df_labels.index.tolist()
    np.random.shuffle(indexes)
    split = round(0.7*len(indexes))
    training_i = indexes[:split]
    testing_i = indexes[split:]
    df_train = df.loc[df.id.isin(training_i)]
    df_test = df.loc[df.id.isin(testing_i)]

    y_train = df_labels.loc[df_labels.index.isin(training_i)]
    y_test = df_labels.loc[df_labels.index.isin(testing_i)]

    y_train = y_train['label']
    y_test = y_test['label']

    X_train = pd.DataFrame(index=y_train.index)
    X_test = pd.DataFrame(index=y_test.index)
    
    return df_train, X_train, y_train, df_test, X_test, y_test

def classify_with_tsfresh_features(df_train, X_train, y_train, df_test, X_test, y_test, extraction_settings=None):
    ppl = Pipeline([
        ('fresh', RelevantFeatureAugmenter(column_id='id', feature_selection_settings=extraction_settings)),
        ('impute', Imputer()),
        ('scale', StandardScaler()),
        ('clf', RandomForestClassifier())
    ])

    ppl.set_params(fresh__timeseries_container=df_train)
    ppl.fit(X_train, y_train)

    ppl.set_params(fresh__timeseries_container=df_test)
    y_pred = ppl.predict(X_test)

    return classification_report(y_test, y_pred)