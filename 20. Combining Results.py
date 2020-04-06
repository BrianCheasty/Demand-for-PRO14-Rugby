import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from	sklearn.linear_model	import	LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import math
import statsmodels.api as sm
from scipy import stats
from sklearn.feature_selection import RFE
from statsmodels.graphics.gofplots import ProbPlot
import seaborn as sns


savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/'
df1=pd.read_csv(savepath+'Attendance Regression Model/Attendance Regression.csv',encoding='latin-1')
df2=pd.read_csv(savepath+'Attendance (log)Regression Model/(log)Attendance Regression.csv',encoding='latin-1')
df3=pd.read_csv(savepath+'Stadium Percentage Regression Model/Stadium Percentage Regression.csv',encoding='latin-1')
df4=pd.read_csv(savepath+'Attendance Random Forest Model/Attendance Random Forest.csv',encoding='latin-1')
df5=pd.read_csv(savepath+'(log)Attendance Random Forest Model/(log)Attendance Random Forest.csv',encoding='latin-1')
df6=pd.read_csv(savepath+'Stadium Percentage Random Forest Model/Stadium Percentage Random Forest.csv',encoding='latin-1')

df7=pd.concat([df1,df4,df2,df5,df3,df6])
df7=df7.reset_index(drop=True)

description=pd.DataFrame(['Regression - Attendance','Random Forest - Attendance',\
             'Regression - (log)Attendance','Random Forest - (log)Attendance',\
                 'Regression - Stadium Percentage','Random Forest - Stadium Percentage'])
description=description.rename(columns={0:'Description'})

initResults=description.join(df7, how='outer')

columns=['RMSE Train','RMSE Val','R2 Train','R2 Val','Mape Train','Mape Val','Overfit']

for i in columns:
    initResults[i]=round(initResults[i],2)
    
savedfile=initResults.to_html(savepath+'Combined Initial Results.html',index=False)   
