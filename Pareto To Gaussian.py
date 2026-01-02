# We apply a Box–Cox transformation to a Pareto-distributed random variable
# to make it more Gaussian-like (reduce skewness and stabilize variance).
from numpy.ma.core import size
# We use scipy.stats.boxcox
# Input:
#   x      : 1D array of strictly positive values (e.g., Pareto samples)
#   lmbda  : optional transformation parameter; if None, it is estimated via MLE
#   alpha  : optional, used only for confidence intervals

# Output:
#   Transformed array (Box–Cox transformed values)
#   Optionally, the estimated lambda if lmbda=None


from scipy import stats
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(211)
x = stats.loggamma.rvs(5, size=500) + 5 # One of the power law distribution
prob = stats.probplot(x, dist=stats.norm, plot=ax1)
ax1.set_xlabel('')
ax1.set_title('Probplot against normal distribution')

ax2 = fig.add_subplot(212)
xt, _ = stats.boxcox(x)
prob = stats.probplot(xt, dist=stats.norm, plot=ax2)
ax2.set_title('Probplot after Box-Cox transformation')

plt.show()
