from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from explainerdashboard import ClassifierExplainer, ExplainerDashboard
import pandas as pd
import Data_preparation as prep

#                            *** Logistic Regression ***
from sklearn.linear_model import LogisticRegression
Reg = LogisticRegression()

Reg.fit(prep.Data_train_scaled, prep.Target_train['Cooler condition'])

prediction_train_reg = Reg.predict(prep.Data_train_scaled)
prediction_test_reg = Reg.predict(prep.Data_test_scaled)

# Scoring this model 
reg_score_train = accuracy_score(prep.Target_train['Cooler condition'], prediction_train_reg)
reg_score_test = accuracy_score(prep.Target_test['Cooler condition'], prediction_test_reg)


#                            *** Support Vector Machine ***
from sklearn import svm
SVM = svm.SVC()

SVM.fit(prep.Data_train_scaled, prep.Target_train['Cooler condition'])
prediction_train_svm = SVM.predict(prep.Data_train_scaled)
prediction_test_svm = SVM.predict(prep.Data_test_scaled)


# Scoring this model 
svm_score_train = accuracy_score(prep.Target_train['Cooler condition'], prediction_train_svm)
svm_score_test = accuracy_score(prep.Target_test['Cooler condition'], prediction_test_svm)


#                            *** K-Nearest Neighbours ***
from sklearn.neighbors import KNeighborsClassifier 

KNN = KNeighborsClassifier(n_neighbors=5, p=2 )  

KNN.fit(prep.Data_train_scaled, prep.Target_train['Cooler condition'])
prediction_train_knn = KNN.predict(prep.Data_train_scaled)
prediction_test_knn = KNN.predict(prep.Data_test_scaled)


# Scoring this model 
knn_score_train = accuracy_score(prep.Target_train['Cooler condition'], prediction_train_knn)
knn_score_test = accuracy_score(prep.Target_test['Cooler condition'], prediction_test_knn)


#                            *** Naïve Bayes ***
from sklearn.naive_bayes import GaussianNB 

GNV = GaussianNB()   

GNV.fit(prep.Data_train_scaled, prep.Target_train['Cooler condition'])
prediction_train_gauss = GNV.predict(prep.Data_train_scaled)
prediction_test_gauss = GNV.predict(prep.Data_test_scaled)


# Scoring this model 
gauss_score_train = accuracy_score(prep.Target_train['Cooler condition'], prediction_train_gauss)
gauss_score_test = accuracy_score(prep.Target_test['Cooler condition'], prediction_test_gauss)



#                            *** Decision Tree Classification ***
from sklearn.tree import DecisionTreeClassifier

Dec_tree = DecisionTreeClassifier(criterion='entropy', random_state=0) 

Dec_tree.fit(prep.Data_train_scaled, prep.Target_train['Cooler condition'])
prediction_train_dec = Dec_tree.predict(prep.Data_train_scaled)
prediction_test_dec = Dec_tree.predict(prep.Data_test_scaled)

# Scoring this model 
dec_score_train = accuracy_score(prep.Target_train['Cooler condition'], prediction_train_dec)
dec_score_test = accuracy_score(prep.Target_test['Cooler condition'], prediction_test_dec)


#                            *** Random Forest Classification ***
from sklearn.ensemble import RandomForestClassifier

Random_For = RandomForestClassifier(n_estimators= 10, criterion="entropy")  

Random_For.fit(prep.Data_train_scaled, prep.Target_train['Cooler condition'])
prediction_train_randomfor = Random_For.predict(prep.Data_train_scaled)
prediction_test_randomfor = Random_For.predict(prep.Data_test_scaled)

# Scoring this model 
random_for_score_train = accuracy_score(prep.Target_train['Cooler condition'], prediction_train_randomfor)
random_for_score_test = accuracy_score(prep.Target_test['Cooler condition'], prediction_test_randomfor)

#                            *** Tpot Classification ***
from tpot import TPOTClassifier

tpotc=TPOTClassifier(generations=20,population_size=50,scoring=["accuracy","precision"],cv=5,verbosity=2,n_jobs=-1,random_state=42,config_dict="TPOT light")
tpotc.fit(prep.Data_train_scaled, prep.Target_train['Stable flag'])
tpotc.fitted_pipeline_
prediction_train_tpot = tpotc.predict(prep.Data_train_scaled)
prediction_test_tpot = tpotc.predict(prep.Data_test_scaled)

# Scoring this model 
tpot_score_train = accuracy_score(prep.Target_train['Stable flag'], prediction_train_tpot)
tpot_score_test = accuracy_score(prep.Target_test['Stable flag'], prediction_test_tpot)


#       Choosing the best model
choice = {"Logistic Regression": [reg_score_train, reg_score_test], 
 "Support Vector Machine": [svm_score_train, svm_score_test], 
  "K-Nearest Neighbours": [knn_score_train, knn_score_test], 
  'Naïve Bayes': [gauss_score_train, gauss_score_test], 
  "Tpot Classification": [tpot_score_train, tpot_score_test]}


scores = pd.DataFrame(choice, index = ['Train', 'Test'])
print(scores.T)
#print("Le meilleur algorithme est {} avec un accuracy score de {}".format(
#  list(choice.keys())[list(choice.values()).index(max(choice.values()))],max(choice.values())))


