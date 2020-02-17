from multipledispatch import dispatch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from .colour import PAL
a = (list, np.ndarray)

@dispatch(np.ndarray, function)
def viz(x, f):
    # Now condition on the observations to make predictions.
    plt.plot(x, f(x), c=PAL[0])
    plt.show()
    return
