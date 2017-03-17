#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import matplotlib.pyplot as plt
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

df['device_name'] = [device_roles[devices[i]] for i in df['device']]
df['clf_name'] = [classifiers[i] for i in df['clf']]
df['feature_name'] = [features[i] for i in df['feature']]

df['group'] = df['device_name']
df['graph'] = df['clf_name'] + ' – ' + df['feature_name']

df.sort_values(by='group')

for graph in df.graph.unique():
    sub_df = df[df['graph'] == graph]
    ax = sub_df.boxplot('accuracy', by='group', rot=90)
    ax.set_ylim(0, 1)
    plt.title(graph)
    plt.suptitle('')
    plt.tight_layout()
    plt.savefig(output_folder + graph + '.png', dpi=300)

# plt.show()
