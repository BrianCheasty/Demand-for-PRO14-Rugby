import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import statsmodels.api as sm
from sklearn.feature_selection import RFE
import seaborn as sns
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
plt.style.use('seaborn')
plt.rc('font', size=14)
plt.rc('figure', titlesize=18)
plt.rc('axes', labelsize=15)
plt.rc('axes', titlesize=18)


"""#########################
IMPORT THE GAME DATA
"""
dfAt=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Attendance Data.csv',\
                 encoding='latin')
savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Attendance Regression Model/'

"""
Multicollinearity
"""
def multicollinearity_check(X, thresh=10.0):
    data_type = X.dtypes
    # print(type(data_type))
    int_cols = \
    X.select_dtypes(include=['int', 'int16', 'int32', 'int64', 'float', 'float16', 'float32', 'float64']).shape[1]
    total_cols = X.shape[1]
    try:
        if int_cols != total_cols:
            raise Exception('All the columns should be integer or float, for multicollinearity test.')
        else:
            variables = list(range(X.shape[1]))
            dropped = True
            print('''\n\nThe VIF calculator will now iterate through the features and calculate their respective values.
            It shall continue dropping the highest VIF features until all the features have VIF less than the threshold of 5.\n\n''')
            while dropped:
                dropped = False
                vif = [variance_inflation_factor(X.iloc[:, variables].values, ix) for ix in variables]
                print('\n\nvif is: ', vif)
                maxloc = vif.index(max(vif))
                if max(vif) > thresh:
                    print('dropping \'' + X.iloc[:, variables].columns[maxloc] + '\' at index: ' + str(maxloc))
                    # del variables[maxloc]
                    X.drop(X.columns[variables[maxloc]], 1, inplace=True)
                    variables = list(range(X.shape[1]))
                    dropped = True

            print('\n\nRemaining variables:\n')
            print(X.columns[variables])
            # return X.iloc[:,variables]
            return X
    except Exception as e:
        print('Error caught: ', e)

"""########################
Set the Training, Validate and Test Data
"""
X = dfAt.iloc[:, :-1]
#multicollinearity_check(X)
y = dfAt['Attendance']
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
#plt.xlabel('Train and Test Set')
#plt.title('Attendance Distribution Split')
plt.legend()
plt.show()

"""##########################
Model 1 Multiple Regression  on Attendance
"""
mlr=linear_model.LinearRegression()
mlr.fit(X_train,y_train)
y_train_pred=mlr.predict(X_train)

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
savedfile=regResult1.to_csv(savepath+'Attendance Regression.csv',index=False)

"""
Review the MAPE of each Team
"""
train=X_train.join(y_train, how ='outer')
train=train.reset_index(drop=True)
y_train_pred2=pd.DataFrame(y_train_pred)
trainidate=train.join(y_train_pred2, how ='outer')
trainidate=trainidate.rename(columns={0:'Predicted'})
trainidate['APE']=np.sqrt((((trainidate['Attendance']-trainidate['Predicted'])/trainidate['Attendance'])*100)**2)
team=['Home_Team_Benetton Treviso','Home_Team_Cardiff Blues','Home_Team_Connacht Rugby',\
      'Home_Team_Dragons','Home_Team_Ospreys','Home_Team_Scarlets','Home_Team_Ulster Rugby','Home_Team_Zebre Rugby',\
          'Venue_Aviva Stadium','Venue_Irish Independent Park','Venue_RDS Arena','Venue_Myreside','Venue_Thomond Park','Venue_BT Murrayfield']
teamMAPE=[]
for i in team:
    df=trainidate[[i,'Attendance','Predicted']]
    df=df[(df[i]==1)]
    mape=mean_absolute_percentage_error(df['Attendance'],df['Predicted'])
    x=[{i:mape}]
    x=pd.DataFrame(x).T
    teamMAPE.append(x)
mapeDF=pd.concat(teamMAPE)
mapeDF=mapeDF.rename(columns={0:'Regression - Attendance'})
savedfile=mapeDF.to_csv(savepath+'Attendance RegressionMAPE.csv')
df=trainidate[(trainidate['APE']>mapeTrain)]
savedfile=df.to_csv(savepath+'highMAPE1.csv')

"""##########################
Feature Selection
"""
cols=len(X_train.columns)
mrresults=[]
for i in range(1,cols+1):
    print(i)
    result=[]
    result.append(i)
    rfe = RFE(mlr, i)
    rfe = rfe.fit(X_train, y_train)
    y_train_pred = rfe.predict(X_train)
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
savedfile=regResult.to_html(savepath+'Regression Attendance Feature Selection Results.csv')

plt.plot(regResult['Mape Train'],color='steelblue',label='Train MAPE')
plt.xlabel('Features')
plt.ylabel('MAPE')
#plt.title('Attendance - Reg - MAPE')
plt.legend(loc='upper right')
plt.hlines(y=regResult['Mape Train'].min(), xmin=0, xmax=cols, color='red', lw=.5)
plt.xlim([0, cols])
plt.savefig(savepath+'Regression Attendance Features vs Mape.jpeg')
plt.show()

rfe = RFE(mlr, 1)
rfe = rfe.fit(X_train, y_train)
ranking=rfe.ranking_
ranks=pd.DataFrame(ranking)
ranks=ranks.rename(columns={0:'Ranking'})
features=pd.DataFrame(X_train.columns)
features=features.rename(columns={0:'Features'})
featureRanks=ranks.join(features,how='outer')
featureRanks=featureRanks[(featureRanks['Ranking']< 20)]
savedfile=featureRanks.to_csv(savepath+'Regression Attendance Feature Selection Rankings.csv',index=False)

featureslist=list(featureRanks['Features'])
X_train2=X_train[featureslist]

                  
minMape=regResult['Mape Train'].min()
minrow=regResult[(regResult['Mape Train']==minMape)]
minrow=minrow.reset_index()
minfeat=int(minrow['Features'])                  
rfe = RFE(mlr, minfeat) #
rfe = rfe.fit(X_train, y_train)
y_train_pred = rfe.predict(X_train)

rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
r2_train=r2_score(y_train, y_train_pred)
mapeTrain=mean_absolute_percentage_error(y_train,y_train_pred)
print(mapeTrain)
df=pd.DataFrame({'With VIF':mapeTrain}.items())
df=df.rename(columns={0:'Description',1:'Attendance Regression'})
savedfile=df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif1.csv',index=False)

df=pd.DataFrame({'Without VIF':mapeTrain}.items())
df=df.rename(columns={0:'Description',1:'Attendance Regression'})
savedfile=df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif2.csv',index=False)

"""
Create a Dataframe of each result for plotting
"""
y_train2=pd.DataFrame(y_train.reset_index(drop=True))
prediction=pd.DataFrame(y_train_pred)
trainResults=y_train2.join(prediction)
trainResults=trainResults.rename(columns={0:'Prediction'})
trainResults['Error']=trainResults['Prediction']-trainResults['Attendance']
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

"""########################
Plot the Model
"""
plt.scatter(y_train_pred,  y_train_res2,
            c='steelblue', marker='o', edgecolor='white',
            label='Training data')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
#plt.title('Attendance - Reg - Residuals vs Fitted')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=0, xmax=50000, color='black', lw=2)
plt.xlim([0, 50000])
plt.savefig(savepath+'Plot the Residuals.jpeg')
plt.show()

#Histogram of Resuiduals
plt.hist(y_train_res2,color='steelblue',label='Train')
plt.xlabel('Standardized Residuals')
#plt.title('Attendance - Reg - Residuals')
plt.legend()
plt.show()

#QQ PLot of Residuals
trainres=np.array(y_train_res2)
fig = sm.qqplot(trainres,fit=True, line='45',
                c='steelblue', marker='o', 
                label='Training Residuals')
plt.ylabel('Standardized Residuals')
plt.legend(loc='upper left')
#plt.title('Attendance - Reg - Normal Q-Q')
plt.savefig(savepath+'QQPlot.jpeg')
plt.show()

_,p=shapiro(y_train_res2)
print(p)
if p>0.05:
    x="The residuals seem to come from Gaussian process"
else:
    x="The normality assumption may not hold"
pvalue=pd.DataFrame(['Attendance Regression',p,x]).T
pvalue=pvalue.rename(columns={0:'Model',1:'p-value',2:'Interpretation'})
savedfile=pvalue.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue1.csv',index=False)

#Breuschpagan test
bp_test = het_breuschpagan(y_train_res, X_train2)
labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
bp=(dict(zip(labels, bp_test)))
bp=pd.DataFrame(bp,index=[0])
bp['Model']='Attendance Regression'
bp.loc[(bp['F-Test p-value']<0.05),'Interpretation']='The Residuals seem to be Heteroskedastic'
bp.loc[(bp['F-Test p-value']>0.05),'Interpretation']='The Residuals seem to be Homoskedastic'
bp=bp[['Model','F-Test p-value','Interpretation']]
savedfile=bp.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp1.csv',index=False)

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
#plot_lm_3.axes[0].set_title('Attendance - Reg - Scale-Location')
plot_lm_3.axes[0].set_xlabel('Fitted values')
plot_lm_3.axes[0].set_ylabel('$\sqrt{|Standardized Residuals|}$');
plt.savefig(savepath+'Scale Location.jpeg')
plt.show()

"""
Run Model on Test Data
"""
y_test_pred = rfe.predict(X_test)
rmse_test=mean_squared_error(y_test, y_test_pred,squared=False)
r2_test=r2_score(y_test, y_test_pred)
mapeTest=mean_absolute_percentage_error(y_test,y_test_pred)
print('Test MAPE2 = '+str(mapeTest))
df=pd.DataFrame(y_test).reset_index(drop=True)
df2=pd.DataFrame(y_test_pred)
df3=df.join(df2)
mrresults2=['Attendance Regression',rmse_train,rmse_test,r2_train,r2_test,mapeTrain,mapeTest]
regResult3=pd.DataFrame(mrresults2).T
regResult3=regResult3.rename(columns={0:'Model',1:'RMSE Train',2:'RMSE Test',3:'R2 Train',4:'R2 Test',5:'Mape Train',6:'Mape Test'})
savedfile=regResult3.to_csv(savepath+'Attendance Regression Test.csv',index=False)


