import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
from	sklearn.linear_model	import	LinearRegression
from sklearn.model_selection import train_test_split
#from	sklearn.	cross_validation	import	cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

data=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Final Data for Model.csv', encoding='latin')
columns=data.columns
for i in columns:
    print(i)    
df=data[['Round','Home Table Position','Away Table Position','Home Last_5_W/L','LastGame',\
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
        'Derby_Extra Derby','Derby_Non Derby','Game Competitiveness_Cant Qualify','Game Competitiveness_Has Qualified','Temperature_Mild','Temperature_Warm',\
        'Wind_Normal','Wind_Wild','Rain_Dry','Rain_Wet','Age of Stadium_New','Age of Stadium_Old','Win Probability Dummy_Uneven','Stadium Capacity','Attendance']]



#cols = ['Round','Attendance','Home Table Position','Away Table Position','Home Last_5_W/L',\
#        'LastGame','Away Last_5_W/L','Max Temperature','Rain Level','Wind Speed','Home Last_3_W/L',\
#        'Last Game in Comp','Home Win/Loss in Comp','Away Win/Loss in Comp','Home Total P','Day Of Week',\
#        'Month of Year','Home Winning Percentage','homeVSaway Winning Percentage','Number ofP14 Wins',\
#        'Number ofEPCR Wins','Years sinceP14 Win','Years sinceEPCR Win','Stadium Age','Table Difference',\
#        'Uncertainty','Sentiment','Win Probability']
#sns.pairplot(df[cols], size=2.5)
#plt.tight_layout()
#plt.show()

#cols2 = ['Round','Attendance','Home Table Position','Away Table Position','Home Last_5_W/L']
#sns.pairplot(df[cols2], size=2.5)
#plt.tight_layout()
#plt.show()


#cm = np.corrcoef(df[cols].values.T)
#sns.set(font_scale=1.5)
#fig, ax = plt.subplots(figsize=(45,30))
#hm = sns.heatmap(cm,cbar=True,annot=True,square=False,fmt='.2f',annot_kws={'size': 15},yticklabels=cols,xticklabels=cols,ax=ax)
#plt.show()
#plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/correlation Heat Map.png')
#
#cm = np.corrcoef(df[cols2].values.T)
#sns.set(font_scale=1.5)
#fig, ax = plt.subplots(figsize=(16,9))
#hm = sns.heatmap(cm,cbar=True,annot=True,square=False,fmt='.2f',annot_kws={'size': 15},yticklabels=cols2,xticklabels=cols2,ax=ax)
#plt.show()



#Model
X = df.iloc[:, :-1].values
y = df['Attendance'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#sc.fit(X_train)
#X_train_std = sc.transform(X_train)
#X_test_std = sc.transform(X_test)

slr=LinearRegression()
slr.fit(X_train,y_train)
y_train_pred=slr.predict(X_train)
y_test_pred=slr.predict(X_test)
#for i, prediction in enumerate(y_test_pred):
#    print('Predicted: %s. Target: %s' % (prediction, y_test[i]))
#print('R-squared: %.2f' % slr.score(X_test, y_test))



#Polynomial
#from	sklearn.preprocessing	import	PolynomialFeatures
#
#quadratic	=	PolynomialFeatures(degree=2)
#X_quad = quadratic.fit_transform(X_train)
#model.fit(X_quad, y_train)
#
#y_quad_fit = model.predict(quadratic.fit_transform(X_test))
#
#
#
#from sklearn.metrics import mean_squared_error
#from sklearn.metrics import r2_score
#y_quad_pred = model.predict(X_quad)
#print('Training MSE linear: %.3f, quadratic: %.3f' % (mean_squared_error(y_test, y_train_pred),mean_squared_error(y_test, y_quad_fit)))
#print('Training  R^2 linear: %.3f, quadratic: %.3f' % (r2_score(y_test, y_train_pred),r2_score(y_test, y_quad_fit)))


#Plot the Residuals

#plt.scatter(y_train_pred,  y_train_pred - y_train,
#            c='steelblue', marker='o', edgecolor='white',
#            label='Training data')
#plt.scatter(y_test_pred,  y_test_pred - y_test,
#            c='limegreen', marker='s', edgecolor='white',
#            label='Test data')
#plt.xlabel('Predicted values')
#plt.ylabel('Residuals')
#plt.legend(loc='upper left')
#plt.hlines(y=0, xmin=-10, xmax=70000, color='black', lw=2)
#plt.xlim([-10, 70000])
#plt.show()


print('MSE train: %.3f, test: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_test, y_test_pred)))
#"""
#All Features
#
#MSE train: 3354004.396, test: 7363332.360
#R^2 train: 0.962, test: 0.899
#"""
#

print('R^2 train: %.3f, test: %.3f' % (r2_score(y_train, y_train_pred), r2_score(y_test, y_test_pred)))

#Coefficients

#import statsmodels.api as sm
#from scipy import stats
#
#X2=sm.add_constant(X_train)
#est = sm.OLS(y_train, X2)
#est2 = est.fit()
#print(est2.summary())
#
######
#
#
#params = np.append(slr.intercept_,slr.coef_)
#
#newX = pd.DataFrame({"Constant":np.ones(len(X))}).join(pd.DataFrame(X))
#MSE = (sum((y_train-y_train_pred)**2))/(len(newX)-len(newX.columns))
#
## Note if you don't want to use a DataFrame replace the two lines above with
## newX = np.append(np.ones((len(X),1)), X, axis=1)
## MSE = (sum((y-y_train_pred)**2))/(len(newX)-len(newX[0]))
#
#var_b = MSE*(np.linalg.inv(np.dot(newX.T,newX)).diagonal())
#sd_b = np.sqrt(var_b)
#ts_b = params/ sd_b
#
#p_values =[2*(1-stats.t.cdf(np.abs(i),(len(newX)-1))) for i in ts_b]
#
#sd_b = np.round(sd_b,3)
#ts_b = np.round(ts_b,3)
#p_values = np.round(p_values,3)
#params = np.round(params,4)
#
#myDF3 = pd.DataFrame()
#myDF3["Coefficients"],myDF3["Standard Errors"],myDF3["t values"],myDF3["Probabilites"] = [params,sd_b,ts_b,p_values]
#print(myDF3)

########MODEL2

data=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Final Data for Model2.csv', encoding='latin')
    
df=data[['Round','Home Table Position','Away Table Position','Home Last_5_W/L','LastGame',\
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
        'Derby_Extra Derby','Derby_Non Derby','Game Competitiveness_Cant Qualify','Game Competitiveness_Has Qualified','Temperature_Mild','Temperature_Warm',\
        'Wind_Normal','Wind_Wild','Rain_Dry','Rain_Wet','Age of Stadium_New','Age of Stadium_Old','Win Probability Dummy_Uneven','Stadium Capacity','Stadium Percentage',]]

X = df.iloc[:, :-1].values
y = df['Stadium Percentage'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
slr=LinearRegression()
slr.fit(X_train,y_train)
y_train_pred=slr.predict(X_train)
y_test_pred=slr.predict(X_test)
print('MSE train: %.3f, test: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_test, y_test_pred)))
print('R^2 train: %.3f, test: %.3f' % (r2_score(y_train, y_train_pred), r2_score(y_test, y_test_pred)))
print(data['Stadium Percentage'].mean())








#########Random Forest

print(data['Stadium Percentage'].mean())
from sklearn.ensemble import RandomForestRegressor
forest = RandomForestRegressor(n_estimators=500,criterion='mse',random_state=1,n_jobs=-1)
forest.fit(X_train, y_train)
y_train_pred = forest.predict(X_train)
y_test_pred = forest.predict(X_test)
print('MSE train: %.3f, test: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_test, y_test_pred)))
print('R^2 train: %.3f, test: %.3f' % (r2_score(y_train, y_train_pred),r2_score(y_test, y_test_pred)))

plt.scatter(y_train_pred,y_train_pred - y_train,c='steelblue',edgecolor='white',marker='o', s=35,alpha=0.9,label='Training data')
plt.scatter(y_test_pred,y_test_pred - y_test, c='limegreen', edgecolor='white',  marker='s', s=35, alpha=0.9, label='Test data')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=0, xmax=100, lw=2, color='black')
plt.xlim([0, 100])
plt.show()

for i, prediction in enumerate(y_test_pred):
    print('Predicted: %s. Target: %s' % (prediction, y_test[i])+'      '+str(round(prediction-y_test[i],0)))
    #print('R-squared: %.2f' % slr.score(X_test, y_test))

#derby



#Feature Selection

from sklearn.feature_selection import RFE
rfe = RFE(forest, 100)
rfe = rfe.fit(X_train, y_train)
print(rfe.support_)
print(rfe.ranking_)
y_train_pred = rfe.predict(X_train)
y_test_pred = rfe.predict(X_test)
print('MSE train: %.3f, test: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_test, y_test_pred)))
print('R^2 train: %.3f, test: %.3f' % (r2_score(y_train, y_train_pred),r2_score(y_test, y_test_pred)))

plt.scatter(y_train_pred,y_train_pred - y_train,c='steelblue',edgecolor='white',marker='o', s=35,alpha=0.9,label='Training data')
plt.scatter(y_test_pred,y_test_pred - y_test, c='limegreen', edgecolor='white',  marker='s', s=35, alpha=0.9, label='Test data')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=0, xmax=1, lw=2, color='black')
plt.xlim([0, 1])
plt.show()