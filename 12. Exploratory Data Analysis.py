import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

attenddata=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Final Data for Model.csv', encoding='latin')
stadiumdata=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Final Data for Model2.csv', encoding='latin')

attcols=['Round','Home Table Position','Away Table Position','Home Last_5_W/L','LastGame',\
        'Away Last_5_W/L','Max Temperature','Rain Level','Wind Speed','Home Last_3_W/L','Last Game in Comp',\
        'Home Win/Loss in Comp','Away Win/Loss in Comp','Home Total P','Day Of Week','Month of Year','Home Winning Percentage',\
        'homeVSaway Winning Percentage','Number ofP14 Wins','Number ofEPCR Wins','Years sinceP14 Win','Years sinceEPCR Win','Stadium Age',\
        'Table Difference','Uncertainty','Sentiment','Win Probability','Tournament_Champions Cup','Tournament_League',\
        'Home Team_Cardiff Blues','Home Team_Connacht Rugby','Home Team_Dragons','Home Team_Edinburgh Rugby','Home Team_Leinster Rugby',\
        'Home Team_Munster Rugby','Home Team_Ospreys','Home Team_Scarlets','Home Team_Ulster Rugby','Home Team_Zebre Rugby',\
        'Venue_BT Murrayfield','Venue_BT Murrayfield Stadium','Venue_Cardiff Arms Park','Away Team_Agen',\
        'Away Team_Bath Rugby','Away Team_Bayonne','Away Team_Benetton Treviso','Away Team_Bordeaux-Begles','Away Team_Bristol Rugby','Away Team_Brive',\
        'Away Team_Cardiff Blues','Away Team_Castres Olympique','Away Team_Connacht Rugby','Away Team_Dragons','Away Team_Edinburgh Rugby',\
        'Away Team_Enisei-STM','Away Team_Exeter Chiefs','Away Team_Glasgow Warriors','Away Team_Gloucester Rugby','Away Team_Grenoble',\
        'Away Team_Harlequins','Away Team_Krasny Yar','Away Team_La Rochelle','Away Team_Leicester Tigers','Away Team_Leinster Rugby','Away Team_London Irish',\
        'Away Team_Lyon','Away Team_Montpellier','Away Team_Munster Rugby','Away Team_Newcastle Falcons','Away Team_Northampton Saints','Away Team_Ospreys',\
        'Away Team_Oyonnax','Away Team_Pau','Away Team_Perpignan','Away Team_RC Toulon','Away Team_Racing 92','Away Team_Rugby Calvisano','Away Team_Sale Sharks',\
        'Away Team_Saracens','Away Team_Scarlets','Away Team_Stade Francais Paris','Away Team_Timisoara Saracens','Away Team_Toulouse','Away Team_Ulster Rugby',\
        'Away Team_Wasps','Away Team_Worcester Warriors','Away Team_Zebre Rugby',\
        'Venue_Constructaquote Stadium (Virginia Park)','Venue_Eugene Cross Park','Venue_Irish Independent Park','Venue_Kingspan Stadium','Venue_La Ghirada',\
        'Venue_Liberty Stadium','Venue_Meggetland','Venue_Morganstone Brewery Field','Venue_Myreside','Venue_Parc y Scarlets','Venue_Principality Stadium',\
        'Venue_RDS Arena','Venue_Rodney Parade','Venue_Sportsground','Venue_Stadio Comunale di Monigo','Venue_Stadio Monigo','Venue_Stadio Sergio Lanfranchi',\
        'Venue_Stadio Tommaso Fattori','Venue_Stadio Zaffanella','Venue_The Sportsground','Venue_Thomond Park','Kick Off Hour_Early','Kick Off Hour_Evening',\
        'Derby_Extra Derby','Derby_Non Derby','Game Competitiveness_Cant Qualify','Game Competitiveness_Has Qualified','Away Country_Ireland','Away Country_Italy','Away Country_Scotland','Away Country_Wales','Temperature_Mild','Temperature_Warm',\
        'Wind_Normal','Wind_Wild','Rain_Dry','Rain_Wet','Age of Stadium_New','Age of Stadium_Old','Win Probability Dummy_Uneven','Stadium Capacity','Attendance']

counter=0
for i in attcols:
    print(str(counter)+'  '+i)
    counter+=1
    
        
sns.pairplot(attenddata[attcols], size=2.5)
plt.tight_layout()
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/Scatter Plot Matrix ATT.png')
plt.close()


attcols2 = ['Round','Attendance','Home Table Position','Away Table Position','Home Last_5_W/L']
sns.pairplot(attenddata[attcols2], size=2.5)
plt.tight_layout()
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/Mini Scatter Plot Matrix ATT.png')
plt.close()


cm = np.corrcoef(attenddata[attcols].values.T)
corr=pd.DataFrame(cm)
sns.set(font_scale=1.5)
fig, ax = plt.subplots(figsize=(500,300))
hm = sns.heatmap(cm,cbar=True,annot=True,square=False,fmt='.2f',annot_kws={'size': 15},yticklabels=attcols,xticklabels=attcols,ax=ax)
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/correlation Heat Map Att.pdf')
plt.close()


corrdfs=[]
for i in range(0,129):
    corr80=corr[(corr[i]>.8)|(corr[i]<-.8)]
    corrdfs.append(corr80)
corrdf2=[]
for i in corrdfs:
    if len(i)>1:
        corrdf2.append(i)
    else:
        continue
corr80all=pd.concat(corrdfs)
for i in range(0,129):
    	corr80all.loc[(corr80all[i]>-0.8)&(corr80all[i]<0.8),i]=np.nan
        
for i in range(0,129):
    	corr80all.loc[(corr80all[i]>0.99),i]=np.nan
        
corr80all2=corr80all.dropna(how='all',axis=1)
corr80all2=corr80all2.drop_duplicates()


cm = np.corrcoef(attenddata[attcols2].values.T)
sns.set(font_scale=1.5)
fig, ax = plt.subplots(figsize=(16,9))
hm = sns.heatmap(cm,cbar=True,annot=True,square=False,fmt='.2f',annot_kws={'size': 15},yticklabels=attcols2,xticklabels=attcols2,ax=ax)
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/mini correlation Heat Map Att.png')
plt.close()




SPcols=['Round','Home Table Position','Away Table Position','Home Last_5_W/L','LastGame',\
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
        'Wind_Normal','Wind_Wild','Rain_Dry','Rain_Wet','Age of Stadium_New','Age of Stadium_Old','Win Probability Dummy_Uneven','Stadium Capacity','Stadium Percentage']

sns.pairplot(stadiumdata[SPcols], size=2.5)
plt.tight_layout()
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/Scatter Plot Matrix ATT.png')
plt.close()


SPcols2 = ['Round','Stadium Percentage','Home Table Position','Away Table Position','Home Last_5_W/L']
sns.pairplot(stadiumdata[SPcols2], size=2.5)
plt.tight_layout()
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/Mini Scatter Plot Matrix ATT.png')
plt.close()


cm = np.corrcoef(stadiumdata[SPcols].values.T)
sns.set(font_scale=1.5)
fig, ax = plt.subplots(figsize=(45,30))
hm = sns.heatmap(cm,cbar=True,annot=True,square=False,fmt='.2f',annot_kws={'size': 15},yticklabels=attcols,xticklabels=attcols,ax=ax)
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/correlation Heat Map Att.png')
plt.close()


cm = np.corrcoef(stadiumdata[SPcols2].values.T)
sns.set(font_scale=1.5)
fig, ax = plt.subplots(figsize=(16,9))
hm = sns.heatmap(cm,cbar=True,annot=True,square=False,fmt='.2f',annot_kws={'size': 15},yticklabels=attcols2,xticklabels=attcols2,ax=ax)
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/mini correlation Heat Map Att.png')
plt.close()






