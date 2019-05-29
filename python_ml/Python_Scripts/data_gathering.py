# *************** DATA GATHERING AND EXPLORATION FUNCTIONS *******************
# add libraries
from Python_Scripts.utility_functions import *
import matplotlib.pyplot as plt
import missingno as mn

def show_missing(read_path, write_path):
    res = read_data(read_path)
    mn.matrix(res)
    plt.savefig(write_path)

def show_histograms(read_path,write_path):
	res = read_data(read_path)
	res1=res[['price', 'bedrooms', 'bathrooms', 'sqft_living',
    'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
    'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
    'lat', 'long', 'sqft_living15', 'sqft_lot15']]
	res1.hist(bins=25,figsize=(16,16),xlabelsize='10',ylabelsize='10',xrot=-15)
	plt.savefig(write_path)

def show_boxplot(read_path, write_path):
	res = read_data(read_path)
	f, axes = plt.subplots(1, 2,figsize=(15,5))
	sns.boxplot(x=res['bedrooms'],y=res['price'], ax=axes[0])
	sns.boxplot(x=res['floors'],y=res['price'], ax=axes[1])
	# sns.despine(left=True, bottom=True)
	axes[0].set(xlabel='Bedrooms', ylabel='Price')
	axes[0].yaxis.tick_left()
	axes[1].yaxis.set_label_position("right")
	axes[1].yaxis.tick_right()
	axes[1].set(xlabel='Floors', ylabel='Price')
	plt.savefig(write_path)