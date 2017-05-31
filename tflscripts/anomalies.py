import pandas as pd
import numpy as np

HIGH_SAMPLING_EUCLIDEAN_DISTANCE_THRESHOLD = 300.0
HIGH_SAMPLING_EUCLIDEAN_DISTANCE_HYSTERESIS_THRESHOLD = 250.0

LOW_SAMPLING_ZSCORE_THRESHOLD = 3.5
LOW_SAMPLING_ZSCORE_HYSTERESIS_THRESHOLD = 3.0

SENSOR_BUFFER_HISTORY_SIZE = 5
BG_BUFFER_HISTORY_LENGTH = 100

# [min, max, stdev]
LOW_SAMPLING_RANGES = {
    'ACCEL': [0.0, 0.0, 0.001],
    'MICROPHONE': [0.0, 0.0, 0.001],
    'EMI': [0.0, 0.0, 0.001],
    'TEMPERATURE': [0.0, 120.0, 1.5],
    'BAROMETER': [870.0, 1013.0, 1.2],
    'HUMIDITY': [0.0, 100.0, 10.0],
    'ILLUMINATION': [0.0, 4096.0, 50.0],
    'COLOR': [0.0, 255.0, 10.0],
    'MAGNETOMETER': [-30.0, 30.0, 5.0],
    'WIFI': [-70.0, 0.0, 0.2],
    'IRMOTION': [0.0, 4096.0, 30.0],
    'GEYE': [0.0, 128.0, 10.0]
}


class ChannelAnomalyComputer:

    def __init__(self, columns):
        self.columns = columns
        self.is_hysteresis = False
        self.channel = columns[0].split('_')[0]
        self.is_fft = '_fft' in columns[0]
        self.background_history = []
        self.history_size = BG_BUFFER_HISTORY_LENGTH

        if not self.is_fft:
            mean_columns = [i for i, col in enumerate(columns) if '_avg' in col]
            self.mean_column = mean_columns[0]

    def add_to_history(self, row):
        self.background_history.append(row)
        if len(self.background_history) > self.history_size:
            self.background_history.pop(0)

    def is_anomaly(self, target_history):
        dist = self.get_distance(target_history)
        threshold = self.get_threshold()
        if self.channel == 'ACCEL':
            threshold *= 0.2

        anomaly = dist > threshold
        self.is_hysteresis = anomaly
        return anomaly

    def get_threshold(self):
        if self.is_fft:
            if self.is_hysteresis:
                return HIGH_SAMPLING_EUCLIDEAN_DISTANCE_HYSTERESIS_THRESHOLD
            else:
                return HIGH_SAMPLING_EUCLIDEAN_DISTANCE_THRESHOLD
        else:
            if self.is_hysteresis:
                return LOW_SAMPLING_ZSCORE_HYSTERESIS_THRESHOLD
            else:
                return LOW_SAMPLING_ZSCORE_THRESHOLD

    def get_distance(self, target_history):
        if len(self.background_history) < self.history_size / 5:
            return 0

        if self.is_fft:
            target_mean = np.mean(target_history, axis=0)
            history_mean = np.mean(self.background_history, axis=0)
            history_stdev = np.std(self.background_history, axis=0)
            zscore = (target_mean - history_mean) / history_stdev
            dist = np.sqrt(np.nan_to_num(zscore * zscore).sum())
            return dist

        else:
            mn, mx, stdev = LOW_SAMPLING_RANGES[self.channel]
            target_mean = np.mean(target_history, axis=0)[self.mean_column]
            history_mean = np.mean(self.background_history, axis=0)[self.mean_column]
            zscore = np.abs(target_mean - history_mean) / stdev
            return np.nan_to_num(zscore)


def compute_anomalies(df, sensor_channels):
    channel_columns = [df.filter(regex=chan).columns.tolist() for chan in sensor_channels]
    channel_anomaly_computers = [ChannelAnomalyComputer(columns) for columns in channel_columns]

    anomalies = []
    history = []
    for row in df.values:
        history.append(row)
        if len(history) > SENSOR_BUFFER_HISTORY_SIZE:
            history.pop(0)

        row_anomalies = [comp.get_distance(history) for comp in channel_anomaly_computers]
        anomalies.append(row_anomalies)

        for comp in channel_anomaly_computers:
            comp.add_to_history(row)

    anomalies = pd.DataFrame(anomalies)
    anomalies.columns = sensor_channels
    anomalies.index = df.index

    return anomalies
