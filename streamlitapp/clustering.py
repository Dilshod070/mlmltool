import streamlit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering


def get_random_color():
    channels = [np.random.randint(16, 255) for _ in range(3)]
    return "#{:x}{:x}{:x}".format(*channels)


@streamlit.cache(ttl=300)
def generate_distribution(n_points):
    return np.random.randn(n_points, 2)


def transform_points(points, p=2):
    center = points.mean(axis=0)
    centred_points = points - center.reshape(1, -1)
    dists_to_center = np.sqrt((centred_points ** 2).sum(axis=1))
    transformed_dists_to_center = np.power(dists_to_center, 1/p)
    transformed_points = centred_points * (transformed_dists_to_center / dists_to_center).reshape(-1, 1)
    return transformed_points


def cluster_split(points, n_clusters=2):
    model = AgglomerativeClustering(n_clusters=n_clusters, linkage='complete')
    labels = model.fit_predict(points)
    return labels


def show_points(ax, points, labels, title='', colors=None):
    df = pd.DataFrame(data=points)
    df['labels'] = labels

    n_clusters = len(set(df['labels']))
    for i, (label, gdf) in enumerate(df.groupby(by='labels')):
        color = get_random_color()
        if colors and len(colors) == n_clusters:
            color = colors[i]
        ax.scatter(gdf[0], gdf[1], label=label, c=color, marker='.')
    ax.set_title(title)


def main():
    n_points = streamlit.sidebar.slider(label='#Points', min_value=50, max_value=5000)
    n_clusters_percent = streamlit.sidebar.slider(label='#Clusters (% of points)', min_value=0.01, max_value=20.0)
    n_clusters = max(1, int(np.round(n_clusters_percent * n_points / 100)))
    transform_param = streamlit.sidebar.slider(label='#Tranformation Param', min_value=0.0, max_value=5.0, value=1.0)

    points = generate_distribution(n_points=n_points)
    transformed_points = transform_points(points, p=transform_param)

    labels = cluster_split(transformed_points, n_clusters=n_clusters)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))
    colors = [get_random_color() for _ in range(n_clusters)]
    show_points(ax1, transformed_points, labels, colors=colors)
    show_points(ax2, points, labels, colors=colors)
    streamlit.pyplot(fig)


if __name__ == '__main__':
    main()
