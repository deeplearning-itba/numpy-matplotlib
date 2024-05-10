import numpy as np
from matplotlib import pyplot as plt



def plot_problem(N, bins=20, plot_hist=False):
    """

    """
    x = 2 * np.random.random(N) - 1
    y = 2 * np.random.random(N) - 1
    in_circle_indexes = (x**2 + y**2) <= 1
    if plot_hist:
        fig, ax = plt.subplots(2, 1)
        ax[0].hist(x, bins=bins)
        ax[1].hist(y, bins=bins)

    fig, ax = plt.subplots(figsize=(10,10))
    circle = plt.Circle((0, 0), 1, fill=False)
    ax.scatter(x[in_circle_indexes], y[in_circle_indexes], c='r', s=10)
    ax.scatter(x[~in_circle_indexes], y[~in_circle_indexes], c='b', s=10)
    ax.add_patch(circle)
    

def estimate_pi(N):
    x = 2 * np.random.random(N) - 1
    y = 2 * np.random.random(N) - 1
    in_circle_indexes = (x**2 + y**2) <= 1
    total_in_circle_points = in_circle_indexes.sum()
    estimated_pi = 4 * total_in_circle_points/N
    return total_in_circle_points, estimated_pi