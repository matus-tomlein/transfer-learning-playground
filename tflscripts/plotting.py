import numpy as np
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def scatter_plot_by(column, df_plot, label='Microwave', features='Microphone', classifier='LogisticRegression',
            x_value_column='accuracy_negative', y_value_column='accuracy_negative_wt',
            common_limits=True):

    if label is not None:
        df_plot = df_plot.loc[df_plot.label == label]
    df_plot = df_plot.loc[df_plot.features_name == features]
    df_plot = df_plot.loc[df_plot.classifier == classifier]

    fig, ax = plt.subplots()

    for value in df_plot[column].drop_duplicates():
        subdf_plot = df_plot.loc[df_plot[column] == value]
        if len(subdf_plot) > 0:
            ax.scatter(subdf_plot[x_value_column], subdf_plot[y_value_column], label=value)
    ax.legend()

    min_val = min(df_plot[x_value_column].min(), df_plot[y_value_column].min()) - 0.02
    max_val = max(df_plot[x_value_column].max(), df_plot[y_value_column].max()) + 0.02

    if common_limits:
        ax.set_ylim(min_val, max_val)
        ax.set_xlim(min_val, max_val)

    plt.title(column)
    plt.xlabel(x_value_column)
    plt.ylabel(y_value_column)
    plt.show()


def boxplot_by(column, df_plot, label='Microwave', features='Microphone', classifier='LogisticRegression',
            value_column='accuracy_positive_change'):
    df_plot = df_plot.sort_values(by=column)

    if label is not None:
        df_plot = df_plot.loc[df_plot.label == label]
    df_plot = df_plot.loc[df_plot.features_name == features]
    df_plot = df_plot.loc[df_plot.classifier == classifier]

    newdf = pd.DataFrame()

    for device in df_plot[column].unique():
        subdf = df_plot.loc[df_plot[column] == device]
        series = subdf[value_column].reset_index(drop=True)
        newdf = pd.concat([pd.DataFrame({device: series}), newdf], axis=1)

    newdf = newdf.sort_index(axis=1)
    newdf.plot.box()
    plt.title(column)
    plt.xticks(rotation='vertical')
    plt.show()


def heatmap_by(x_column, y_column, value_column, df_plot,
               label=None, features='Microphone', classifier='LogisticRegression',
              cmap='gray'):

    title_parts = []

    if label is not None:
        df_plot = df_plot.loc[df_plot.label == label]
        title_parts.append(label)
    if features is not None:
        df_plot = df_plot.loc[df_plot.features_name == features]
        title_parts.append(features)
    if classifier is not None:
        df_plot = df_plot.loc[df_plot.classifier == classifier]
        title_parts.append(classifier)

    df_plot = df_plot.groupby([x_column, y_column])[value_column].mean()
    df_plot = df_plot.reset_index()
    df_plot = df_plot.pivot(index=y_column, columns=x_column, values=value_column)
    sns.heatmap(df_plot, annot=True, cmap=cmap)
    plt.title(', '.join(title_parts))
    plt.show()


def confusion_matrices(df, dataset, configuration, graph_column, output_folder):
    df.sort_values(by=graph_column)

    # find column with the larget number as name
    last_column = 0
    for column in df.columns:
        if column.isdigit():
            if last_column < int(column):
                last_column = int(column)

    activities = configuration['activities'][dataset]

    starting_column = last_column - (len(activities) * len(activities))
    # columns = [str(i) for i in range(starting_column, last_column + 1)]

    for graph in df[graph_column].unique():
        sub_df = df.loc[df[graph_column] == graph]

        cm = []
        for i in range(len(activities)):
            values = []
            for n in range(len(activities)):
                k = (n + 1) + len(activities) * (i)
                column = str(starting_column + k)
                value = sub_df[column].sum()
                values.append(value)

            cm.append(values)

        cm = np.array(cm)
        plt.figure()
        plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        plt.title(graph)
        plt.colorbar()
        tick_marks = np.arange(len(activities))
        plt.xticks(tick_marks, activities, rotation=45)
        plt.yticks(tick_marks, activities)

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True activity')
        plt.xlabel('Predicted activity')
        plt.savefig(output_folder + graph + '.png', dpi=300)
