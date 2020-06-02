import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import statsmodels.api as sm
import seaborn as sns
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
plt.style.use('seaborn') # pretty matplotlib plots
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
multicollinearity_check(X)
y = dfAt['Attendance']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.16, random_state=1)

"""##########################
Set the mape def
"""
def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

"""#########################
Ordinary Least Squares of Model
"""

X2=sm.add_constant(X_train)
model = sm.OLS(y_train, X2)
model_fit = model.fit()
with open('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/OLS Summaryatt.csv', 'w') as fh:
    fh.write(model_fit.summary().as_csv())
with open('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/OLS Summaryatt.csv', 'w') as fh:
    fh.write(model_fit.summary().as_csv())
    
featurepvalue=['Home_Lst_3_Win','Tournament_Champions Cup','Home_Team_Benetton Treviso','Home_Team_Ospreys','Home_Team_Zebre Rugby','Away_Team_Scarlets',\
               'Venue_Irish Independent Park','Venue_RDS Arena','Venue_Thomond Park','Yrs_EPCR_Win_Four to Six','Yrs_EPCR_Win_Within Three','Derby_Extra Derby',\
                   'Derby_Non Derby','Kick_off_Hour_Evening','Stadium_Age_Dummy_New']
     
X_train2=X_train[featurepvalue]
X_test2=X_test[featurepvalue]
    
fpvalue=pd.DataFrame(featurepvalue)
savedfile=fpvalue.to_csv(savepath+'Regression Attendance pvalue.csv',index=False)

# cm = np.corrcoef(X_train2.values.T)
# corr=pd.DataFrame(cm)
# sns.set(font_scale=3)
# fig, ax = plt.subplots(figsize=(50,30))
# hm = sns.heatmap(cm,cbar=True,annot=True,square=False,fmt='.2f',annot_kws={'size': 35},yticklabels=featurepvalue,xticklabels=featurepvalue,ax=ax)
# plt.show()
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/correlation Heat Map Att.pdf')

mlr=linear_model.LinearRegression()
mlr.fit(X_train2,y_train)
y_train_pred=mlr.predict(X_train2)

rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
r2_train=r2_score(y_train, y_train_pred)
mapeTrain=mean_absolute_percentage_error(y_train,y_train_pred)

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
plt.style.use('seaborn') # pretty matplotlib plots
plt.rc('font', size=14)
plt.rc('figure', titlesize=18)
plt.rc('axes', labelsize=15)
plt.rc('axes', titlesize=18)
#Scatter Plot of Residuals
plt.scatter(y_train_pred,  y_train_res2,
            c='steelblue', marker='o', edgecolor='white',
            label='Training data')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
#plt.title('Attendance - Reg(p-value) - Residuals vs Fitted')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=0, xmax=50000, color='black', lw=2)
plt.xlim([0, 50000])
plt.savefig(savepath+'Plot the Residuals.jpeg')
plt.show()

#Histogram of Resuiduals
plt.hist(y_train_res2,color='steelblue',label='Train')
plt.xlabel('Standardized Residuals')
#plt.title('Attendance - Reg(p-value) - Residuals')
plt.legend()
plt.show()

#QQ PLot of Residuals
trainres=np.array(y_train_res2)
fig = sm.qqplot(trainres,fit=True, line='45',
                c='steelblue', marker='o', 
                label='Training Residuals')
plt.ylabel('Standardized Residuals')
plt.legend(loc='upper left')
#plt.title('Attendance - Reg(p-value) - Normal Q-Q')
plt.savefig(savepath+'QQPlot.jpeg')
plt.show()

_,p=shapiro(y_train_res2)
print(p)
if p>0.05:
    x="The residuals seem to come from Gaussian process"
else:
    x="The normality assumption may not hold"
pvalue=pd.DataFrame(['Attendance Regression (p-value)',p,x]).T
pvalue=pvalue.rename(columns={0:'Model',1:'p-value',2:'Interpretation'})
savedfile=pvalue.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue9.csv',index=False)

#Breuschpagan test
bp_test = het_breuschpagan(y_train_res, X_train2)
labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
bp=(dict(zip(labels, bp_test)))
bp=pd.DataFrame(bp,index=[0])
bp['Model']='Attendance - Reg(p-value)'
bp.loc[(bp['F-Test p-value']<0.05),'Interpretation']='The Residuals seem to be Heteroskedastic'
bp.loc[(bp['F-Test p-value']>0.05),'Interpretation']='The Residuals seem to be Homoskedastic'
bp=bp[['Model','F-Test p-value','Interpretation']]
savedfile=bp.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp9.csv',index=False)

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
#plot_lm_3.axes[0].set_title('Attendance - Reg(p-value) - Scale-Location')
plot_lm_3.axes[0].set_xlabel('Fitted values')
plot_lm_3.axes[0].set_ylabel('$\sqrt{|Standardized Residuals|}$');
plt.savefig(savepath+'Scale Location.jpeg')
plt.show()

"""
Run Model on Test Data
"""
y_test_pred = mlr.predict(X_test2)
rmse_test=mean_squared_error(y_test, y_test_pred,squared=False)
r2_test=r2_score(y_test, y_test_pred)
mapeTest=mean_absolute_percentage_error(y_test,y_test_pred)
print('Test MAPE = '+str(mapeTest))
df=pd.DataFrame(y_test).reset_index(drop=True)
df2=pd.DataFrame(y_test_pred)
df3=df.join(df2)
mrresults2=['Attendance Regression pvalue',rmse_train,rmse_test,r2_train,r2_test,mapeTrain,mapeTest]
regResult3=pd.DataFrame(mrresults2).T
regResult3=regResult3.rename(columns={0:'Model',1:'RMSE Train',2:'RMSE Test',3:'R2 Train',4:'R2 Test',5:'Mape Train',6:'Mape Test'})
savedfile=regResult3.to_csv(savepath+'Attendance Regression Test pvalue.csv',index=False)