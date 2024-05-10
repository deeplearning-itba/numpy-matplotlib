# %%
%load_ext autoreload
%autoreload 2
# %%
from montecarlo_utils import estimate_pi, plot_problem
# %%

# %%
_, pi_estimated = estimate_pi(1_000_000)

pi_estimated

# %%
fig = plot_problem(100, plot_hist=True)
# %%
fig.savefig('hist.png')
# %%
import seaborn as sns
# %%
import numpy as np
N = 10_000
x = 2 * np.random.random(N) - 1
y = 2 * np.random.random(N) - 1
# %%
sns.kdeplot(x=x, y=y)
# %%
sns.displot(x=x, y=y)
# %%
