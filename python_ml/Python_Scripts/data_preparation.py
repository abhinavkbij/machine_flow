# *************** DATA PREPARATION FUNCTIONS *******************
# add libraries
from Python_Scripts.utility_functions import *
import json

def split_data(read_path, write_path, target_feature, split_percentage):
    X_train, X_test, Y_train, Y_test = create_train_test(read_path, target_feature, split_percentage)
    write_split_sets(write_path, X_train, X_test, Y_train, Y_test)

def binning(read_path,write_path):
	res = read_data(read_path)
	# just take the year from the date column
	res['sales_yr']=res['date'].astype(str).str[:4]

	# add the age of the buildings when the houses were sold as a new column
	res['age']=res['sales_yr'].astype(int)-res['yr_built']
	# add the age of the renovation when the houses were sold as a new column
	res['age_rnv']=0
	res['age_rnv']=res['sales_yr'][res['yr_renovated']!=0].astype(int)-res['yr_renovated'][res['yr_renovated']!=0]
	res['age_rnv'][res['age_rnv'].isnull()]=0

	# partition the age into bins
	bins = [-2,0,5,10,25,50,75,100,100000]
	labels = ['<1','1-5','6-10','11-25','26-50','51-75','76-100','>100']
	res['age_binned'] = pd.cut(res['age'], bins=bins, labels=labels)
	# partition the age_rnv into bins
	bins = [-2,0,5,10,25,50,75,100000]
	labels = ['<1','1-5','6-10','11-25','26-50','51-75','>75']
	res['age_rnv_binned'] = pd.cut(res['age_rnv'], bins=bins, labels=labels)

	# histograms for the binned columns
	f, axes = plt.subplots(1, 2,figsize=(15,5))
	p1=sns.countplot(res['age_binned'],ax=axes[0])
	for p in p1.patches:
	    height = p.get_height()
	    p1.text(p.get_x()+p.get_width()/2,height + 50,height,ha="center")   
	p2=sns.countplot(res['age_rnv_binned'],ax=axes[1])
	sns.despine(left=True, bottom=True)
	for p in p2.patches:
	    height = p.get_height()
	    p2.text(p.get_x()+p.get_width()/2,height + 200,height,ha="center")
	    
	axes[0].set(xlabel='Age')
	axes[0].yaxis.tick_left()
	axes[1].yaxis.set_label_position("right")
	axes[1].yaxis.tick_right()
	axes[1].set(xlabel='Renovation Age');
	plt.savefig(write_path)
	# transform the factor values to be able to use in the model
	# res = pd.get_dummies(res, columns=['age_binned','age_rnv_binned'])
