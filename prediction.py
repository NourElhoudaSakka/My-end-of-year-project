import Data_preparation as prep
from Cooler_condition import Reg
from Hydraulic_accumulator import Random_For
from Valve_condition import Dec_tree
from Internal_pump_leakage import Random_For2
from Stable_flag import SVM

Data_to_predict = prep.pd.DataFrame(columns = prep.clms)
Data_to_predict.loc[0] = prep.Data_df.iloc[15]
#print(Data_to_predict.T)

def predict(Data_to_predict):
    target1_prediction = Reg.predict(Data_to_predict)
    
    target2_prediction = Dec_tree.predict(Data_to_predict)
    
    target3_prediction = Random_For.predict(Data_to_predict)
    
    target4_prediction = Random_For2.predict(Data_to_predict)
    
    Final_prediction = prep.pd.DataFrame(columns = ['Cooler condition', 'Valve condition', 'Internal pump leakage', 'Hydraulic accumulator'])
    Final_prediction.loc[0] = [target1_prediction, target2_prediction, target3_prediction, target4_prediction]
    
    final_target_prediction = SVM.predict(Final_prediction)
    
    return [target1_prediction, target2_prediction, target3_prediction, target4_prediction, final_target_prediction]

print (predict(Data_to_predict))