import csv
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

def compute_histogram_bins(data, desired_bin_size):
    min_val = np.min(data)
    max_val = np.max(data)
    min_boundary = -1.0 * (min_val % desired_bin_size - min_val)
    max_boundary = max_val - max_val % desired_bin_size + desired_bin_size
    n_bins = int((max_boundary - min_boundary) / desired_bin_size) + 1
    bins = np.linspace(min_boundary, max_boundary, n_bins)
    return bins

df = pd.read_csv("foodorders.csv")

h_sunny = df.loc[(df.burger==0) & (df.sunny==1)]["extra"]
h_cloudy = df.loc[(df.burger==0) & (df.sunny==0)]["extra"]

xticks = [i for i in range(5)]
xticks_labels = ['hot_creole', 'max_original', 'green_and_carlic ', 'bean', 'ice_cream']
bins = compute_histogram_bins(h_cloudy.to_numpy(), 1.0)
fig, axs = plt.subplots(3, 2)

axs[0,0].set_title("delifresh_burger", fontsize=10)
axs[0,0].hist([h_sunny.to_numpy(), h_cloudy.to_numpy()], label=['Sunny', 'Cloudy'], align='left', bins=bins, density=True)
axs[0,0].legend(loc='upper left')
axs[0,0].set_xticks(xticks)
axs[0,0].set_xticklabels(xticks_labels, fontsize=8)

h_sunny = df.loc[(df.burger==1) & (df.sunny==1)]["extra"]
h_cloudy = df.loc[(df.burger==1) & (df.sunny==0)]["extra"]
axs[0,1].set_title("cheese_n_beacon", fontsize=10)
axs[0,1].hist([h_sunny.to_numpy(), h_cloudy.to_numpy()], label=['Sunny', 'Cloudy'], align='left', bins=bins, density=True)
axs[0,1].legend(loc='upper left')
axs[0,1].set_xticks(xticks)
axs[0,1].set_xticklabels(xticks_labels, fontsize=8)

h_sunny = df.loc[(df.burger==2) & (df.sunny==1)]["extra"]
h_cloudy = df.loc[(df.burger==2) & (df.sunny==0)]["extra"]
axs[1,0].set_title("salad_warp", fontsize=10)
axs[1,0].hist([h_sunny.to_numpy(), h_cloudy.to_numpy()], label=['Sunny', 'Cloudy'], align='left', bins=bins, density=True)
axs[1,0].legend(loc='upper left')
axs[1,0].set_xticks(xticks)
axs[1,0].set_xticklabels(xticks_labels, fontsize=8)

h_sunny = df.loc[(df.burger==3) & (df.sunny==1)]["extra"]
h_cloudy = df.loc[(df.burger==3) & (df.sunny==0)]["extra"]
axs[1,1].set_title("fish_meal", fontsize=10)
axs[1,1].hist([h_sunny.to_numpy(), h_cloudy.to_numpy()], label=['Sunny', 'Cloudy'], align='left', bins=bins, density=True)
axs[1,1].legend(loc='upper left')
axs[1,1].set_xticks(xticks)
axs[1,1].set_xticklabels(xticks_labels, fontsize=8)

h_sunny = df.loc[(df.burger==4) & (df.sunny==1)]["extra"]
h_cloudy = df.loc[(df.burger==4) & (df.sunny==0)]["extra"]
axs[2,0].set_title("orginal_meal", fontsize=10)
axs[2,0].hist([h_sunny.to_numpy(), h_cloudy.to_numpy()], label=['Sunny', 'Cloudy'], align='left', bins=bins
, density=True)
axs[2,0].legend(loc='upper left')
axs[2,0].set_xticks(xticks)
axs[2,0].set_xticklabels(xticks_labels, fontsize=8)

fig.delaxes(axs[2, 1])

plt.show()
