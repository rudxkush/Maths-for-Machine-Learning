import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

# Generate a Gaussian Random Variable x
x = stats.norm.rvs(size = 1000)
sns.set_style('whitegrid')
sns.kdeplot(np.array(x), bw = 0.5)
plt.show()

print(stats.kstest(x, 'norm'))

# y ~ Continuous Uniform Distribution(0, 1)
y = np.random.uniform(0, 1, 10000);
sns.kdeplot(np.array(y), bw = 0.1)
plt.show()

print(stats.kstest(y, 'norm'))

