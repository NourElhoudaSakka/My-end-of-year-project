from numpy.core.fromnumeric import shape
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


#Importing the dataset
PS1 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\PS1.txt').mean(axis=1)
PS3 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\PS3.txt').mean(axis=1)
PS2 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\PS2.txt').mean(axis=1)
PS4 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\PS4.txt').mean(axis=1)
PS5 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\PS5.txt').mean(axis=1)
PS6 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\PS6.txt').mean(axis=1)
MP = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\EPS1.txt').mean(axis=1)
TS1 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\TS1.txt').mean(axis=1)
TS2 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\TS2.txt').mean(axis=1)
TS3 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\TS3.txt').mean(axis=1)
TS4 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\TS4.txt').mean(axis=1)
VS = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\VS1.txt').mean(axis=1)
FS1 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\FS1.txt').mean(axis=1)
FS2 = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\FS2.txt').mean(axis=1)
ES = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\SE.txt').mean(axis=1)
CE = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\CE.txt').mean(axis=1)
CP = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\CP.txt').mean(axis=1)
Targets = np.genfromtxt(r'C:\Users\Asus\Desktop\pfa\dataset\profile.txt')

# Creating DataFrames
Data_df = pd.DataFrame({'Pression1': PS1, 'Pression2': PS2, 'Pression3': PS3, 'Pression4': PS4, 'Pression5': PS5, 'Pression6': PS6, 'Puissance moteur': MP, 
 'Température1': TS1, 'Température2': TS2, 'Température3': TS3, 'Température4': TS4, 'Vibration': VS, 
 'Débit volumique1': FS1, 'Débit volumique2': FS2, '''Facteur d'efficience''': ES, 'Efficience de refroidissement': CE, 'Puissance de refroidissement': CP},
 index = range(2205))
Targets_df = pd.DataFrame(Targets, columns = ['Cooler condition', 'Valve condition', 'Internal pump leakage', 'Hydraulic accumulator', 'Stable flag'])


# Spliting data
Data_train, Data_test, Target_train, Target_test  = train_test_split(
    Data_df, Targets_df, test_size=0.2, random_state=1)



#Data preprocessing 
clms = ['Pression1', 'Pression2', 'Pression3', 'Pression4', 'Pression5', 'Pression6', 'Puissance moteur', 
 'Température1', 'Température2', 'Température3', 'Température4', 'Vibration', 
 'Débit volumique1', 'Débit volumique2', '''Facteur d'efficience''', 'Efficience de refroidissement', 'Puissance de refroidissement']

Scaler = StandardScaler()

Data_train_scaled = Scaler.fit_transform(Data_train)
Data_test_scaled = Scaler.transform(Data_test)

Data_train_scaled = pd.DataFrame(Data_train_scaled, columns = clms)
Data_test_scaled = pd.DataFrame(Data_test_scaled, columns = clms)




 



