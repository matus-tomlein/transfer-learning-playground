#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
from ml.plotting import boxplots
import json

dataset = 'synergy-mites-kitchen'

csv_file = '/'.join([
    dataset,
    'results',
    'results_transfer_with_labeled_target_data.csv'
])

output_folder = dataset + '/plots/new/'

with open('configuration.json') as f:
    configuration = json.load(f)

df = pd.DataFrame.from_csv(csv_file, index_col=None)

devices = configuration['devices']
classifiers = configuration['classifier_names']
features = configuration['feature_names']
device_roles = configuration['device_roles'][dataset]

df['source_name'] = [device_roles[devices[i]] for i in df['source']]
df['target_name'] = [device_roles[devices[i]] for i in df['target']]
df['clf_name'] = [classifiers[i] for i in df['clf']]
df['feature_name'] = [features[i] for i in df['feature']]

df['Percentage of target data'] = 100 * df['target_training_data']
df['graph'] = df['source_name'] + ' > ' + df['target_name'] + \
    ' – ' + df['clf_name'] + ': ' + df['feature_name']

boxplots(df, 'Percentage of target data', output_folder)
