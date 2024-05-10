# %%
import seaborn as sns
import numpy as np
# %%
N = 10_000
x_gauss = np.random.normal(0, 1, N)
y_gauss = np.random.normal(0, 10, N)
# %%
sns.kdeplot(x_gauss)
# %%
from matplotlib import pyplot as plt
f = plt.figure(figsize=(5,10))
sns.kdeplot(x=x_gauss, y=y_gauss)
# %%
sns.displot(x=x_gauss, y=y_gauss)
# %%
N = 10000
mu_alt = 170
std_alt = 10
alturas_h = np.random.normal(mu_alt, std_alt, N)
# %%
peso_h = np.random.normal(80, 10, N)
# %%
peso_h = 80*alturas_h/170 + np.random.normal(0, 5, N)
# %%
# %%
sns.kdeplot(x=alturas_h, y=peso_h)
# %%
np.random.multivariate_normal()
# %%
alturas_h.mean()
# %%
peso_h.mean()
# %%
concatenated_data = np.array([alturas_h, peso_h])
# %%
np.corrcoef(concatenated_data)
# %%
concatenated_data
# %%
