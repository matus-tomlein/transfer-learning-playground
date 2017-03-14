#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import matplotlib.pyplot as plt

devices = ['Sink', 'Corner', 'Coffee', 'Table']
features = ['Accelerometer', 'Microphone', 'Magnetometer']
classifiers = ['Random Forest', 'SVM', 'Decision Tree', 'Gaussian Naive Bayes']

df = pd.DataFrame.from_csv('results_no_transfer.csv', index_col=None)

df['device_name'] = [devices[i] for i in df['device']]
df['clf_name'] = [classifiers[i] for i in df['clf']]
df['feature_name'] = [features[i] for i in df['feature']]

df['group'] = df['device_name']
df['graph'] = df['clf_name'] + ' – ' + df['feature_name']

for graph in df.graph.unique():
    sub_df = df[df['graph'] == graph]
    ax = sub_df.boxplot('accuracy', by='group', rot=30)
    ax.set_ylim(0, 1)
    plt.title(graph)
    plt.suptitle('')
    plt.savefig('plots/' + graph + '.png', dpi=300)

# plt.show()
