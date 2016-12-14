import sys
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support

def ave(score):
	sum = 0.00
	for i in score:
		sum += i
	return sum/len(score)

def crossValidation(cv_data, cv_label, fold_num, clf):
        cv_label = np.array(cv_label)
        total_row_num = len(cv_data)
        offset = int(total_row_num/fold_num)
        precision = 0
        recall = 0
        fscore = 0
        for i in range(fold_num):
                start_index = i*offset
                #print("Start_Index: " + str(start_index))
                end_index = start_index + offset
                #print("End_Index: " + str(end_index))
                test_data = cv_data.iloc[i*offset:i*offset+offset]
                #test_label = cv_label.iloc[i*offset:i*offset+offset]
                test_label = cv_label[i*offset:i*offset+offset]
                train_data_1 = cv_data.iloc[0:i*offset]
                train_data_2 = cv_data.iloc[i*offset+offset:]
                #train_label_1 = cv_label.iloc[0:i*offset]
                #train_label_2 = cv_label.iloc[i*offset+offset:]
                train_label_1 = cv_label[0:i*offset]
                train_label_2 = cv_label[i*offset+offset:]
                train_data = pd.concat([train_data_1, train_data_2])
                #print(len(train_data))
                #train_label = pd.concat([train_label_1, train_label_2])
                train_label = np.append(train_label_1, train_label_2)
                clf.fit(train_data, train_label)
                results = clf.predict(test_data)
                scores = precision_recall_fscore_support(test_label, results, average = 'binary')
                precision += scores[0]
                recall += scores[1]
                fscore += scores[2]
        return [precision/10.00, recall/10.00, fscore/10.00]

I_data = pd.read_csv('I_data.csv', header=0)
I_label = pd.read_csv('I_label.csv', header=0)

#J_data = pd.read_csv('J_data.csv', header=0)
#J_label = pd.read_csv('J_label.csv', header=0)

C_data = pd.read_csv('tableMerge.csv', header=0)

print(I_data.columns[12])
print(I_data.columns[30])
I_data.drop(I_data.columns[12], axis=1, inplace=True)
I_data.drop(I_data.columns[30], axis=1, inplace=True)

#J_data.drop(I_data.columns[12], axis=1, inplace=True)
#J_data.drop(I_data.columns[30], axis=1, inplace=True)

# Random Forest
#rfClf = RandomForestClassifier(n_estimators=100)
rfClf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=4, min_samples_split=3, min_samples_leaf=2, min_weight_fraction_leaf=0.0, max_features=6, max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0, warm_start=False, class_weight=None)
print("Random Forest F-1 score:")
print(crossValidation(I_data, I_label, 10, rfClf))

I_data = np.array(I_data)
#J_data = np.array(J_data)

I_label = np.array(I_label['gold'])
#J_label = np.array(J_label['gold'])

cv_num = 10

# min_samples_leaf = 2


rfClf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=4, min_samples_split=3, min_samples_leaf=2, min_weight_fraction_leaf=0.0, max_features=6, max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0, warm_start=False, class_weight=None)
scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
ave_score = ave(scores)
print(ave_score)

'''
rfClf = RandomForestClassifier(n_estimators=100)
scores = cross_val_score(rfClf, I_data, I_label, cv=cv_num)
ave_score = ave(scores)
print(ave_score)
'''

print("***********************************")
# Test on table J
rfClf.fit(I_data, I_label)
results = rfClf.predict(C_data)
#results = rfClf.predict(J_data)
#print(type(results))
#scores = precision_recall_fscore_support(J_label, results, average='binary')
#print(scores)
print(results)
'''
# Decision Tree
Clf = tree.DecisionTreeClassifier()
print("Decision Tree F-1 score:")
Clf.fit(I_data, I_label)
results = Clf.predict(J_data)
print(type(results))
scores = precision_recall_fscore_support(J_label, results, average='binary')
print(scores)

# Support Vector Machine
Clf = svm.SVC(kernel='linear', C=1)
print("Linear SVM F-1 score:")
Clf.fit(I_data, I_label)
results = Clf.predict(J_data)
print(type(results))
scores = precision_recall_fscore_support(J_label, results, average='binary')
print(scores)
# Naive Bayes
Clf = GaussianNB()
print("Gaussian Naive Bayes score:")
Clf.fit(I_data, I_label)
results = Clf.predict(J_data)
print(type(results))
scores = precision_recall_fscore_support(J_label, results, average='binary')
print(scores)

Clf = BernoulliNB()
print("Bernoulli Naive Bayes score:")
Clf.fit(I_data, I_label)
results = Clf.predict(J_data)
print(type(results))
scores = precision_recall_fscore_support(J_label, results, average='binary')
print(scores)

# Logistic Regression
Clf = LogisticRegression(penalty='l1', tol=0.01)
print("L1 Logistic Regression score: ")
Clf.fit(I_data, I_label)
results = Clf.predict(J_data)
print(type(results))
scores = precision_recall_fscore_support(J_label, results, average='binary')
print(scores)

Clf = LogisticRegression(penalty='l2', tol=0.01)
print("L2 Logistic Regression score: ")
Clf.fit(I_data, I_label)
results = Clf.predict(J_data)
print(type(results))
scores = precision_recall_fscore_support(J_label, results, average='binary')
print(scores)
'''
