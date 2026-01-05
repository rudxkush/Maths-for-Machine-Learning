import numpy
from pandas import read_csv
from sklearn.utils import resample
from sklearn.metrics import accuracy_score
from matplotlib import pyplot

# Load Dataset
x = numpy.array([180, 162, 158, 172, 168, 150, 171, 183, 165, 176])

# Configure Bootstrap
n_iterations = 1000
n_size = int(len(x))

# Run Bootstrap
median = list()
for i in range(n_iterations):
    # Prepare Train and Test sets
    s = resample(x, n_samples = n_size) # As our n_size is small, we let samples size to be equivalent of the dataset size
    m = numpy.median(s)
    # print(m)
    median.append(m)

# Plot Scores
pyplot.hist(median)
pyplot.show()

# Confidence Intervals
alpha = 0.95
p = ((1 - alpha)/2.0) * 100
lower = numpy.percentile(median, p)

p = (alpha + (1 - alpha)/2.0) * 100
upper = numpy.percentile(median, p)

print('%.1f Confidence Interval %.1f and %.1f' % (alpha * 100, lower, upper))
