from multipledispatch import dispatch
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import matrix_normal, invwishart, invgamma, special_ortho_group
from scipy.stats import bernoulli
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

def Ber(N=100, T=30, p=0.2):
  """ Bernoulli random matrix, N is population size, T is number of tests, p is
  infection probability. Every person has a probability p of being included in a test"""
  r = bernoulli.rvs(p, size=int(N*T))
  r = np.reshape(r, (N, T))
  return r

def CCW(N=100, T=30, L=None, p=0.2):
  """ Constant column weight random matrix. N: population size, T: number of tests,
  p: probability of element being included in test. For each element, assign it
  to any test with a probability p with replacement. Independently within each
  column of X, L random entries are selected uniformly at random with replacement
  and set to 1. So, each person is put into L tests. So roughly, p=L/T. TESTED."""
  X = np.zeros(shape=(N, T))
  if L is None:
    L = int(p * T)
  # Sample indices between 0 and T-1 with replacement, of size L. Set those
  # indices in each row of X to 1.
  for i in range(N):
    X[i][np.random.choice(T, size=L, replace=True)] = 1
  return X
