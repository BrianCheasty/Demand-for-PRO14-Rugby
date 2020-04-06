import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import statsmodels.api as sm
import seaborn as sns
plt.style.use('seaborn') # pretty matplotlib plots
plt.rc('font', size=14)
plt.rc('figure', titlesize=18)
plt.rc('axes', labelsize=15)
plt.rc('axes', titlesize=18)

savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Stadium Percentage Random Forest Model/'

"""#########################
IMPORT THE GAME DATA
"""
dfAt=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Stadium Percentage Data.csv', encoding='latin')

"""########################
Set the Training, Validate and Test Data
"""
X = dfAt.iloc[:, :-1]
y = dfAt['Stadium Percentage']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.125, random_state=1)

"""#########################
Also the average for the MAPE calculation
"""
y_train_avg=np.mean(y_train)
y_val_avg=np.mean(y_val)
y_test_avg=np.mean(y_test)

"""##########################
Model 6 Random Forest  on Stadium Percentage
"""

forest = RandomForestRegressor(n_estimators=500,criterion='mse',random_state=1,n_jobs=-1)
forest.fit(X_train, y_train)
y_train_pred = forest.predict(X_train)
y_val_pred = forest.predict(X_val)

val=X_val.join(y_val, how ='outer')
val=val.reset_index(drop=True)
y_val_pred2=pd.DataFrame(y_val_pred)
validate=val.join(y_val_pred2, how ='outer')
validate=validate.rename(columns={0:'Predicted'})
validate['err']=validate['Stadium Percentage']-validate['Predicted']
validate['errsq']=validate['err']**2
validate['rse']=np.sqrt(validate['errsq'])

team=['Home Team_Benetton Treviso','Home Team_Cardiff Blues','Home Team_Connacht Rugby','Home Team_Edinburgh Rugby',\
      'Home Team_Dragons','Home Team_Ospreys','Home Team_Scarlets','Home Team_Ulster Rugby','Home Team_Zebre Rugby',\
          'Venue_Aviva Stadium','Venue_Irish Independent Park','Venue_RDS Arena','Venue_Myreside','Venue_Thomond Park']

rmseperteam=[]
for i in team:
    df=validate[[i,'Stadium Percentage','rse']]
    df=df[(df[i]==1)]
    rmse=df['rse'].mean()
    attavg=df['Stadium Percentage'].mean()
    mape=rmse/attavg
    print(mape)
    x=[{i:mape}]
    x=pd.DataFrame(x).T
    rmseperteam.append(x)
mapeDF=pd.concat(rmseperteam)
savedfile=mapeDF.to_csv(savepath+'Val Mape.csv',index=False)

    



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

"""
Create a Dataframe of each result
"""

def normalise(row):
    minimum=trainResults['Error'].min()
    maximum=trainResults['Error'].max()
    x=(row['Error']-minimum)/(maximum-minimum)
    return x
y_train2=pd.DataFrame(y_train.reset_index(drop=True))
prediction=pd.DataFrame(y_train_pred)
trainResults=y_train2.join(prediction)
trainResults=trainResults.rename(columns={0:'Prediction'})
trainResults['Error']=trainResults['Prediction']-trainResults['Stadium Percentage']
trainResults['NormalError']=trainResults.apply(lambda row: normalise(row), axis=1)
trainResults['Squared Error']=trainResults['NormalError']**2
trainResults['rse']=np.sqrt(trainResults['Squared Error'])
y_train_res=list(trainResults['rse'])
y_train_res2=list(trainResults['Error'])

def normalise(row):
    minimum=valResults['Error'].min()
    maximum=valResults['Error'].max()
    x=(row['Error']-minimum)/(maximum-minimum)
    return x
y_val2=pd.DataFrame(y_val.reset_index(drop=True))
prediction=pd.DataFrame(y_val_pred)
valResults=y_val2.join(prediction)
valResults=valResults.rename(columns={0:'Prediction'})
valResults['Error']=valResults['Prediction']-valResults['Stadium Percentage']
valResults['NormalError']=valResults.apply(lambda row: normalise(row), axis=1)
valResults['Squared Error']=valResults['NormalError']**2
valResults['rse']=np.sqrt(valResults['Squared Error'])
y_val_res=list(valResults['rse'])
y_val_res2=list(valResults['Error'])

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

savedfile=regResult1.to_csv(savepath+'Stadium Percentage Random Forest.csv',index=False)

"""########################
Plot the Model
"""
#Scatter Plot of Residuals
plt.scatter(y_train_pred,  y_train_res2,
            c='steelblue', marker='o', edgecolor='white',
            label='Training data')
plt.scatter(y_val_pred,  y_val_res2,
            c='limegreen', marker='s', edgecolor='white',
            label='Validation data')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('Stadium Percentage - RF - Residuals vs Fitted')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=0, xmax=1, color='black', lw=2)
plt.xlim([0, 1])
plt.savefig(savepath+'Plot the Residuals.jpeg')
plt.show()

#QQ PLot of Residuals
trainres=np.array(y_train_res2)
valres=np.array(y_val_res2)
fig = sm.qqplot(trainres,fit=True, line='45',
                c='steelblue', marker='o', 
                label='Training Residuals')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.title('Stadium % - RF - Normal Q-Q')
plt.savefig(savepath+'QQPlot.jpeg')
plt.show()

#Scale Loction
plot_lm_3 = plt.figure()
plt.scatter(y_train_pred, y_train_res, alpha=0.5,
            c='steelblue', marker='o', edgecolor='white',
            label='Training data');
plt.scatter(y_val_pred, y_val_res, alpha=0.5,
            c='limegreen', marker='s', edgecolor='white',
            label='Validation data');
sns.regplot(y_train_pred, y_train_res,
            scatter=False,
            ci=False,
            lowess=True,
            line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
plot_lm_3.axes[0].set_title('Stadium % - RF - Scale-Location')
plot_lm_3.axes[0].set_xlabel('Fitted values')
plot_lm_3.axes[0].set_ylabel('$\sqrt{|Standardized Residuals|}$');
plt.savefig(savepath+'Normalised Scale Location.jpeg')

"""##########################
Feature Selection
"""

mrresults=[]
for i in range(1,104):
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
plt.plot(regResult['Overfit'],color='bisque',label='Overfit')
plt.xlabel('Features')
plt.ylabel('MAPE & Overfit')
plt.title('Stadium % - RF - Features vs MAPE vs Overfit')
plt.legend(loc='upper right')
plt.hlines(y=0.1611, xmin=0, xmax=103, color='red', lw=.5)
plt.xlim([0, 105])
plt.savefig(savepath+'Features vs Mape.jpeg')
plt.show()

"""
Run Model on Test Data
"""

forest = RandomForestRegressor(n_estimators=500,criterion='mse',random_state=1,n_jobs=-1, max_features=65)
forest.fit(X_test, y_test)
y_test_pred = forest.predict(X_test)
rmse_test=mean_squared_error(y_test, y_test_pred, squared=False)
r2_test=r2_score(y_test, y_test_pred)
print('RMSE test: %.3f' % (mean_squared_error(y_test, y_test_pred, squared=False)))
print('R^2 test: %.3f' % (r2_score(y_test, y_test_pred)))
mapeTest=rmse_test/y_test_avg
print('Train MAPE = '+str(mapeTest))

"""########################
Create a DataFrame of results for comparison later
"""
mrresults=[rmse_test,r2_test,mapeTest]
regResult1=pd.DataFrame(mrresults).T
regResult1=regResult1.rename(columns={0:'RMSE Test',1:'R2 Test',3:'Mape Test'})
savedfile=regResult1.to_csv(savepath+'Test Stadium Percentage Regression.csv',index=False) 

