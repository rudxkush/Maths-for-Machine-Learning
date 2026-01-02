# picks any values in the range [0 1]
import random
print(random.random())

# Loading IRIS Dataset with 150 points
from sklearn import datasets
iris = datasets.load_iris()
d = iris.data
print(d.shape)

# Sample 30 points randomly from the 150 point datasets
n = 150;
m = 30;
p = m / n; # 0.2 -> 20 percent
sampled_data = [];
# Any point in 150 point datasets should have an equal chance of belonging to the 30 point datasets

for i in range(0, n):
    if random.random() <= p:            # Each of the 150 points does have an equal probability (0.2) of being selected
        sampled_data.append(d[i, :])    # There is no bias toward any specific point
                                        # This is a valid Bernoulli / independent sampling scheme.

print(len(sampled_data))                # Needn't always be 30




