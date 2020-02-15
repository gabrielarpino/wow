import wow
from wow import *
import matplotlib.pyplot as plt
import numpy as np
from wow.viz import *

import stheno
from stheno import GP, EQ, Delta, model

# Define points to predict at.
x = np.linspace(0, 10, 100)
x_obs = np.linspace(0, 7, 20)

# Construct a prior.
f = GP(EQ().periodic(5.))  # Latent function.
e = GP(Delta())  # Noise.
y = f + .5 * e

# Sample a true, underlying function and observations.
f_true, y_obs = model.sample(f(x), y(x_obs))
post = (f | (y(x_obs), y_obs))

viz(x_obs, y_obs, post)

# # Now condition on the observations to make predictions.
# mean, lower, upper = (f | (y(x_obs), y_obs))(x).marginals()
#
# # Plot result.
# plt.plot(x, f_true, label='True', c=PAL[0])
# plt.scatter(x_obs, y_obs, label='Observations', c=PAL[1])
# plt.plot(x, mean, label='Prediction', c=PAL[2])
# plt.plot(x, lower, ls='--', c=PAL[2])
# plt.plot(x, upper, ls='--', c=PAL[2])
# plt.show()
