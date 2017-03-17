import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class ImputeInf(BaseEstimator, TransformerMixin):
    def fit(self, X, y):
        return self

    def transform(self, X):
        X[X == np.inf] = 0.0
        return X
