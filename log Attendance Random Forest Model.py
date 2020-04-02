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
plt.style.use('seaborn') # pretty matplotlib plots
plt.rc('font', size=14)
plt.rc('figure', titlesize=18)
plt.rc('axes', labelsize=15)
plt.rc('axes', titlesize=18)

"""#########################
IMPORT THE GAME DATA
"""
dfAt=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/(log)Attendance Data.csv', encoding='latin')

"""########################
Set the Training, Validate and Test Data
"""
X = dfAt.iloc[:, :-1]
y = dfAt['Attendance']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=1)

"""#########################
Also the average for the MAPE calculation
"""
y_train_avg=np.mean(y_train)
y_val_avg=np.mean(y_val)
y_test_avg=np.mean(y_test)

"""##########################
Model 5 Random Forest  on Attendance
"""

forest = RandomForestRegressor(n_estimators=500,criterion='mse',random_state=1,n_jobs=-1)
forest.fit(X_train, y_train)
y_train_pred = forest.predict(X_train)
y_val_pred = forest.predict(X_val)

"""########################
Evaluate Random Forest on Train and Validate set
"""

print('RMSE train: %.3f, Val: %.3f' % (mean_squared_error(y_train, y_train_pred, squared=False),mean_squared_error(y_val, y_val_pred, squared=False)))
print('R^2 train: %.3f, Val: %.3f' % (r2_score(y_train, y_train_pred), r2_score(y_val, y_val_pred)))
rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
rmse_val=mean_squared_error(y_val, y_val_pred,squared=False)
r2_train=r2_score(y_train, y_train_pred)
r2_val=r2_score(y_val, y_val_pred)
mapeTrain=rmse_train/y_train_avg
mapeVal=rmse_val/y_val_avg
print('Train MAPE = '+str(mapeTrain))
print('Val MAPE = '+str(mapeVal))

"""########################
Create a DataFrame of results for comparison later
"""
mrresults=[rmse_train,rmse_val,r2_train,r2_val,mapeTrain,mapeVal]
regResult1=pd.DataFrame(mrresults).T
regResult1=regResult1.rename(columns={0:'RMSE Train',1:'RMSE Val',2:'R2 Train',3:'R2 Val',4:'Mape Train',5:'Mape Val'})
regResult1['Overfit3']=regResult1['Mape Train']-regResult1['Mape Val']
regResult1['Overfit2']=regResult1['Overfit3']**2
regResult1['Overfit']=np.sqrt(regResult1['Overfit2'])
regResult1=regResult1.drop(columns=['Overfit3','Overfit2'])

savedfile=regResult1.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/(log)Attendance Random Forest Model/(log)Attendance Random Forest.csv',index=False)
savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/(log)Attendance Random Forest Model/'
"""########################
Plot the Model
"""
#Scatter Plot of Residuals
plt.scatter(y_train_pred,  y_train_pred - y_train,
            c='steelblue', marker='o', edgecolor='white',
            label='Training data')
plt.scatter(y_val_pred,  y_val_pred - y_val,
            c='limegreen', marker='s', edgecolor='white',
            label='Validation data')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('(log) Attendance - RF - Residuals vs Fitted')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=6, xmax=12, color='black', lw=2)
plt.xlim([6, 12])
plt.savefig(savepath+'Plot the Residuals.jpeg')
plt.show()

#QQ PLot of Residuals
trainres=y_train_pred - y_train
fig = sm.qqplot(trainres,fit=True, line='45',
                c='steelblue', marker='o', 
                label='Residuals')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.title('(log) Attendance - RF - Normal Q-Q')
plt.savefig(savepath+'QQPlot.jpeg')
plt.show()

"""##########################
Feature Selection
"""

mrresults=[]
for i in range(1,73):
    print(i)
    result=[]
    result.append(i)
    forest = RandomForestRegressor(n_estimators=500,criterion='mse',random_state=1,n_jobs=-1,max_features=i)
    forest.fit(X_train, y_train)
    y_train_pred = forest.predict(X_train)
    y_val_pred = forest.predict(X_val)
    rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
    result.append(rmse_train)
    rmse_val=mean_squared_error(y_val, y_val_pred,squared=False)
    result.append(rmse_val)
    r2_train=r2_score(y_train, y_train_pred)
    result.append(r2_train)
    r2_val=r2_score(y_val, y_val_pred)
    result.append(r2_val)
    print('RMSE train: %.3f, val: %.3f' % (mean_squared_error(y_train, y_train_pred,squared=False),mean_squared_error(y_val, y_val_pred,squared=False)))
    print('R^2 train: %.3f, val: %.3f' % (r2_score(y_train, y_train_pred),r2_score(y_val, y_val_pred)))
    MeaTrain=rmse_train/y_train_avg
    Meaval=rmse_val/y_val_avg
    result.append(MeaTrain)
    result.append(Meaval)
    print('Train MAPE = '+str(MeaTrain))
    print('Val MAPE = '+str(Meaval))
    mrresults.append(result)
    
regResult=pd.DataFrame(mrresults)
regResult=regResult.rename(columns={0:'Features',1:'RMSE Train',2:'RMSE Val',3:'R2 Train',4:'R2 Val',5:'Mape Train',6:'Mape Val'})
regResult['Overfit3']=regResult['Mape Train']-regResult['Mape Val']
regResult['Overfit2']=regResult['Overfit3']**2
regResult['Overfit']=np.sqrt(regResult['Overfit2'])
regResult=regResult.drop(columns=['Overfit3','Overfit2'])
savedfile=regResult.to_csv(savepath+'Regression Feature Selection Results.csv',index=False)

plt.plot(regResult['Mape Train'],color='steelblue',label='Train MAPE')
plt.plot(regResult['Mape Val'],color='limegreen',label='Validate MAPE')
plt.plot(regResult['Overfit'],color='red',label='Overfit')
plt.xlabel('Features')
plt.ylabel('MAPE & Overfit')
plt.title('Features vs MAPE')
plt.legend(loc='upper right')
plt.hlines(y=0.193604, xmin=0, xmax=73, color='red', lw=.5)
plt.xlim([0, 73])
plt.savefig(savepath+'Features vs Mape.jpeg')
plt.show()

"""
Run Model on Test Data
"""

forest = RandomForestRegressor(n_estimators=500,criterion='mse',random_state=1,n_jobs=-1, max_features=54)
forest.fit(X_test, y_test)
y_test_pred = forest.predict(X_test)
y_test2=pd.DataFrame(y_test.reset_index(drop=True))
prediction=pd.DataFrame(y_test_pred)
#for i, prediction in enumerate(y_test_pred):
#    print('Predicted: %s. Target: %s' % ((10**(prediction)), (10**(y_test2[i]))+'      '+str(round(prediction-y_test2[i])))
testResults=y_test2.join(prediction)
testResults=testResults.rename(columns={0:'Prediction'})
testResults['Attendance2']=10**testResults['Attendance']
testResults['Prediction2']=10**testResults['Prediction']
testResults['Error']=testResults['Prediction2']-testResults['Attendance2']
testResults['Squared Error']=testResults['Error']**2
mse=testResults['Squared Error'].mean()
test_error=math.sqrt(mse)
test_avg=testResults['Attendance2'].mean()
Meatest=test_error/test_avg
print('Test MAPE = '+str(Meatest))


