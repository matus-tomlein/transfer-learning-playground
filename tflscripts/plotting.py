import numpy as np
import itertools
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def scatter_plot_by(column, df_plot, other_column=None, label='Microwave', features='Microphone', classifier='LogisticRegression',
                    use_markers={}, use_colors={},
                    ax=None, show_legend=True, title=None,
                    x_value_column='f1_change', y_value_column='f1_wt',
                    xlabel=None, ylabel=None,
                    min_val=None, max_val=None,
                    size=200,
                    common_limits=True):

    if label is not None:
        df_plot = df_plot.loc[df_plot.label == label]
    if features is not None:
        df_plot = df_plot.loc[df_plot.features_name == features]
    if classifier is not None:
        df_plot = df_plot.loc[df_plot.classifier == classifier]

    if ax is None:
        fig, ax = plt.subplots()
    else:
        ax = ax

    colors = itertools.cycle(matplotlib.cm.rainbow(np.linspace(0, 1, len(df_plot[column].drop_duplicates()))))

    for value in df_plot[column].drop_duplicates():
        if value in use_colors:
            color = use_colors[value]
        else:
            color = next(colors)
            use_colors[value] = color

        subdf_plot = df_plot.loc[df_plot[column] == value]
        if other_column is None:
            if len(subdf_plot) > 0:
                ax.scatter(subdf_plot[x_value_column],
                        subdf_plot[y_value_column], s=size,
                        edgecolor='black',
                        label=value, color=color)

        else:
            markers = itertools.cycle(['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd'])
            for other_value in df_plot[other_column].drop_duplicates():
                ssubdf_plot = subdf_plot.loc[df_plot[other_column] == other_value]
                if other_value in use_markers:
                    marker = use_markers[other_value]
                else:
                    marker = next(markers)
                    use_markers[other_value] = marker

                if len(ssubdf_plot) > 0:
                    ax.scatter(ssubdf_plot[x_value_column],
                            ssubdf_plot[y_value_column],
                            label=value + ', ' + other_value,
                            edgecolor='black',
                            s=size,
                            color=color, marker=marker)

    if show_legend:
        ax.legend()

    if min_val is None:
        min_val = min(df_plot[x_value_column].min(), df_plot[y_value_column].min()) - 0.02
    if max_val is None:
        max_val = max(df_plot[x_value_column].max(), df_plot[y_value_column].max()) + 0.02

    matplotlib.pyplot.sca(ax)

    if common_limits:
        ax.set_ylim(min_val, max_val)
        ax.set_xlim(min_val, max_val)
        plt.plot([min_val, max_val], [min_val, max_val], zorder=-10)

    if title is None:
        plt.title(column)
    else:
        plt.title(title)

    plt.xlabel(x_value_column if xlabel is None else xlabel)
    plt.ylabel(y_value_column if ylabel is None else ylabel)

    return use_colors, use_markers, df_plot


def boxplot_by(column, df_plot, label='Microwave',
               features='Microphone', classifier='LogisticRegression',
               value_column='recall_change', ax=None, title=None):
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
    newdf.plot.box(ax=ax)

    if ax is not None:
        matplotlib.pyplot.sca(ax)

    if title is None:
        plt.title(column)
    else:
        plt.title(title)

    plt.xticks(rotation='vertical')


def heatmap_by(x_column, y_column, value_column, df_plot,
               label=None, features='Microphone', classifier='LogisticRegression',
               draw_cbar=True, cbar_ax=None,
               vmin=None, vmax=None,
               ax=None, title=None, cmap='gray'):

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
    sns.heatmap(df_plot,
            cbar=draw_cbar,
            cbar_ax=cbar_ax,
            vmin=vmin,
            vmax=vmax,
            annot=True,
            cmap=cmap,
            ax=ax)

    if ax is not None:
        matplotlib.pyplot.sca(ax)

    if title is None:
        plt.title(', '.join(title_parts))
    else:
        plt.title(title)


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
