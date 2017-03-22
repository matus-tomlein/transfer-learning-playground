#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import os
from ml.plotting import boxplots
import json

dataset = 'synergy-mites-colocated'

csv_file = '/'.join([
    dataset,
    'results',
    'results_no_transfer.csv'
])

output_folder = dataset + '/plots/new/'

with open('configuration.json') as f:
    configuration = json.load(f)

df = pd.DataFrame.from_csv(csv_file, index_col=None)

devices = configuration['devices']
classifiers = configuration['classifier_names']
features = configuration['feature_names']
device_roles = configuration['device_roles'][dataset]

if 'source' in df:
    df['source_name'] = [device_roles[devices[i]] for i in df['source']]
    df['target_name'] = [device_roles[devices[i]] for i in df['target']]
    df['Devices'] = df['source_name'] + ' > ' + df['target_name']


def names_for_sources(sources):
    source_names = [device_roles[devices[int(i)]] for i in sources.split('_')]
    return ', '.join(source_names)


if 'sources' in df:
    df['source_name'] = [names_for_sources(i) for i in df['sources']]
    df['target_name'] = [device_roles[devices[i]] for i in df['target']]
    df['Devices'] = df['source_name'] + ' > ' + df['target_name']

if 'device' in df:
    df['Devices'] = [device_roles[devices[i]] for i in df['device']]

df['Classifier'] = [classifiers[i] for i in df['clf']]
df['Features'] = [features[i] for i in df['feature']]

df['Classifier and features'] = df['Classifier'] + ' – ' + df['Features']

os.makedirs(output_folder + 'all')
os.makedirs(output_folder + 'by_classifiers')

boxplots(df,
         group_column='Devices',
         graph_column='Classifier and features',
         output_folder=output_folder + 'all/')

boxplots(df,
         group_column='Features',
         graph_column='Classifier',
         output_folder=output_folder + 'by_classifiers/')
