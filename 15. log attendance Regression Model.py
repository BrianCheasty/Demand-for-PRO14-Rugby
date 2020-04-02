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
Model 2 Multiple Regression  on Attendance
"""
mlr=linear_model.LinearRegression()
mlr.fit(X_train,y_train)
y_train_pred=mlr.predict(X_train)
y_val_pred=mlr.predict(X_val)

"""########################
Evaluate Regression on Train and Validate set
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

savedfile=regResult1.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Attendance (log)Regression Model/(log)Attendance Regression.csv',index=False)
savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Attendance (log)Regression Model/'
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
plt.title('(log) Attendance - Reg - Residuals vs Fitted')
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
plt.title('(log) Attendance - Reg - Normal Q-Q')
plt.savefig(savepath+'QQPlot.jpeg')
plt.show()

"""#########################
Ordinary Least Squares of Model
"""
X2=sm.add_constant(X_train)
model = sm.OLS(y_train, X2)
model_fit = model.fit()
dataframe = pd.concat([X_train, y_train], axis=1)

# model values
model_fitted_y = model_fit.fittedvalues
# model residuals
model_residuals = model_fit.resid
# absolute squared  residuals
model_residuals_abs_sqrt = np.sqrt(np.abs(model_residuals))
# normalized residuals
model_norm_residuals = model_fit.get_influence().resid_studentized_internal
# absolute squared normalized residuals
model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))
# absolute residuals
model_abs_resid = np.abs(model_residuals)
# leverage, from statsmodels internals
model_leverage = model_fit.get_influence().hat_matrix_diag

#Scale Loction
plot_lm_3 = plt.figure()
plt.scatter(model_fitted_y, model_norm_residuals_abs_sqrt, alpha=0.5);
sns.regplot(model_fitted_y, model_norm_residuals_abs_sqrt,
            scatter=False,
            ci=False,
            lowess=True,
            line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
plot_lm_3.axes[0].set_title('Scale-Location')
plot_lm_3.axes[0].set_xlabel('Fitted values')
plot_lm_3.axes[0].set_ylabel('$\sqrt{|Standardized Residuals|}$');
plt.savefig(savepath+'Normalised Scale Location.jpeg')

plot_lm_4 = plt.figure();
plt.scatter(model_leverage, model_norm_residuals, alpha=0.5);
sns.regplot(model_leverage, model_norm_residuals,
              scatter=False,
              ci=False,
              lowess=True,
              line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
plot_lm_4.axes[0].set_xlim(0, max(model_leverage)+0.01)
plot_lm_4.axes[0].set_ylim(-3, 5)
plot_lm_4.axes[0].set_title('Residuals vs Leverage')
plot_lm_4.axes[0].set_xlabel('Leverage')
plot_lm_4.axes[0].set_ylabel('Standardized Residuals');
plt.savefig(savepath+'Standardised Leverage.jpeg')   

"""##############################
Get the OLS Results
"""
with open(savepath+'OLS Summary.csv', 'w') as fh:
    fh.write(model_fit.summary().as_csv())
    
"""##########################
Feature Selection
"""

mrresults=[]
for i in range(1,73):
    print(i)
    result=[]
    result.append(i)
    rfe = RFE(mlr, i)
    rfe = rfe.fit(X_train, y_train)
    y_train_pred = rfe.predict(X_train)
    y_val_pred = rfe.predict(X_val)
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
plt.hlines(y=0.02985, xmin=0, xmax=73, color='red', lw=.5)
plt.xlim([0, 73])
plt.savefig(savepath+'Features vs Mape.jpeg')
plt.show()


rfe = RFE(mlr, 1)
rfe = rfe.fit(X_train, y_train)
#Examine the Features
ranking=rfe.ranking_
ranks=pd.DataFrame(ranking)
ranks=ranks.rename(columns={0:'Ranking'})
features=pd.DataFrame(X_train.columns)
features=features.rename(columns={0:'Features'})
featureRanks=ranks.join(features,how='outer')
savedfile=featureRanks.to_csv(savepath+'Regression Feature Selection Rankings.csv',index=False)

"""
Run Model on Test Data
"""
rfe = RFE(mlr, 31)
rfe = rfe.fit(X_test, y_test)
y_test_pred = rfe.predict(X_test)
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
