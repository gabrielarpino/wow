from multipledispatch import dispatch
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import matrix_normal, invwishart, invgamma, special_ortho_group
import pandas as pd
from .colour import PAL, gen_PAL
sns.set()
a = (list, np.ndarray)

@dispatch(np.ndarray)
def viz(x):
    """ Visualize matrices. Next step: visualize them randomly,
    sometimes to PCA sometimes do heatmap etc """
    sns.set()
    pal = gen_PAL()
    if x.ndim == 1: # It is a vector
        plt.scatter(np.linspace(0, 1, x.shape[0]), x)
    elif x.ndim == 2: # Matrix
        # Draw a heatmap with the numeric values in each cell
        f, ax = plt.subplots(figsize=(9, 6))
        sns.heatmap(x, cmap=pal, fmt="d", linewidths=.5, ax=ax)
    plt.show()
    return

@dispatch() # Empty input, let's try
def viz():
    return viz(GOE())

def GOE(dim=(100, 100)): # Samples from a gaussian orthogonal ensemble
    m = matrix_normal.rvs(mean=np.zeros(dim))
    return (m + m.T) / np.sqrt(2)
