import numpy as np
import itertools
import matplotlib.pyplot as plt


def boxplots(df, group_column, output_folder, graph_column='graph'):
    df.sort_values(by=group_column)

    for graph in df[graph_column].unique():
        sub_df = df[df[graph_column] == graph]

        ax = sub_df.boxplot('accuracy', by=group_column, rot=90)
        ax.set_ylim(0, 1)
        plt.title(graph)
        plt.suptitle('')
        plt.tight_layout()
        plt.savefig(output_folder + graph + '.png', dpi=300)


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
