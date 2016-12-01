import sys
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_fscore_support

def ave(score):
	sum = 0.00
	for i in score:
		sum += i
	return sum/len(score)

I_data = pd.read_csv('I_data.csv', header=0)
I_label = pd.read_csv('I_label.csv', header=0)

J_data = pd.read_csv('J_data.csv', header=0)
J_label = pd.read_csv('J_label.csv', header=0)

print(I_data.columns[12])
print(I_data.columns[30])
I_data.drop(I_data.columns[12], axis=1, inplace=True)
I_data.drop(I_data.columns[30], axis=1, inplace=True)

J_data.drop(I_data.columns[12], axis=1, inplace=True)
J_data.drop(I_data.columns[30], axis=1, inplace=True)

I_data = np.array(I_data)
J_data = np.array(J_data)

I_label = np.array(I_label['gold'])
J_label = np.array(J_label['gold'])

cv_num = 10

# min_samples_leaf = 2

rfClf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=4, min_samples_split=3, min_samples_leaf=2, min_weight_fraction_leaf=0.0, max_features=6, max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0, warm_start=False, class_weight=None)
'''
scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
ave_score = ave(scores)
print(ave_score)
'''

# Test on table J
rfClf.fit(I_data, I_label)
results = rfClf.predict(J_data)
scores = precision_recall_fscore_support(J_label, results, average='micro')
print(scores)
