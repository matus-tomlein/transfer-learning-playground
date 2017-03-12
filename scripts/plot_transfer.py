#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

devices = ['Sink', 'Corner', 'Coffee', 'Table']
features = ['Accelerometer', 'Microphone', 'Magnetometer']
classifiers = ['Random Forest', 'SVM', 'Decision Tree', 'Gaussian Naive Bayes']

df = pd.DataFrame.from_csv('results_transfer.csv', index_col=None)

df['source_name'] = [devices[i] for i in df['source']]
df['target_name'] = [devices[i] for i in df['target']]
df['clf_name'] = [classifiers[i] for i in df['clf']]
df['feature_name'] = [features[i] for i in df['feature']]

df['group'] = df['source_name'] + ' > ' + df['target_name']
df['graph'] = df['clf_name'] + ' – ' + df['feature_name']

for graph in df.graph.unique():
    sub_df = df[df['graph'] == graph]
    ax = sub_df.boxplot('accuracy', by='group', rot=30)
    ax.set_ylim(0, 1)
    plt.title(graph)
    plt.suptitle('')
    plt.savefig('plots/' + graph + '.png', dpi=300)

# plt.show()
