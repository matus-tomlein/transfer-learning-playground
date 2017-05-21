import math
import numpy as np
import pandas as pd


def derivative(row):
    der = []
    for i in range(len(row) - 1):
        der.append(row[i + 1] - row[i])
    return der


def RMS(row):
    squares = [i * i for i in row]
    return [math.sqrt(sum(squares) / len(row))]


def mean(row):
    return [np.mean(row)]


def std(row):
    return [np.std(row)]


def max_index(row):
    return [np.argmax(row)]


def min_index(row):
    return [np.argmin(row)]


def down_sample(row, down_sample_size=16):
    # only take length that is divisible by the sample size
    l = len(row) - (len(row) % down_sample_size)
    row = row[:l]

    bin_size = int(len(row) / down_sample_size)
    bins = []
    for i in range(down_sample_size):
        since = i * bin_size
        until = since + bin_size
        bins.append(np.mean(row[since:until]))

    return bins


def band_ratios(signal):
    ratios = []
    for i in range(len(signal)):
        for j in range(len(signal)):
            ratios.append(signal[i] / (0.0001 + signal[j]))
    return ratios


def features_from_fft(fft_df):
    df_values = fft_df.values
    return np.concatenate([
        [derivative(row) for row in df_values],
        [RMS(row) for row in df_values],
        [mean(row) for row in df_values],
        [std(row) for row in df_values],
        [max_index(row) for row in df_values],
        [band_ratios(down_sample(row)) for row in df_values]
        ], axis=1)


def add_fft_features_for(df, sensor_stream):
    values_df = df.filter(regex=sensor_stream)

    features = pd.DataFrame(features_from_fft(values_df))
    features.columns = [sensor_stream + str(col) for col in features.columns]

    return pd.concat([df, features], axis=1, ignore_index=True)
