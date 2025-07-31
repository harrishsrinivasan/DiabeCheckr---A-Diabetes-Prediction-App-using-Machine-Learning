import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

import pickle


data = pd.read_csv('diabetes.csv')





data_X = data.iloc[:,[1, 4, 5, 7]].values
data_Y = data.iloc[:,8].values





data_X






from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))
data_scaled = sc.fit_transform(data_X)





data_scaled = pd.DataFrame(data_scaled)




X = data_scaled
Y = data_Y


X




Y





from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 42, stratify = dataset['Outcome'] )





from sklearn.ensemble import RandomForestClassifier as rfc 
rfc = rfc(n_estimators = 100, random_state = 42, probability=True)
rfc.fit(X_train, Y_train)





rfc.score(X_test, Y_test)


Y_pred = rfc.predict(X_test)





pickle.dump(rfc, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))