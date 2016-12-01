import sys
import copy
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression

def ave(scores):
	sum = 0.00
	for i in scores:
		sum += i
	return sum/len(scores)

def tuneFeature(columns, I_data, max_score):
        cv_num = 10
        cur_max_score = 0
        cur_max_index = -1
        cur_data = I_data
        for i in range(-1, len(columns)):
                if(i != -1):
                        I_data_temp = copy.deepcopy(I_data)
                        I_data_temp.drop(columns[i], axis=1, inplace=True)
                else:
                        I_data_temp = copy.deepcopy(I_data)
                        cur_I_data = np.array(I_data_temp)

                total_score = 0
                for j in range(10):
                        rfClf = RandomForestClassifier(n_estimators=100)
                        scores = cross_val_score(rfClf, cur_I_data, I_label, cv=cv_num)
                        ave_score = ave(scores)
                        total_score += ave_score
                        
                ave_total_score = total_score/10.00
                if(ave_total_score > cur_max_score):
                        cur_max_score = ave_total_score
                        cur_max_index = i
                        cur_data = copy.deepcopy(I_data_temp)
                        print("Max score so far: " + str(cur_max_score))
                        if(i != -1):
                                print("Column removed: " + str(columns[cur_max_index]))
                        else:
                                print("Before removing any column")
        return [cur_max_index, cur_data, cur_max_score]


# initial data
I_data = pd.read_csv('I_data.csv', header=0)
I_label = pd.read_csv('I_label.csv', header=0)

columns = list(I_data.columns.values)
max_score = 0

# Drop the entire feature one by one
I_label = np.array(I_label['gold'])

for i in range(42):
        next_input = tuneFeature(columns, I_data, max_score)
        if(next_input[0] == -1):
                print("No column was removed in the last run")
                break
        if(next_input[2] <= max_score):
                print("No improvement in the last run")
                break
        columns = list(next_input[1].columns.values)
        I_data = next_input[1]
        max_score = next_input[2]
        print("removed column: " + columns[next_input[0]])
        print("current max score: " + str(max_score))
