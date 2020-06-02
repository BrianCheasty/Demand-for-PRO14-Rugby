import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import statsmodels.api as sm
import seaborn as sns
from scipy.stats import shapiro
#from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.feature_selection import SelectFromModel
from statsmodels.stats.diagnostic import het_breuschpagan
plt.style.use('seaborn')
plt.rc('font', size=14)
plt.rc('figure', titlesize=18)
plt.rc('axes', labelsize=15)
plt.rc('axes', titlesize=18)

"""#########################
IMPORT THE GAME DATA
"""
dfAt=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/(log)Attendance Data.csv',\
                 encoding='latin')
savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/(log)Attendance Random Forest Model/'

"""
Multicollinearity
"""
# def multicollinearity_check(X, thresh=10.0):
#     data_type = X.dtypes
#     # print(type(data_type))
#     int_cols = \
#     X.select_dtypes(include=['int', 'int16', 'int32', 'int64', 'float', 'float16', 'float32', 'float64']).shape[1]
#     total_cols = X.shape[1]
#     try:
#         if int_cols != total_cols:
#             raise Exception('All the columns should be integer or float, for multicollinearity test.')
#         else:
#             variables = list(range(X.shape[1]))
#             dropped = True
#             print('''\n\nThe VIF calculator will now iterate through the features and calculate their respective values.
#             It shall continue dropping the highest VIF features until all the features have VIF less than the threshold of 5.\n\n''')
#             while dropped:
#                 dropped = False
#                 vif = [variance_inflation_factor(X.iloc[:, variables].values, ix) for ix in variables]
#                 print('\n\nvif is: ', vif)
#                 maxloc = vif.index(max(vif))
#                 if max(vif) > thresh:
#                     print('dropping \'' + X.iloc[:, variables].columns[maxloc] + '\' at index: ' + str(maxloc))
#                     # del variables[maxloc]
#                     X.drop(X.columns[variables[maxloc]], 1, inplace=True)
#                     variables = list(range(X.shape[1]))
#                     dropped = True

#             print('\n\nRemaining variables:\n')
#             print(X.columns[variables])
#             # return X.iloc[:,variables]
#             return X
#     except Exception as e:
#         print('Error caught: ', e)

"""########################
Set the Training, Validate and Test Data
"""
X = dfAt.iloc[:, :-1]
#multicollinearity_check(X)
y = dfAt['(log)Attendance']
i=[0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2]
idf=[]
for f in i:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=f, random_state=1)
    train_mean=(y_train.mean())
    test_mean=(y_test.mean())
    train_med=(y_train.std())
    test_med=(y_test.std())
    title='Attendance'
    idf.append(pd.DataFrame([title,f,train_mean,test_mean,train_med,test_med]).T)
idf2=pd.concat(idf)
columns=[2,3,4,5]
for i in columns:
    idf2[i]=idf2[i].astype(float)
idf2=idf2.reset_index(drop=True)    
idf2['Mean']=np.sqrt(((idf2[3]-idf2[2])**2))
idf2['std']=np.sqrt((idf2[5]-idf2[4])**2)
minim=idf2['Mean'].min()
idf2=idf2[(idf2['Mean']==minim)]
savedfile=idf2.to_csv(savepath+'Attendance TrainTestSplit.csv',index=False)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.16, random_state=1)
plt.hist(y_train,color='steelblue',label='Train')
plt.hist(y_test,color='darkorange',label='Test')
plt.xlabel('Train and Test Set')
#plt.title('(log)Attendance Distribution Split')
plt.legend()
plt.show()

"""##########################
Model 5 Random Forest  on Attendance
"""
forest = RandomForestRegressor(n_estimators=1000,criterion='mae',random_state=1,n_jobs=-1)
forest.fit(X_train, y_train)
y_train_pred = forest.predict(X_train)

"""########################
Evaluate Regression on Train and Validate set
"""
rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
r2_train=r2_score(y_train, y_train_pred)
def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
mapeTrain=mean_absolute_percentage_error(y_train,y_train_pred)
print('Train MAPE2 = '+str(mapeTrain))

"""########################
Create a DataFrame of results for comparison later
"""
mrresults=[rmse_train,r2_train,mapeTrain]
regResult1=pd.DataFrame(mrresults).T
regResult1=regResult1.rename(columns={0:'RMSE Train',1:'R2 Train',2:'Mape Train'})
savedfile=regResult1.to_csv(savepath+'(log)Attendance Random Forest.csv',index=False)

"""
Review the MAPE of each Team
"""
train=X_train.join(y_train, how ='outer')
train=train.reset_index(drop=True)
y_train_pred2=pd.DataFrame(y_train_pred)
trainidate=train.join(y_train_pred2, how ='outer')
trainidate=trainidate.rename(columns={0:'Predicted'})
trainidate['APE']=np.sqrt((((trainidate['(log)Attendance']-trainidate['Predicted'])/trainidate['(log)Attendance'])*100)**2)
team=['Home_Team_Benetton Treviso','Home_Team_Cardiff Blues','Home_Team_Connacht Rugby',\
      'Home_Team_Dragons','Home_Team_Ospreys','Home_Team_Scarlets','Home_Team_Ulster Rugby','Home_Team_Zebre Rugby',\
          'Venue_Aviva Stadium','Venue_Irish Independent Park','Venue_RDS Arena','Venue_Myreside','Venue_Thomond Park','Venue_BT Murrayfield']
teamMAPE=[]
for i in team:
    df=trainidate[[i,'(log)Attendance','Predicted']]
    df=df[(df[i]==1)]
    mape=mean_absolute_percentage_error(df['(log)Attendance'],df['Predicted'])
    x=[{i:mape}]
    x=pd.DataFrame(x).T
    teamMAPE.append(x)
mapeDF=pd.concat(teamMAPE)
mapeDF=mapeDF.rename(columns={0:'Random Forest - (log)Attendance'})
savedfile=mapeDF.to_csv(savepath+'(log)Attendance Random ForestMAPE.csv')
df=trainidate[(trainidate['APE']>mapeTrain)]
savedfile=df.to_csv(savepath+'highMAPE1.csv')

"""##########################
Feature Selection
"""
x=np.linspace(0.05,2,40)
mrresults=[]
for i in x:
    print(i)
    result=[]
    result.append(i)
    thresh=str(i)+'*mean'
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.16, random_state=1)
    sel = SelectFromModel(RandomForestRegressor(n_estimators=1000,criterion='mae',random_state=1,n_jobs=-1),threshold=thresh)
    sel.fit(X_train, y_train)
    sel.get_support()
    selected_feat= X_train.columns[(sel.get_support())]
    len(selected_feat)
    print(selected_feat)
    X_train=X_train[selected_feat]
    X_test=X_test[selected_feat]
    forest = RandomForestRegressor(n_estimators=1000,criterion='mae',random_state=1,n_jobs=-1)
    forest.fit(X_train, y_train)
    y_train_pred = forest.predict(X_train)
    rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
    result.append(rmse_train)
    r2_train=r2_score(y_train, y_train_pred)
    result.append(r2_train)
    mapeTrain=mean_absolute_percentage_error(y_train,y_train_pred)
    result.append(mapeTrain)
    print('Train MAPE = '+str(mapeTrain))
    mrresults.append(result)
    
regResult=pd.DataFrame(mrresults)
regResult=regResult.rename(columns={0:'Threshold',1:'RMSE Train',2:'R2 Train',3:'Mape Train'})
regResult=regResult.set_index('Threshold')

plt.plot(regResult['Mape Train'],color='steelblue',label='Train MAPE')
plt.xlabel('Threshold')
plt.ylabel('MAPE')
#plt.title('Attendance - RF - MAPE')
plt.legend(loc='upper right')
plt.hlines(y=regResult['Mape Train'].min(), xmin=0, xmax=2, color='red', lw=.5)
#plt.xlim([0, cols])
plt.savefig(savepath+'Threshold vs Mape (log)att.jpeg')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.16, random_state=1)
sel = SelectFromModel(RandomForestRegressor(n_estimators=1000,criterion='mae',random_state=1,n_jobs=-1),threshold='0.25*mean')
sel.fit(X_train, y_train)
sel.get_support()
selected_feat= X_train.columns[(sel.get_support())]
len(selected_feat)
print(selected_feat)
X_train=X_train[selected_feat]
X_test=X_test[selected_feat]

df=pd.DataFrame(selected_feat)
df=df.rename(columns={0:'Attendance'})
savedfile=df.to_csv(savepath+'modelselect2.csv',index=False)

cols=len(X_train.columns)
mrresults=[]
for i in range(1,cols+1):
    print(i)
    result=[]
    result.append(i)
    forest = RandomForestRegressor(n_estimators=1000,criterion='mae',random_state=1,n_jobs=-1,max_features=i)
    forest.fit(X_train, y_train)
    y_train_pred = forest.predict(X_train)
    rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
    result.append(rmse_train)
    r2_train=r2_score(y_train, y_train_pred)
    result.append(r2_train)
    mapeTrain=mean_absolute_percentage_error(y_train,y_train_pred)
    result.append(mapeTrain)
    print('Train MAPE = '+str(mapeTrain))
    mrresults.append(result)
    
regResult=pd.DataFrame(mrresults)
regResult=regResult.rename(columns={0:'Features',1:'RMSE Train',2:'R2 Train',3:'Mape Train'})
regResult=regResult.set_index('Features')
#savedfile=regResult.to_csv(savepath+'Random Forest Attendance Feature Selection Results.csv',index=False)

plt.plot(regResult['Mape Train'],color='steelblue',label='Train MAPE')
plt.xlabel('Features')
plt.ylabel('MAPE')
#plt.title('Attendance - RF - MAPE')
plt.legend(loc='upper right')
plt.hlines(y=regResult['Mape Train'].min(), xmin=0, xmax=cols, color='red', lw=.5)
plt.xlim([0, cols])
plt.savefig(savepath+'Features vs Mape.jpeg')
plt.show()

minMape=regResult['Mape Train'].min()
minrow=regResult[(regResult['Mape Train']==minMape)]
minrow=minrow.reset_index()
minfeat=int(minrow['Features'])

forest = RandomForestRegressor(n_estimators=1000,criterion='mae',random_state=1,n_jobs=-1,max_features=38) #69
forest.fit(X_train, y_train)
y_train_pred = forest.predict(X_train)

rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
r2_train=r2_score(y_train, y_train_pred)
mapeTrain=mean_absolute_percentage_error(y_train,y_train_pred)
print(mapeTrain)
y_train_pred = forest.predict(X_train)
y_train2=pd.DataFrame(y_train.reset_index(drop=True))
prediction=pd.DataFrame(y_train_pred)
trainResults=y_train2.join(prediction)
trainResults=trainResults.rename(columns={0:'Prediction'})
trainResults['Attendance2']=10**trainResults['(log)Attendance']
trainResults['Prediction2']=10**trainResults['Prediction']
rmse_train=mean_squared_error(trainResults['Attendance2'], trainResults['Prediction2'],squared=False)
r2_train=r2_score(trainResults['Attendance2'] ,trainResults['Prediction2'])
mapetrain=mean_absolute_percentage_error(trainResults['Attendance2'],trainResults['Prediction2'])
print('train MAPE2 = '+str(mapetrain))
print(rmse_train)

mrresults2=['(log)Attendance Random Forest',rmse_train,rmse_test,r2_train,r2_test,mapeTrain,mapeTest]
regResult3=pd.DataFrame(mrresults2).T
regResult3=regResult3.rename(columns={0:'Model',1:'RMSE Train',2:'RMSE Test',3:'R2 Train',4:'R2 Test',5:'Mape Train',6:'Mape Test'})
savedfile=regResult3.to_csv(savepath+'(log)Attendance Random Forest Test.csv',index=False)

df=pd.DataFrame({'With VIF':mapeTrain}.items())
df=df.rename(columns={0:'Description',1:'(log)Attendance Random Forest'})
savedfile=df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif9.csv',index=False)

df=pd.DataFrame({'Without VIF':mapeTrain}.items())
df=df.rename(columns={0:'Description',1:'(log)Attendance Random Forest'})
savedfile=df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif10.csv',index=False)

feat_labels = X_train.columns
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]
print(importances[indices[8]])
for f in range(X_train.shape[1]): 
    print("%2d) %-*s %f" % (f + 1,43,
                            feat_labels[indices[f]],
                            importances[indices[f]]))
plt.title('Feature Importance')
plt.bar(range(X_train.shape[1]), importances[indices], align='center')
plt.xticks(range(X_train.shape[1]), feat_labels, rotation=90) 
plt.xlim([-1, X_train.shape[1]])

"""
Create a Dataframe of each result for plotting
"""
y_train2=pd.DataFrame(y_train.reset_index(drop=True))
prediction=pd.DataFrame(y_train_pred)
trainResults=y_train2.join(prediction)
trainResults=trainResults.rename(columns={0:'Prediction'})
trainResults['Error']=trainResults['Prediction']-trainResults['(log)Attendance']
trainResults['Squared Error']=trainResults['Error']*trainResults['Error']
trainResults['rse']=np.sqrt(trainResults['Squared Error'])
stdRes=trainResults['Error'].std()
meanRes=trainResults['Error'].mean()
trainResults['Std Error']=(trainResults['Error']-meanRes)/stdRes
stdRes=trainResults['rse'].std()
meanRes=trainResults['rse'].mean()
trainResults['Std rse']=(trainResults['rse']-meanRes)/stdRes
y_train_res=list(trainResults['Std rse'])
y_train_res2=list(trainResults['Std Error'])

#Scatter Plot of Residuals
plt.scatter(y_train_pred,  y_train_res2,
            c='steelblue', marker='o', edgecolor='white',
            label='Training data')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
#plt.title('(log) Attendance - RF - Residuals vs Fitted')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=3, xmax=5, color='black', lw=2)
plt.xlim([3, 5])
plt.savefig(savepath+'Plot the Residuals.jpeg')
plt.show()

#Histogram of Resuiduals
plt.hist(y_train_res2,color='steelblue',label='Train')
plt.xlabel('Standardized Residuals')
#plt.title('(log) Attendance - RF - Residuals')
plt.legend()
plt.show()

#QQ PLot of Residuals
trainres=np.array(y_train_res2)
fig = sm.qqplot(trainres,fit=True, line='45',
                c='steelblue', marker='o', 
                label='Training Residuals')
plt.ylabel('Standardized Residuals')
plt.legend(loc='upper left')
#plt.title('(log) Attendance - RF - Normal Q-Q')
plt.savefig(savepath+'QQPlot.jpeg')
plt.show()

_,p=shapiro(y_train_res2)
print(p)
if p>0.05:
    x="The residuals seem to come from Gaussian process"
else:
    x="The normality assumption may not hold"
pvalue=pd.DataFrame(['(log)Attendance Random Forest',p,x]).T
pvalue=pvalue.rename(columns={0:'Model',1:'p-value',2:'Interpretation'})
savedfile=pvalue.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue5.csv',index=False)

#Scale Loction
plot_lm_3 = plt.figure()
plt.scatter(y_train_pred, y_train_res, alpha=0.5,
            c='steelblue', marker='o', edgecolor='white',
            label='Training data');
sns.regplot(y_train_pred, y_train_res,
            scatter=False,
            ci=False,
            lowess=True,
            line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
#plot_lm_3.axes[0].set_title('(log) Attendance - RF - Scale-Location')
plot_lm_3.axes[0].set_xlabel('Fitted values')
plot_lm_3.axes[0].set_ylabel('$\sqrt{|Standardized Residuals|}$');
plt.savefig(savepath+'Normalised Scale Location.jpeg')

#Breuschpagan test
bp_test = het_breuschpagan(y_train_res, X_train)
labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
bp=(dict(zip(labels, bp_test)))
bp=pd.DataFrame(bp,index=[0])
bp['Model']='Attendance Regression'
bp.loc[(bp['F-Test p-value']<0.05),'Interpretation']='The Residuals seem to be Heteroskedastic'
bp.loc[(bp['F-Test p-value']>0.05),'Interpretation']='The Residuals seem to be Homoskedastic'
bp=bp[['Model','F-Test p-value','Interpretation']]
savedfile=bp.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp5.csv',index=False)

"""
Run Model on Test Data
"""

y_test_pred = forest.predict(X_test)
y_test2=pd.DataFrame(y_test.reset_index(drop=True))
prediction=pd.DataFrame(y_test_pred)
testResults=y_test2.join(prediction)
testResults=testResults.rename(columns={0:'Prediction'})
testResults['Attendance2']=10**testResults['(log)Attendance']
testResults['Prediction2']=10**testResults['Prediction']
rmse_test=mean_squared_error(testResults['Attendance2'], testResults['Prediction2'],squared=False)
r2_test=r2_score(testResults['Attendance2'] ,testResults['Prediction2'])
mapeTest=mean_absolute_percentage_error(testResults['Attendance2'],testResults['Prediction2'])
print('Test MAPE2 = '+str(mapeTest))
mrresults2=['(log)Attendance Random Forest',rmse_train,rmse_test,r2_train,r2_test,mapeTrain,mapeTest]
regResult3=pd.DataFrame(mrresults2).T
regResult3=regResult3.rename(columns={0:'Model',1:'RMSE Train',2:'RMSE Test',3:'R2 Train',4:'R2 Test',5:'Mape Train',6:'Mape Test'})
savedfile=regResult3.to_csv(savepath+'(log)Attendance Random Forest Test.csv',index=False)








