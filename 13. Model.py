import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
from	sklearn.linear_model	import	LinearRegression
from sklearn.model_selection import train_test_split
#from	sklearn.	cross_validation	import	cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import math
import statsmodels.api as sm
from scipy import stats
from	sklearn.preprocessing	import	PolynomialFeatures
from sklearn.feature_selection import RFE

attenddata=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Final Data for Model.csv', encoding='latin')
attenddata['Attendance']=attenddata['Attendance'].apply(np.log10)

#plt.hist(attenddata['Attendance'])


dfAt=attenddata[['Round','Home Table Position','Away Table Position','Home Last_5_W/L','LastGame',\
        'Away Last_5_W/L','Max Temperature','Rain Level','Wind Speed','Home Last_3_W/L','Last Game in Comp',\
        'Home Win/Loss in Comp','Away Win/Loss in Comp','Home Total P','Day Of Week','Month of Year','Home Winning Percentage',\
        'homeVSaway Winning Percentage','Number ofP14 Wins','Number ofEPCR Wins','Years sinceP14 Win','Years sinceEPCR Win','Stadium Age',\
        'Table Difference','Uncertainty','Sentiment','Win Probability','Tournament_Champions Cup','Tournament_League',\
        'Home Team_Cardiff Blues','Home Team_Connacht Rugby','Home Team_Dragons','Home Team_Edinburgh Rugby','Home Team_Leinster Rugby',\
        'Home Team_Munster Rugby','Home Team_Ospreys','Home Team_Scarlets','Home Team_Ulster Rugby','Home Team_Zebre Rugby','Away Team_Agen',\
        'Away Team_Bath Rugby','Away Team_Bayonne','Away Team_Benetton Treviso','Away Team_Bordeaux-Begles','Away Team_Bristol Rugby','Away Team_Brive',\
        'Away Team_Cardiff Blues','Away Team_Castres Olympique','Away Team_Connacht Rugby','Away Team_Dragons','Away Team_Edinburgh Rugby',\
        'Away Team_Enisei-STM','Away Team_Exeter Chiefs','Away Team_Glasgow Warriors','Away Team_Gloucester Rugby','Away Team_Grenoble',\
        'Away Team_Harlequins','Away Team_Krasny Yar','Away Team_La Rochelle','Away Team_Leicester Tigers','Away Team_Leinster Rugby','Away Team_London Irish',\
        'Away Team_Lyon','Away Team_Montpellier','Away Team_Munster Rugby','Away Team_Newcastle Falcons','Away Team_Northampton Saints','Away Team_Ospreys',\
        'Away Team_Oyonnax','Away Team_Pau','Away Team_Perpignan','Away Team_RC Toulon','Away Team_Racing 92','Away Team_Rugby Calvisano','Away Team_Sale Sharks',\
        'Away Team_Saracens','Away Team_Scarlets','Away Team_Stade Francais Paris','Away Team_Timisoara Saracens','Away Team_Toulouse','Away Team_Ulster Rugby',\
        'Away Team_Wasps','Away Team_Worcester Warriors','Away Team_Zebre Rugby','Venue_BT Murrayfield','Venue_BT Murrayfield Stadium','Venue_Cardiff Arms Park',\
        'Venue_Constructaquote Stadium (Virginia Park)','Venue_Eugene Cross Park','Venue_Irish Independent Park','Venue_Kingspan Stadium','Venue_La Ghirada',\
        'Venue_Liberty Stadium','Venue_Meggetland','Venue_Morganstone Brewery Field','Venue_Myreside','Venue_Parc y Scarlets','Venue_Principality Stadium',\
        'Venue_RDS Arena','Venue_Rodney Parade','Venue_Sportsground','Venue_Stadio Comunale di Monigo','Venue_Stadio Monigo','Venue_Stadio Sergio Lanfranchi',\
        'Venue_Stadio Tommaso Fattori','Venue_Stadio Zaffanella','Venue_The Sportsground','Venue_Thomond Park','Kick Off Hour_Early','Kick Off Hour_Evening',\
        'Derby_Extra Derby','Derby_Non Derby','Game Competitiveness_Cant Qualify','Game Competitiveness_Has Qualified','Away Country_Ireland','Away Country_Italy','Away Country_Scotland','Away Country_Wales','Temperature_Mild','Temperature_Warm',\
        'Wind_Normal','Wind_Wild','Rain_Dry','Rain_Wet','Age of Stadium_New','Age of Stadium_Old','Win Probability Dummy_Uneven','Stadium Capacity','Attendance']]

#attcols=['Attendance','Home Last_5_W/L','Home Last_3_W/L','Away Last_5_W/L','Away Win/Loss in Comp','Wind Speed',\
#                       'Home Winning Percentage','Uncertainty','Number ofP14 Wins','Years sinceP14 Win','Number ofEPCR Wins','Years sinceEPCR Win',\
#                       'Home Team_Cardiff Blues','Venue_Cardiff Arms Park','Home Team_Connacht Rugby','Venue_Sportsground','Home Team_Dragons',\
#                       'Venue_Rodney Parade','Home Team_Leinster Rugby','Venue_RDS Arena','Home Team_Munster Rugby','Venue_Thomond Park','Home Team_Ospreys',\
#                       'Venue_Liberty Stadium','Home Team_Ulster Rugby','Age of Stadium_New','Home Team_Zebre Rugby','Venue_Stadio Sergio Lanfranchi',\
#                       'Venue_Kingspan Stadium','Age of Stadium_New']
#cm = np.corrcoef(dfAt[attcols].values.T)
dfAt=dfAt.drop(columns=['Home Last_3_W/L','Away Last_5_W/L','Wind Speed','Uncertainty','Years sinceP14 Win','Number ofEPCR Wins',\
                        'Venue_Cardiff Arms Park','Venue_Sportsground','Home Team_Dragons','Venue_RDS Arena','Home Team_Munster Rugby',\
                        'Home Team_Ospreys','Venue_Stadio Sergio Lanfranchi','Age of Stadium_New'])

#'Away Team_Agen',\
#        'Away Team_Bath Rugby','Away Team_Bayonne','Away Team_Benetton Treviso','Away Team_Bordeaux-Begles','Away Team_Bristol Rugby','Away Team_Brive',\
#        'Away Team_Cardiff Blues','Away Team_Castres Olympique','Away Team_Connacht Rugby','Away Team_Dragons','Away Team_Edinburgh Rugby',\
#        'Away Team_Enisei-STM','Away Team_Exeter Chiefs','Away Team_Glasgow Warriors','Away Team_Gloucester Rugby','Away Team_Grenoble',\
#        'Away Team_Harlequins','Away Team_Krasny Yar','Away Team_La Rochelle','Away Team_Leicester Tigers','Away Team_Leinster Rugby','Away Team_London Irish',\
#        'Away Team_Lyon','Away Team_Montpellier','Away Team_Munster Rugby','Away Team_Newcastle Falcons','Away Team_Northampton Saints','Away Team_Ospreys',\
#        'Away Team_Oyonnax','Away Team_Pau','Away Team_Perpignan','Away Team_RC Toulon','Away Team_Racing 92','Away Team_Rugby Calvisano','Away Team_Sale Sharks',\
#        'Away Team_Saracens','Away Team_Scarlets','Away Team_Stade Francais Paris','Away Team_Timisoara Saracens','Away Team_Toulouse','Away Team_Ulster Rugby',\
#        'Away Team_Wasps','Away Team_Worcester Warriors','Away Team_Zebre Rugby',





#Model 1 Multiple Regression  on Attendance

X = dfAt.iloc[:, :-1].values
y = dfAt['Attendance'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=1)
y_train_avg=np.mean(y_train)
y_val_avg=np.mean(y_val)
slr=LinearRegression()
slr.fit(X_train,y_train)
y_train_pred=slr.predict(X_train)
y_val_pred=slr.predict(X_val)
print('MSE train: %.3f, val: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_val, y_val_pred)))
print('R^2 train: %.3f, val: %.3f' % (r2_score(y_train, y_train_pred), r2_score(y_val, y_val_pred)))
train_error=math.sqrt(mean_squared_error(y_train, y_train_pred))
val_error=math.sqrt(mean_squared_error(y_val, y_val_pred))
MeaTrain=train_error/y_train_avg
Meaval=val_error/y_val_avg
print('Train MAPE = '+str(MeaTrain))
print('Val MAPE = '+str(Meaval))

plt.scatter(y_train_pred,  y_train_pred - y_train,
            c='steelblue', marker='o', edgecolor='white',
            label='Training data')
plt.scatter(y_val_pred,  y_val_pred - y_val,
            c='limegreen', marker='s', edgecolor='white',
            label='val data')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=2.5, xmax=5, color='black', lw=2)
plt.xlim([2.5, 5])
plt.show()

#X2=sm.add_constant(X_train)
#est = sm.OLS(y_train, X2)
#est2 = est.fit()
#print(est2.summary())
#params = np.append(slr.intercept_,slr.coef_)
#newX = pd.DataFrame({"Constant":np.ones(len(X))}).join(pd.DataFrame(X).reset_index(drop=True))
##newX = pd.DataFrame({"Constant":np.ones(len(X))}).join(pd.DataFrame(X))
#MSE = (sum((y_train-y_train_pred)**2))/(len(newX)-len(newX.columns))
#var_b = MSE*(np.linalg.inv(np.dot(newX.T,newX)).diagonal())
#sd_b = np.sqrt(var_b)
#ts_b = params/ sd_b
#p_values =[2*(1-stats.t.cdf(np.abs(i),(len(newX)-1))) for i in ts_b]
#sd_b = np.round(sd_b,3)
#ts_b = np.round(ts_b,3)
#p_values = np.round(p_values,3)
#params = np.round(params,4)
#myDF3 = pd.DataFrame()
#myDF3["Coefficients"],myDF3["Standard Errors"],myDF3["t values"],myDF3["Probabilites"] = [params,sd_b,ts_b,p_values]
#print(myDF3)





#Model 3 Random Forest on Attendance

X = dfAt.iloc[:, :-1].values
y = dfAt['Attendance'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=1)
y_train_avg=np.mean(y_train)
y_val_avg=np.mean(y_val)
forest = RandomForestRegressor(n_estimators=500,criterion='mse',random_state=1,n_jobs=-1)
forest.fit(X_train, y_train)
y_train_pred = forest.predict(X_train)
y_val_pred = forest.predict(X_val)
print('MSE train: %.3f, val: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_val, y_val_pred)))
print('R^2 train: %.3f, val: %.3f' % (r2_score(y_train, y_train_pred), r2_score(y_val, y_val_pred)))
train_error=math.sqrt(mean_squared_error(y_train, y_train_pred))
val_error=math.sqrt(mean_squared_error(y_val, y_val_pred))
MeaTrain=train_error/y_train_avg
Meaval=val_error/y_val_avg
print('Train MAPE = '+str(MeaTrain))
print('val MAPE = '+str(Meaval))

plt.scatter(y_train_pred,y_train_pred - y_train,c='steelblue',edgecolor='white',marker='o', s=35,alpha=0.9,label='Training data')
plt.scatter(y_val_pred,y_val_pred - y_val, c='limegreen', edgecolor='white',  marker='s', s=35, alpha=0.9, label='val data')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=2.5, xmax=5, lw=2, color='black')
plt.xlim([2.5, 5])
plt.show()


  
X = dfAt.iloc[:, :-1].values
y = dfAt['Attendance'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=1)
y_train_avg=np.mean(y_train)
y_val_avg=np.mean(y_val)

results=[]
for i in range(1,114):
    result=[]
    rfe = RFE(forest, i)
    rfe = rfe.fit(X_train, y_train)
    y_train_pred = rfe.predict(X_train)
    y_val_pred = rfe.predict(X_val)
    mse_train=mean_squared_error(y_train, y_train_pred)
    result.append(mse_train)
    mse_val=mean_squared_error(y_val, y_val_pred)
    result.append(mse_val)
    r2_train=r2_score(y_train, y_train_pred)
    result.append(r2_train)
    r2_val=r2_score(y_val, y_val_pred)
    result.append(r2_val)
    print('MSE train: %.3f, val: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_val, y_val_pred)))
    print('R^2 train: %.3f, val: %.3f' % (r2_score(y_train, y_train_pred),r2_score(y_val, y_val_pred)))
    train_error=math.sqrt(mean_squared_error(y_train, y_train_pred))
    val_error=math.sqrt(mean_squared_error(y_val, y_val_pred))
    MeaTrain=train_error/y_train_avg
    Meaval=val_error/y_val_avg
    result.append(MeaTrain)
    result.append(Meaval)
    print('Train MAPE = '+str(MeaTrain))
    print('val MAPE = '+str(Meaval))
    results.append(result)
#
#plt.scatter(y_train_pred,y_train_pred - y_train,c='steelblue',edgecolor='white',marker='o', s=35,alpha=0.9,label='Training data')
#plt.scatter(y_test_pred,y_test_pred - y_test, c='limegreen', edgecolor='white',  marker='s', s=35, alpha=0.9, label='Test data')
#plt.xlabel('Predicted values')
#plt.ylabel('Residuals')
#plt.legend(loc='upper left')
#plt.hlines(y=0, xmin=2.5, xmax=1, lw=2, color='black')
#plt.xlim([0, 1])
#plt.show()
# 
#from itertools import combinations
#x=[1,2,3,4,5,6,7]
#for i in combinations(x,r=7):
#    print(i)
