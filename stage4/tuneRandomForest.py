import sys
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

def ave(score):
	sum = 0.00
	for i in score:
		sum += i
	return sum/len(score)

I_data = pd.read_csv('I_data.csv', header=0)
I_label = pd.read_csv('I_label.csv', header=0)

I_data = np.array(I_data)
I_label = np.array(I_label['gold'])

cv_num = 10

# Random Forest
'''
rfClf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False, class_weight=None)
scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
print("criterion = gini")
print(scores)
print(ave(scores))
'''

'''
rfClf = RandomForestClassifier(n_estimators=100, criterion='entropy', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False, class_weight=None)
scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
print("criterion = entropy")
print(scores)
print(ave(scores))
'''

'''
for i in [3,4]:
	rfClf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=i+1, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False, class_weight=None)
	scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
	print("Max Depth: " + str(i+1))
	print(scores)
	print(ave(scores))
'''

'''
max_score = 0
max_index = 0
for i in range(42):
	_max_feature = i+1
	rfClf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=4, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=_max_feature, max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0, warm_start=False, class_weight=None)
	scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
	ave_score = ave(scores)
	if(ave_score > max_score):
		max_score = ave_score
		max_index = i+1
		print(max_score)
		print(max_index)
'''
# max number of features: 6

'''
max_score = 0
max_index = 0
for i in range(2,20):
	rfClf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=4, min_samples_split=i, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=6, max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0, warm_start=False, class_weight=None)
	scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
	ave_score = ave(scores)
	if(ave_score > max_score):
		max_score = ave_score
		max_index = i
		print(max_score)
		print(max_index)
'''
# min_sample_split = 3
'''
max_score = 0
max_index = 0
for i in range(1,20):
    rfClf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=4, min_samples_split=3, min_samples_leaf=i, min_weight_fraction_leaf=0.0, max_features=6, max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0, warm_start=False, class_weight=None)
    scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
    ave_score = ave(scores)
    if(ave_score > max_score):
        max_score = ave_score
        max_index = i
        print(max_score)
        print(max_index)
'''
# min_samples_leaf = 2

rfClf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=4, min_samples_split=3, min_samples_leaf=2, min_weight_fraction_leaf=0.0, max_features=6, max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0, warm_start=False, class_weight=None)
scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
ave_score = ave(scores)
print(ave_score)
