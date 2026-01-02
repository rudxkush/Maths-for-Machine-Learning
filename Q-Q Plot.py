# Quantile-Quantile plot (Q-Q)
import numpy as np
import pylab
import scipy.stats as stats

# N(0, 1)
std_normal_disb = np.random.normal(loc = 0, scale = 1, size = 1000)
# This is how we generate random samples/observations from Guassian distribution

# 0 to 100th percentiles of std-normal-disb
# percentile = (number of value below x / total count of values ) * 100
for i in range(0, 101):
    print(i, np.percentile(std_normal_disb, i))


# Generate 100 samples from N(20, 5)
measurements = np.random.normal(loc = 20, scale = 5, size = 100000)
# In order to make Q-Q plot work, we shall always take a bigger sample size
# so that the points drawn drops closure to the straight line

stats.probplot(measurements, dist="norm", plot=pylab)
pylab.show()


# Generate 100 samples from N(20, 5)
measurements = np.random.uniform(low = -1, high = 1, size = 100)

stats.probplot(measurements, dist="norm", plot=pylab)
pylab.show()
