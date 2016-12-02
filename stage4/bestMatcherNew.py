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

I_data = pd.read_csv('I_data_tuned.csv', header=0)
I_label = pd.read_csv('I_label.csv', header=0)

columns = list(I_data.columns.values)


# Drop the entire feature one by one
#I_label = np.array(I_label['gold'])

# Decision Tree
dtClf = tree.DecisionTreeClassifier()
print("Decision Tree F-1 score:")
print(crossValidation(I_data, I_label, 10, dtClf))

# Random Forest
rfClf = RandomForestClassifier(n_estimators=100)
print("Random Forest F-1 score:")
print(crossValidation(I_data, I_label, 10, rfClf))

# Support Vector Machine
lsvmClf = svm.SVC(kernel='linear', C=1)
print("Linear SVM F-1 score:")
print(crossValidation(I_data, I_label, 10, lsvmClf))

# Naive Bayes
gnbClf = GaussianNB()
print("Gaussian Naive Bayes score:")
print(crossValidation(I_data, I_label, 10, gnbClf))

bernoulliClf = BernoulliNB()
print("Bernoulli Naive Bayes score:")
print(crossValidation(I_data, I_label, 10, bernoulliClf))

# Logistic Regression
l1lrClf = LogisticRegression(penalty='l1', tol=0.01)
print("L1 Logistic Regression score: ")
print(crossValidation(I_data, I_label, 10, l1lrClf))

l2lrClf = LogisticRegression(penalty='l2', tol=0.01)
print("L2 Logistic Regression score: ")
print(crossValidation(I_data, I_label, 10, l2lrClf))


  	
