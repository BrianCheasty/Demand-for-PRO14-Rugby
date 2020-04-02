import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
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
plt.style.use('seaborn') # pretty matplotlib plots
plt.rc('font', size=14)
plt.rc('figure', titlesize=18)
plt.rc('axes', labelsize=15)
plt.rc('axes', titlesize=18)

attenddata=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Final Data for Model.csv', encoding='latin')
attenddata.info()
columns=attenddata.columns
for i in columns:
    print(i)
attcols=['Round','Home Table Position','Away Table Position','Home Last_5_W/L','LastGame','Away Last_5_W/L','Max Temperature',\
         'Rain Level','Wind Speed','Home Last_3_W/L','Last Game in Comp','Home Win/Loss in Comp','Away Win/Loss in Comp','Home Total P',\
             'Day Of Week','Month of Year','Home Winning Percentage','homeVSaway Winning Percentage','Number ofP14 Wins','Number ofEPCR Wins',\
                 'Years sinceP14 Win','Years sinceEPCR Win','Stadium Age','Stadium Capacity','Table Difference','Uncertainty','Sentiment',\
                     'Win Probability','Tournament_Challenge Cup','Tournament_Champions Cup','Tournament_League','Home Team_Benetton Treviso',\
                         'Home Team_Cardiff Blues','Home Team_Connacht Rugby','Home Team_Dragons','Home Team_Edinburgh Rugby','Home Team_Leinster Rugby',\
                             'Home Team_Munster Rugby','Home Team_Ospreys','Home Team_Scarlets','Home Team_Ulster Rugby','Home Team_Zebre Rugby',\
                                 'Away Team_ASM Clermont Auvergne','Away Team_Agen','Away Team_Bath Rugby','Away Team_Bayonne','Away Team_Benetton Treviso',\
                                     'Away Team_Bordeaux-Begles','Away Team_Bristol Rugby','Away Team_Brive','Away Team_Cardiff Blues','Away Team_Castres Olympique',\
                                         'Away Team_Connacht Rugby','Away Team_Dragons','Away Team_Edinburgh Rugby','Away Team_Enisei-STM','Away Team_Exeter Chiefs',\
                                             'Away Team_Glasgow Warriors','Away Team_Gloucester Rugby','Away Team_Grenoble','Away Team_Harlequins','Away Team_Krasny Yar',\
                                                 'Away Team_La Rochelle','Away Team_Leicester Tigers','Away Team_Leinster Rugby','Away Team_London Irish','Away Team_Lyon',\
                                                     'Away Team_Montpellier','Away Team_Munster Rugby','Away Team_Newcastle Falcons','Away Team_Northampton Saints','Away Team_Ospreys',\
                                                         'Away Team_Oyonnax','Away Team_Pau','Away Team_Perpignan','Away Team_RC Toulon','Away Team_Racing 92','Away Team_Rugby Calvisano',\
                                                             'Away Team_Sale Sharks','Away Team_Saracens','Away Team_Scarlets','Away Team_Stade Francais Paris','Away Team_Timisoara Saracens',\
                                                                 'Away Team_Toulouse','Away Team_Ulster Rugby','Away Team_Wasps','Away Team_Worcester Warriors','Away Team_Zebre Rugby',\
                                                                     'Venue_Aviva Stadium','Venue_Cardiff Arms Park','Venue_Constructaquote Stadium (Virginia Park)','Venue_Eugene Cross Park',\
                                                                         'Venue_Irish Independent Park','Venue_Kingspan Stadium','Venue_La Ghirada','Venue_Liberty Stadium','Venue_Meggetland',\
                                                                             'Venue_Morganstone Brewery Field','Venue_Myreside','Venue_Parc y Scarlets','Venue_Principality Stadium','Venue_RDS Arena',\
                                                                                 'Venue_Rodney Parade','Venue_Sportsground','Venue_Stadio Monigo','Venue_Stadio Sergio Lanfranchi','Venue_Stadio Tommaso Fattori',\
                                                                                     'Venue_Stadio Zaffanella','Venue_The Sportsground','Venue_Thomond Park','Venue_Venue_BT Murrayfield','Venue_Venue_Stadio Monigo',\
                                                                                         'Kick Off Hour_Afternoon','Kick Off Hour_Early','Kick Off Hour_Evening','Derby_Derby','Derby_Extra Derby','Derby_Non Derby',\
                                                                                             'Game Competitiveness_Can Still Qualify','Game Competitiveness_Cant Qualify','Game Competitiveness_Has Qualified','Away Country_EngFra',\
                                                                                                 'Away Country_Ireland','Away Country_Italy','Away Country_Scotland','Away Country_Wales','Temperature_Cold','Temperature_Mild',\
                                                                                                     'Temperature_Warm','Wind_Calm','Wind_Normal','Wind_Wild','Rain_Damp','Rain_Dry','Rain_Wet','Age of Stadium_Middle Age','Age of Stadium_New',\
                                                                                                         'Age of Stadium_Old','Win Probability Dummy_Even','Win Probability Dummy_Uneven','Win Prob Squared','Attendance']

counter=0
for i in attcols:
    print(str(counter)+'  '+i)
    counter+=1
    
        
#pairplots=sns.pairplot(attenddata[attcols], size=2.5)
#plt.tight_layout()
#plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/Scatter Plot Matrix ATT.png')
#plt.close()


attcols2 = ['Round','Attendance','Home Table Position','Away Table Position','Home Last_5_W/L']
sns.pairplot(attenddata[attcols2], size=2.5)
plt.tight_layout()
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/Mini Scatter Plot Matrix ATT.png')
plt.close()


cm = np.corrcoef(attenddata[attcols].values.T)
corr=pd.DataFrame(cm)
#sns.set(font_scale=1.5)
#fig, ax = plt.subplots(figsize=(500,300))
#hm = sns.heatmap(cm,cbar=True,annot=True,square=False,fmt='.2f',annot_kws={'size': 15},yticklabels=attcols,xticklabels=attcols,ax=ax)
#plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/correlation Heat Map Att.pdf')
#plt.close()


corrdfs=[]
for i in range(0,141):
    corr80=corr[(corr[i]>.8)|(corr[i]<-.8)]
    corrdfs.append(corr80)
corrdf2=[]
for i in corrdfs:
    if len(i)>1:
        corrdf2.append(i)
    else:
        continue
corr80all=pd.concat(corrdfs)
for i in range(0,141):
    	corr80all.loc[(corr80all[i]>-0.8)&(corr80all[i]<0.8),i]=np.nan
        
for i in range(0,141):
    	corr80all.loc[(corr80all[i]>0.99),i]=np.nan
        
corr80all2=corr80all.dropna(how='all',axis=1)
corr80all2=corr80all2.drop_duplicates()



attenddata2=attenddata[['Round','Home Table Position','Away Table Position','Home Last_5_W/L','LastGame','Away Last_5_W/L','Max Temperature',\
                        'Rain Level','Wind Speed','Last Game in Comp','Home Win/Loss in Comp','Home Total P',\
                            'Day Of Week','Month of Year','Home Winning Percentage','homeVSaway Winning Percentage','Number ofP14 Wins',\
                                'Years sinceEPCR Win','Stadium Age','Stadium Capacity','Table Difference','Sentiment',\
                                    'Win Probability','Tournament_Champions Cup','Tournament_League','Home Team_Benetton Treviso',\
                                        'Home Team_Cardiff Blues','Home Team_Connacht Rugby','Home Team_Dragons','Home Team_Edinburgh Rugby','Home Team_Leinster Rugby',\
                                            'Home Team_Scarlets','Home Team_Ulster Rugby','Home Team_Zebre Rugby',\
                                                'Venue_Aviva Stadium','Venue_Constructaquote Stadium (Virginia Park)','Venue_Eugene Cross Park',\
                                                    'Venue_Irish Independent Park','Venue_Kingspan Stadium','Venue_La Ghirada','Venue_Liberty Stadium','Venue_Meggetland',\
                                                        'Venue_Morganstone Brewery Field','Venue_Myreside','Venue_Parc y Scarlets','Venue_Principality Stadium',\
                                                            'Venue_Stadio Sergio Lanfranchi','Venue_Stadio Tommaso Fattori',\
                                                                'Venue_Stadio Zaffanella','Venue_The Sportsground','Venue_Thomond Park','Venue_Venue_Stadio Monigo',\
                                                                    'Kick Off Hour_Afternoon','Kick Off Hour_Early','Derby_Derby','Derby_Extra Derby',\
                                                                        'Game Competitiveness_Cant Qualify','Game Competitiveness_Has Qualified',\
                                                                            'Away Country_Ireland','Away Country_Italy','Away Country_Scotland','Away Country_Wales','Temperature_Cold',\
                                                                                'Temperature_Warm','Wind_Calm','Wind_Normal','Rain_Damp','Rain_Wet','Age of Stadium_Middle Age',\
                                                                                    'Age of Stadium_Old','Win Probability Dummy_Even','Win Prob Squared',\
                                                                                        'Attendance']]


savedfile=attenddata2.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Attendance Data.csv', index=False)

logattend=attenddata2.copy()
logattend['Attendance']=logattend['Attendance'].apply(np.log10)

attendsp=attenddata2.copy()
attendsp['Stadium Percentage']=attendsp['Attendance']/attendsp['Stadium Capacity']

attendsp=attendsp[['Round','Home Table Position','Away Table Position','Home Last_5_W/L','LastGame','Away Last_5_W/L','Max Temperature',\
                        'Rain Level','Wind Speed','Last Game in Comp','Home Win/Loss in Comp','Home Total P',\
                            'Day Of Week','Month of Year','Home Winning Percentage','homeVSaway Winning Percentage','Number ofP14 Wins',\
                                'Years sinceEPCR Win','Stadium Age','Table Difference','Sentiment',\
                                    'Win Probability','Tournament_Champions Cup','Tournament_League','Home Team_Benetton Treviso',\
                                        'Home Team_Cardiff Blues','Home Team_Connacht Rugby','Home Team_Dragons','Home Team_Edinburgh Rugby','Home Team_Leinster Rugby',\
                                            'Home Team_Scarlets','Home Team_Ulster Rugby','Home Team_Zebre Rugby',\
                                                'Venue_Aviva Stadium','Venue_Constructaquote Stadium (Virginia Park)','Venue_Eugene Cross Park',\
                                                    'Venue_Irish Independent Park','Venue_Kingspan Stadium','Venue_La Ghirada','Venue_Liberty Stadium','Venue_Meggetland',\
                                                        'Venue_Morganstone Brewery Field','Venue_Myreside','Venue_Parc y Scarlets','Venue_Principality Stadium',\
                                                            'Venue_Stadio Sergio Lanfranchi','Venue_Stadio Tommaso Fattori',\
                                                                'Venue_Stadio Zaffanella','Venue_The Sportsground','Venue_Thomond Park','Venue_Venue_Stadio Monigo',\
                                                                    'Kick Off Hour_Afternoon','Kick Off Hour_Early','Derby_Derby','Derby_Extra Derby',\
                                                                        'Game Competitiveness_Cant Qualify','Game Competitiveness_Has Qualified',\
                                                                            'Away Country_Ireland','Away Country_Italy','Away Country_Scotland','Away Country_Wales','Temperature_Cold',\
                                                                                'Temperature_Warm','Wind_Calm','Wind_Normal','Rain_Damp','Rain_Wet','Age of Stadium_Middle Age',\
                                                                                    'Age of Stadium_Old','Win Probability Dummy_Even','Win Prob Squared',\
                                                                                        'Stadium Percentage']]
    
logspattend=attendsp.copy()
logspattend['Stadium Percentage']=logspattend['Stadium Percentage'].apply(np.log10)

# attenddata2 = df with attendance
plt.hist(attenddata2['Attendance'],color='steelblue')
plt.xlabel('Attendance')
plt.ylabel('Quantity of Games')
plt.title('Distribution of Attendance')
plt.hlines(y=0, xmin=0, xmax=70000, color='black', lw=2)
plt.xlim([0, 70000])
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Distribution of Standard Attendance.jpeg')
plt.show()

X = attenddata2.iloc[:, :-1]
y = attenddata2['Attendance']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=1)
y_train_avg=np.mean(y_train)
y_val_avg=np.mean(y_val)
y_test_avg=np.mean(y_test)
mlr=linear_model.LinearRegression()
mlr.fit(X_train,y_train)
y_train_pred=mlr.predict(X_train)
y_val_pred=mlr.predict(X_val)
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

# logattend = df with log attendance
savedfile=logattend.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/(log)Attendance Data.csv', index=False)

plt.hist(logattend['Attendance'],color='steelblue')
plt.xlabel('Attendance')
plt.ylabel('Quantity of Games')
plt.title('Distribution of (log)Attendance')
plt.hlines(y=0, xmin=6, xmax=12, color='black', lw=2)
plt.xlim([6, 12])
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Distribution of (log)Attendance.jpeg')
plt.show()

X = logattend.iloc[:, :-1]
y = logattend['Attendance']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=1)
y_train_avg=np.mean(y_train)
y_val_avg=np.mean(y_val)
y_test_avg=np.mean(y_test)
mlr=linear_model.LinearRegression()
mlr.fit(X_train,y_train)
y_train_pred=mlr.predict(X_train)
y_val_pred=mlr.predict(X_val)
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

# attendsp = df with stadium percentage
savedfile=attendsp.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Stadium Percentage Data.csv', index=False)

plt.hist(attendsp['Stadium Percentage'],color='steelblue')
plt.xlabel('Stadium Percentage')
plt.ylabel('Quantity of Games')
plt.title('Distribution of Stadium Percentage')
plt.hlines(y=0, xmin=0, xmax=1, color='black', lw=2)
plt.xlim([0, 1])
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Distribution of Stadium Percentage.jpeg')
plt.show()

X = attendsp.iloc[:, :-1]
y = attendsp['Stadium Percentage']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=1)
y_train_avg=np.mean(y_train)
y_val_avg=np.mean(y_val)
y_test_avg=np.mean(y_test)
mlr=linear_model.LinearRegression()
mlr.fit(X_train,y_train)
y_train_pred=mlr.predict(X_train)
y_val_pred=mlr.predict(X_val)
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








