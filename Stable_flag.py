from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.naive_bayes import GaussianNB 
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score
from explainerdashboard import ClassifierExplainer, ExplainerDashboard
import pandas as pd
import Data_preparation as prep

X = prep.Targets_df[['Cooler condition', 'Valve condition', 'Internal pump leakage', 'Hydraulic accumulator']]
Y = prep.Targets_df['Stable flag']
X_train = prep.Target_train[['Cooler condition', 'Valve condition', 'Internal pump leakage', 'Hydraulic accumulator']]
Y_train = prep.Target_train['Stable flag']
X_test = prep.Target_test[['Cooler condition', 'Valve condition', 'Internal pump leakage', 'Hydraulic accumulator']]
Y_test = prep.Target_test['Stable flag']


#                            *** Logistic Regression ***
Reg = LogisticRegression()

Reg.fit(X_train, Y_train)
prediction_train_reg = Reg.predict(X_train)
prediction_test_reg = Reg.predict(X_test)

# Scoring this model 
reg_score_train = accuracy_score(Y_train, prediction_train_reg)
reg_score_test = accuracy_score(Y_test, prediction_test_reg)
print(reg_score_train, reg_score_test)

#Cross validation
reg_cv = cross_validate(Reg, X, Y,  scoring = ['accuracy', 'precision_weighted'], cv=5)
reg_cv_acc = reg_cv["test_accuracy"].mean()
reg_cv_prec = reg_cv["test_precision_weighted"].mean()


#                            *** Support Vector Machine ***
SVM = svm.SVC()

SVM.fit(X_train, Y_train)
prediction_train_svm = SVM.predict(X_train)
prediction_test_svm = SVM.predict(X_test)

# Scoring this model 
svm_score_train = accuracy_score(Y_train, prediction_train_svm)
svm_score_test = accuracy_score(Y_test, prediction_test_svm)

#Cross validation
svm_cv = cross_validate(SVM, X, Y,  scoring = ['accuracy', 'precision_weighted'], cv=5)
svm_cv_acc = svm_cv["test_accuracy"].mean()
svm_cv_prec = svm_cv["test_precision_weighted"].mean()


#                            *** K-Nearest Neighbours ***
KNN = KNeighborsClassifier(n_neighbors=5, p=2 )  

KNN.fit(X_train, Y_train)
prediction_train_knn = KNN.predict(X_train)
prediction_test_knn = KNN.predict(X_test)

# Scoring this model 
knn_score_train = accuracy_score(Y_train, prediction_train_knn)
knn_score_test = accuracy_score(Y_test, prediction_test_knn)

#Cross validation
knn_cv = cross_validate(KNN, X, Y,  scoring = ['accuracy', 'precision_weighted'], cv=5)
knn_cv_acc = knn_cv["test_accuracy"].mean()
knn_cv_prec = knn_cv["test_precision_weighted"].mean()


#                            *** Naïve Bayes ***
GNV = GaussianNB()   

GNV.fit(X_train, Y_train)
prediction_train_gauss = GNV.predict(X_train)
prediction_test_gauss = GNV.predict(X_test)

# Scoring this model 
gauss_score_train = accuracy_score(Y_train, prediction_train_gauss)
gauss_score_test = accuracy_score(Y_test, prediction_test_gauss)

#Cross validation
gauss_cv = cross_validate(GNV, X, Y,  scoring = ['accuracy', 'precision_weighted'], cv=5)
gauss_cv_acc = gauss_cv["test_accuracy"].mean()
gauss_cv_prec = gauss_cv["test_precision_weighted"].mean()


#                            *** Decision Tree Classification ***
Dec_tree = DecisionTreeClassifier(criterion='entropy', random_state=0) 

Dec_tree.fit(X_train, Y_train)
prediction_train_dec = Dec_tree.predict(X_train)
prediction_test_dec = Dec_tree.predict(X_test)

# Scoring this model 
dec_score_train = accuracy_score(Y_train, prediction_train_dec)
dec_score_test = accuracy_score(Y_test, prediction_test_dec)

#Cross validation
dec_cv = cross_validate(Dec_tree, X, Y,  scoring = ['accuracy', 'precision_weighted'], cv=5)
dec_cv_acc = dec_cv["test_accuracy"].mean()
dec_cv_prec = dec_cv["test_precision_weighted"].mean()


#                            *** Random Forest Classification ***
Random_For = RandomForestClassifier(n_estimators= 10, criterion="entropy")  

Random_For.fit(X_train, Y_train)
prediction_train_randomfor = Random_For.predict(X_train)
prediction_test_randomfor = Random_For.predict(X_test)

# Scoring this model 
random_for_score_train = accuracy_score(Y_train, prediction_train_randomfor)
random_for_score_test = accuracy_score(Y_test, prediction_test_randomfor)

#Cross validation
random_for_cv = cross_validate(Random_For, X, Y,  scoring = ['accuracy', 'precision_weighted'], cv=5)
random_for_cv_acc = random_for_cv["test_accuracy"].mean()
random_for_cv_prec = random_for_cv["test_precision_weighted"].mean()


#       Choosing the best model
choice = {"Logistic Regression": [reg_score_train, reg_score_test], 
 "Support Vector Machine": [svm_score_train, svm_score_test], 
  "K-Nearest Neighbours": [knn_score_train, knn_score_test], 
  'Naïve Bayes': [gauss_score_train, gauss_score_test], 
  "Decision Tree Classification": [dec_score_train, dec_score_test], 
  "Random Forest Classification" : [random_for_score_train, random_for_score_test]}

scores = pd.DataFrame(choice, index = ['Train', 'Test'])
print(scores.T)

cv_scores = {"Logistic Regression": [reg_cv_acc, reg_cv_prec], 
 "Support Vector Machine": [svm_cv_acc, svm_cv_prec], 
  "K-Nearest Neighbours": [knn_cv_acc, knn_cv_prec], 
  'Naïve Bayes': [gauss_cv_acc, gauss_cv_prec], 
  "Decision Tree Classification": [dec_cv_acc, dec_cv_prec], 
  "Random Forest Classification" : [random_for_cv_acc, random_for_cv_prec]}

scores_cv = pd.DataFrame(cv_scores, index = ['Accuracy score', 'Precision score'])
print(scores_cv.T)


#print("The best model is {} with an accuracy score of {}".format(list(choice.keys())[list(choice.values()).index(max(choice.values()))],max(choice.values())))
