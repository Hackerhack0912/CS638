import sys
import pandas as pd
import numpy as np
'''
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
'''
def ave(score):
	sum = 0.00
	for i in score:
		sum += i
	return sum/len(score)

I_data = pd.read_csv('I_data.csv', header=0)
I_label = pd.read_csv('I_label.csv', header=0)

# Drop the entire feature one by one
I_label = np.array(I_label['gold'])
for i in range(0, 43):
    I_data_temp = I_data
    I_data_temp.drop(I_data_temp.columns[0], axis=1, inplace=True)

    I_data = np.array(I_data_temp)

    cv_num = 6

    # Decision Tree
    dtClf = tree.DecisionTreeClassifier()
    scores = cross_val_score(dtClf, I_data, I_label, cv=cv_num)
    print("Decision Tree F-1 score:")
    print(scores)
    print(ave(scores))

    # Random Forest
    rfClf = RandomForestClassifier(n_estimators=100)
    scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
    print("Random Forest F-1 score:")
    print(scores)
    print(ave(scores))

    # Support Vector Machine
    lsvmClf = svm.SVC(kernel='linear', C=1)
    scores = cross_val_score(lsvmClf, I_data, I_label, cv=cv_num)
    print("Linear SVM F-1 score:")
    print(scores)
    print(ave(scores))

    # Naive Bayes
    gnbClf = GaussianNB()
    scores = cross_val_score(gnbClf, I_data, I_label, cv=cv_num)
    print("Gaussian Naive Bayes score:")
    print(scores)
    print(ave(scores))

    bernoulliClf = BernoulliNB()
    scores = cross_val_score(bernoulliClf, I_data, I_label, cv=cv_num)
    print("Bernoulli Naive Bayes score:")
    print(scores)
    print(ave(scores))

    # Logistic Regression
    l1lrClf = LogisticRegression(penalty='l1', tol=0.01)
    scores = cross_val_score(l1lrClf, I_data, I_label, cv=cv_num)
    print("L1 Logistic Regression score: ")
    print(scores)
    print(ave(scores))

    l2lrClf = LogisticRegression(penalty='l2', tol=0.01)
    scores = cross_val_score(l2lrClf, I_data, I_label, cv=cv_num)
    print("L2 Logistic Regression score: ")
    print(scores)
    print(ave(scores))
