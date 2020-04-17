from multipledispatch import dispatch
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from .colour import PAL, gen_PAL
sns.set()

# Remove stheno from this temporarily cus too many dependencies and not maintained, it depends on lab and wbml which is not easy to install.
a = (list, np.ndarray)

@dispatch(np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray)
def viz(x, y, mean, lower, upper):
    pal = gen_PAL()
    plt.figure(figsize=(12, 6))
    plt.scatter(x[:, 0], y, label='Observations', c=pal[0], alpha=0.8)
    plt.plot(x[:, 0], mean, label='Prediction', c=pal[1])
    plt.fill_between(x[:, 0], lower, upper, color=pal[2], alpha=0.3)
    plt.legend()
    plt.show()
    return

# @dispatch(a, a, stheno.graph.GP)
# def viz(x, y, p):
#     # Now condition on the observations to make predictions.
#     mean, lower, upper = p(x).marginals()
#     # Plot result.
#     plt.scatter(x, y, label='Observations', c=PAL[1])
#     plt.plot(x, mean, label='Prediction', c=PAL[2])
#     plt.plot(x, lower, ls='--', c=PAL[2])
#     plt.plot(x, upper, ls='--', c=PAL[2])
#     plt.show()
#     return

# @dispatch(a, stheno.graph.GP)
# def viz(x, p):
#     mean, lower, upper = p(x).marginals()
#     plt.plot(x, mean, label='Prediction', c=PAL[2])
#     plt.plot(x, lower, ls='--', c=PAL[2])
#     plt.plot(x, upper, ls='--', c=PAL[2])
#     plt.show()
#     return
