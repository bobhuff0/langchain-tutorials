import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming vectors_array is your data
vectors_array = np.random.rand(100,10)

# Compute the correlation matrix
corr = np.corrcoef(vectors_array, rowvar=False)

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})