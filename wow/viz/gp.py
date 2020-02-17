from multipledispatch import dispatch
import stheno
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from .colour import PAL

# Remove stheno from this cus too many dependencies and not maintained, it depends on lab and wbml which is not easy to install.

a = (list, np.ndarray)

@dispatch(a, a, stheno.graph.GP)
def viz(x, y, p):
    # Now condition on the observations to make predictions.
    mean, lower, upper = p(x).marginals()
    # Plot result.
    plt.scatter(x, y, label='Observations', c=PAL[1])
    plt.plot(x, mean, label='Prediction', c=PAL[2])
    plt.plot(x, lower, ls='--', c=PAL[2])
    plt.plot(x, upper, ls='--', c=PAL[2])
    plt.show()
    return

@dispatch(a, stheno.graph.GP)
def viz(x, p):
    mean, lower, upper = p(x).marginals()
    plt.plot(x, mean, label='Prediction', c=PAL[2])
    plt.plot(x, lower, ls='--', c=PAL[2])
    plt.plot(x, upper, ls='--', c=PAL[2])
    plt.show()
    return
