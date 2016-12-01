import sys
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression

def ave(score):
	sum = 0.00
	for i in score:
		sum += i
	return sum/len(score)

I_data = pd.read_csv('I_data.csv', header=0)
I_label = pd.read_csv('I_label.csv', header=0)

columns = list(I_data.columns.values)

# Drop the entire feature one by one
I_label = np.array(I_label['gold'])
for i in range(-1, 42):
    if(i != -1):
         I_data_temp = I_data.copy()
         I_data_temp.drop(columns[i], axis=1, inplace=True)
    else:
        I_data_temp = I_data.copy()
        cur_I_data = np.array(I_data_temp)
	
    cv_num = 10
    # Decision Tree
    dtClf = tree.DecisionTreeClassifier()
    scores = cross_val_score(dtClf, cur_I_data, I_label, cv=cv_num)
    print("Decision Tree F-1 score:")
    #print(scores)
    print(ave(scores))

    # Random Forest
    rfClf = RandomForestClassifier(n_estimators=100)
    scores = cross_val_score(rfClf, cur_I_data, I_label, cv=cv_num)
    print("Random Forest F-1 score:")
    #print(scores)
    print(ave(scores))

    # Support Vector Machine
    lsvmClf = svm.SVC(kernel='linear', C=1)
    scores = cross_val_score(lsvmClf, cur_I_data, I_label, cv=cv_num)
    print("Linear SVM F-1 score:")
    #print(scores)
    print(ave(scores))

    # Naive Bayes
    gnbClf = GaussianNB()
    scores = cross_val_score(gnbClf, cur_I_data, I_label, cv=cv_num)
    print("Gaussian Naive Bayes score:")
    #print(scores)
    print(ave(scores))

    bernoulliClf = BernoulliNB()
    scores = cross_val_score(bernoulliClf, cur_I_data, I_label, cv=cv_num)
    print("Bernoulli Naive Bayes score:")
    #print(scores)
    print(ave(scores))

    # Logistic Regression
    l1lrClf = LogisticRegression(penalty='l1', tol=0.01)
    scores = cross_val_score(l1lrClf, cur_I_data, I_label, cv=cv_num)
    print("L1 Logistic Regression score: ")
    #print(scores)
    print(ave(scores))

    l2lrClf = LogisticRegression(penalty='l2', tol=0.01)
    scores = cross_val_score(l2lrClf, cur_I_data, I_label, cv=cv_num)
    print("L2 Logistic Regression score: ")
    #print(scores)
    print(ave(scores))

    print("\ndrop column " + str(i)+"\n")
	
