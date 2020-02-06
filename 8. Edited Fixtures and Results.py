import pandas as pd

games=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Combined Content/Fixtures and Results.csv', encoding='latin-1')
games=games[(games['Home Team'].notnull())]
def split_scores_home(row):
    x=row['Score'].split(' - ')
    y=x[0]
    z=int(y)
    return z

def split_scores_away(row):
    x=row['Score'].split(' - ')
    y=x[1]
    z=int(y)
    return z
games['Score']=games['Score'].astype(str)
    
games['Home Score']=games.apply(lambda row:split_scores_home(row), axis=1)

games['Away Score']=games.apply(lambda row:split_scores_away(row), axis=1)

games=games.drop(columns=['Score'])

def home_win(row):
    if row['Home Score']>row['Away Score']:
        x='Win'
    elif row['Home Score']==row['Away Score']:
        x='Draw'
    else:
        x='Loss'
    return x

def away_win(row):
    if row['Home Score']<row['Away Score']:
        x='Win'
    elif row['Home Score']==row['Away Score']:
        x='Draw'
    else:
        x='Loss'
    return x

games['Home Win/loss/draw']=games.apply(lambda row:home_win(row), axis=1)
games['Away Win/loss/draw']=games.apply(lambda row:away_win(row), axis=1)

teams=pd.pivot_table(games,index='Home Team')

games=games[(games['Home Team'].str.contains('Benetton Rugby|Benetton Treviso|Cardiff Blues|Connacht Rugby|Dragons|Edinburgh Rugby|Glasgow Warriors|Isuzu Southern Kings|Leinster Rugby|Munster Rugby|Newport Gwent Dragons|Ospreys|Scarlets|Southern Kings|Toyota Cheetahs|Ulster Rugby|Zebre Rugby|Zebre Rugby Club'))]

games['Home Team']=games['Home Team'].replace(r'Benetton Rugby','Benetton Treviso',regex=True)
games['Home Team']=games['Home Team'].replace(r'Newport Gwent Dragons','Dragons',regex=True)
games['Home Team']=games['Home Team'].replace(r'Isuzu Southern Kings','Southern Kings',regex=True)
games['Home Team']=games['Home Team'].replace(r'Zebre Rugby Club','Zebre Rugby',regex=True)

teams=pd.pivot_table(games,index='Home Team')
teams=teams.reset_index()
home_teams=list(teams['Home Team'])

awayteams=pd.pivot_table(games,index='Away Team')

games['Away Team']=games['Away Team'].replace(r'Benetton Rugby','Benetton Treviso',regex=True)
games['Away Team']=games['Away Team'].replace(r'Newport Gwent Dragons','Dragons',regex=True)
games['Away Team']=games['Away Team'].replace(r'Isuzu Southern Kings','Southern Kings',regex=True)
games['Away Team']=games['Away Team'].replace(r'Zebre Rugby Club','Zebre Rugby',regex=True)
games['Away Team']=games['Away Team'].replace(r'Bristol Bears','Bristol Rugby',regex=True)

games['Date']=pd.to_datetime(games['Date'])

games=games[(games['Date'].notnull())]
def addSeason(row):
    if (row['Date'] > pd.to_datetime('2003-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2004-07-15 00:00:00')):
        x= '2003/2004 Season'
    elif (row['Date'] > pd.to_datetime('2004-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2005-07-15 00:00:00')):
        x= '2004/2005 Season'
    elif (row['Date'] > pd.to_datetime('2005-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2006-07-15 00:00:00')):
        x= '2005/2006 Season'
    elif (row['Date'] > pd.to_datetime('2006-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2007-07-15 00:00:00')):
        x= '2006/2007 Season'
    elif (row['Date'] > pd.to_datetime('2007-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2008-07-15 00:00:00')):
        x= '2007/2008 Season'
    elif (row['Date'] > pd.to_datetime('2008-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2009-07-15 00:00:00')):
        x= '2008/2009 Season'
    elif (row['Date'] > pd.to_datetime('2009-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2010-07-15 00:00:00')):
        x= '2009/2010 Season'
    elif (row['Date'] > pd.to_datetime('2010-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2011-07-15 00:00:00')):
        x= '2010/2011 Season'
    elif (row['Date'] > pd.to_datetime('2011-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2012-07-15 00:00:00')):
        x= '2011/2012 Season'
    elif (row['Date'] > pd.to_datetime('2012-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2013-07-15 00:00:00')):
        x= '2012/2013 Season'
    elif (row['Date'] > pd.to_datetime('2013-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2014-07-15 00:00:00')):
        x= '2013/2014 Season'
    elif (row['Date'] > pd.to_datetime('2014-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2015-07-15 00:00:00')):
        x= '2014/2015 Season'
    elif (row['Date'] > pd.to_datetime('2015-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2016-07-15 00:00:00')):
        x= '2015/2016 Season'
    elif (row['Date'] > pd.to_datetime('2016-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2017-07-15 00:00:00')):
        x= '2016/2017 Season'
    elif (row['Date'] > pd.to_datetime('2017-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2018-07-15 00:00:00')):
        x= '2017/2018 Season'
    elif (row['Date'] > pd.to_datetime('2018-07-15 00:00:00')) & (row['Date'] < pd.to_datetime('2019-07-15 00:00:00')):
        x= '2018/2019 Season'
    else:
        x= '2019/2020 Season'
    return x

games['Season']=games.apply(lambda row: addSeason(row), axis=1)
season=pd.pivot_table(games, index='Season')
season=season.reset_index()
seasons=list(season['Season'])

dftest=[]
for i in home_teams:
    df=[]
    df=games[(games['Home Team'].str.contains(i))] | games[(games['Away Team'].str.contains(i))]
    for j in seasons:
        df2=df[(df['Season'].str.contains(j))]
        df2=df2.sort_values(by=['Date'])
        df3=df2[(df2['Tournament'].str.contains('League'))]
        df3['rc']=1
        df3['Round2']=df3['rc'].expanding(1).sum()
        df.append(df3)
    dftest.append(df)
testp14=pd.concat(dftest)
        
        
        

test=df7[:20]

test['test count']=test['Home Win/loss/draw'].rolling(3).sum()


def roundcalc(row):
    if row['Round']>21:
        x='Knock Out'
    else:
        x='Pool'
    return x

def roundcalc12(row):
    if row['Round']>22:
        x='Knock Out'
    else:
        x='Pool'
    return x

def roundcalc10(row):
    if row['Round']>18:
        x='Knock Out'
    else:
        x='Pool'
    return x
teamslist=pd.pivot_table(df7, index='Home Team', values = None).reset_index()
teams_list=list(teamslist['Home Team'])

def awayCountry(row):
    if row['Away Team']==('Benetton Rugby'):
        x=4
    elif row['Away Team']==('Zebre Rugby Club'):
        x=4
    elif row['Away Team']==('Zebre Rugby'):
        x=4
    elif row['Away Team']==('Zebre'):
        x=4
    elif row['Away Team']==('Aironi Rugby'):
        x=4
    elif row['Away Team']==('Benetton Treviso'):
        x=4
    elif row['Away Team']== ('Edinburgh Rugby'):
        x=3 
    elif row['Away Team']== ('Glasgow Warriors'):
        x=3 
    elif row['Away Team']== ('Cardiff Blues'):
        x=2
    elif row['Away Team']== ('Dragons'):
        x=2
    elif row['Away Team']== ('Newport Gwent Dragons'):
        x=2
    elif row['Away Team']== ('Ospreys'):
        x=2
    elif row['Away Team']== ('Scarlets'):
        x=2
    elif row['Away Team']== ('Llanelli Scarlets'):
        x=2
    elif row['Away Team']== ('Isuzu Southern Kings'):
        x=5
    elif row['Away Team']== ('Southern Kings'):
        x=5
    elif row['Away Team']== ('Toyota Cheetahs'):
        x=5
    else:
        x=1
    return x

def homeCountry(row):
    if row['Home Team']==('Benetton Rugby'):
        x=4
    elif row['Home Team']==('Zebre Rugby Club'):
        x=4
    elif row['Home Team']== ('Edinburgh Rugby'):
        x=3 
    elif row['Home Team']== ('Glasgow Warriors'):
        x=3 
    elif row['Home Team']== ('Cardiff Blues'):
        x=2
    elif row['Home Team']== ('Dragons'):
        x=2
    elif row['Home Team']== ('Ospreys'):
        x=2
    elif row['Home Team']== ('Scarlets'):
        x=2
    elif row['Home Team']== ('Isuzu Southern Kings'):
        x=5
    elif row['Home Team']== ('Toyota Cheetahs'):
        x=5
    else:
        x=1
    return x


 
df8=pd.pivot_table(Season1819, index='Home Team', values = None).reset_index()
teams=list(df8['Home Team'])
teamsqty=len(teams)
Season1819['Team Qty']=teamsqty 
df9=[]
for i in teams:
    x=(Season1819[(Season1819['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season1819[(Season1819['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=1819
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df9.append(p)
Season_1819=pd.concat(df9)

df10=pd.pivot_table(Season1718, index='Home Team', values = None).reset_index()
teams=list(df10['Home Team'])
teamsqty=len(teams)
Season1718['Team Qty']=teamsqty 
df11=[]
for i in teams:
    x=(Season1718[(Season1718['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season1718[(Season1718['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=1718
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df11.append(p)
Season_1718=pd.concat(df11)

df12=pd.pivot_table(Season1617, index='Home Team', values = None).reset_index()
teams=list(df12['Home Team'])
teamsqty=len(teams)
Season1617['Team Qty']=teamsqty 
df13=[]
for i in teams:
    x=(Season1617[(Season1617['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season1617[(Season1617['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc12(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=1617
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df13.append(p)
Season_1617=pd.concat(df13 )

df14=pd.pivot_table(Season1516, index='Home Team', values = None).reset_index()
teams=list(df14['Home Team'])
teamsqty=len(teams)
Season1516['Team Qty']=teamsqty 
df15=[]
for i in teams:
    x=(Season1516[(Season1516['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season1516[(Season1516['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc12(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=1516
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df15 .append(p)
Season_1516=pd.concat(df15 )

df16=pd.pivot_table(Season1415, index='Home Team', values = None).reset_index()
teams=list(df16['Home Team'])
teamsqty=len(teams)
Season1415['Team Qty']=teamsqty 
df17=[]
for i in teams:
    x=(Season1415[(Season1415['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season1415[(Season1415['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc12(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=1415
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df17.append(p)
Season_1415=pd.concat(df17)

df18=pd.pivot_table(Season1314, index='Home Team', values = None).reset_index()
teams=list(df18['Home Team'])
teamsqty=len(teams)
Season1314['Team Qty']=teamsqty 
df19=[]
for i in teams:
    x=(Season1314[(Season1314['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season1314[(Season1314['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc12(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=1314
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df19.append(p)
Season_1314=pd.concat(df19)

df20=pd.pivot_table(Season1213, index='Home Team', values = None).reset_index()
teams=list(df20['Home Team'])
teamsqty=len(teams)
Season1213['Team Qty']=teamsqty 
df21=[]
for i in teams:
    x=(Season1213[(Season1213['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season1213[(Season1213['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc12(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=1213
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df21.append(p)
Season_1213=pd.concat(df21)

df22=pd.pivot_table(Season1112, index='Home Team', values = None).reset_index()
teams=list(df22['Home Team'])
teamsqty=len(teams)
Season1112['Team Qty']=teamsqty 
df23=[]
for i in teams:
    x=(Season1112[(Season1112['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season1112[(Season1112['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc10(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=1112
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df23.append(p)
Season_1112=pd.concat(df23)

df24=pd.pivot_table(Season1011, index='Home Team', values = None).reset_index()
teams=list(df24['Home Team'])
teamsqty=len(teams)
Season1011['Team Qty']=teamsqty 
df25=[]
for i in teams:
    x=(Season1011[(Season1011['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season1011[(Season1011['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc12(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=1011
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df25.append(p)
Season_1011=pd.concat(df25)

df26=pd.pivot_table(Season0910, index='Home Team', values = None).reset_index()
teams=list(df26['Home Team'])
teamsqty=len(teams)
Season0910['Team Qty']=teamsqty 
df27=[]
for i in teams:
    x=(Season0910[(Season0910['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season0910[(Season0910['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc10(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=910
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df27.append(p)
Season_0910=pd.concat(df27)

df28=pd.pivot_table(Season0809, index='Home Team', values = None).reset_index()
teams=list(df28['Home Team'])
teamsqty=len(teams)
Season0809['Team Qty']=teamsqty 
df29=[]
for i in teams:
    x=(Season0809[(Season0809['Home Team']==i)])
    x['Wins']=x['Home Win/loss/draw']
    y=(Season0809[(Season0809['Away Team']==i)])
    y['Wins']=y['Away Win/loss/draw']
    z=x.append(y)
    z=z.drop_duplicates('Date')
    z=z.sort_values(by='Date')
    z['Last3w/l']=z['Wins'].rolling(4).sum()
    z['Last 3w/l']=z['Last3w/l']-z['Wins']
    avg=z['Last 3w/l'].mean(skipna=True)
    avg=int(avg)
    z['Last 3w/l']=z['Last 3w/l'].fillna(avg)
    z['round count']=1
    z['Round']=z['round count'].expanding(1).sum()
    z['Pool Stage']=z.apply(lambda row:roundcalc12(row), axis=1)
    z['Home Country']=z.apply(lambda row:homeCountry(row), axis=1)
    z['Away Country']=z.apply(lambda row:awayCountry(row), axis=1)
    p=z[(z['Home Team']==i)]
    p['Tournament']=809
    p['TimeSinceLstgm']=p['Date']-p['Date'].shift(1)
    p['TimeSinceLstgmdays']=p['TimeSinceLstgm'].dt.days
    p['TimeSinceLstgmdays']=p['TimeSinceLstgmdays'].fillna(90)
    df29.append(p)
Season_0809=pd.concat(df29)

Seasons=[Season_0809,Season_0910,Season_1011,Season_1112,Season_1213,Season_1314,Season_1415,Season_1516,Season_1617,Season_1718,Season_1819]

pRO14=pd.concat(Seasons)
pRO14=pRO14.drop(['Score','Ref','Home Total score','away total score','home Total Tries','Away Total Tries',\
                  'Home Total Conversions','Away Total Conversions','Home Total Dropgoals','Away Total Dropgoals',\
                  'Home Total Penalties','Away Total Penalties','Home Total Metres Gained','Away Total Metres Gained',\
                  'Home Total Carries','Away Total Carries','Home Total Passes Made','Away Total Passes Made',\
                  'Home Total Tackles Made','Away Total Tackles Made','Home Total Tackles Missed','Away_total_tackles_missed',\
                  'Home Total Turnovers Won','Away Total Turnovers Won','Home Total Turnovers Conceded','Away Total Turnovers Conceded',\
                  'Home Total Penalties Conceded','Away Total Penalties Conceded','Home Total Yellow Cards','Away Total Yellow Cards',\
                  'Home Total Red Cards','Away Total Red Cards','away_played','home_losses','away_losses','away_draws',\
                  'Last3w/l','round count','Home Score','Away Score','Home Win/loss/draw','Away Win/loss/draw','TimeSinceLstgm'],axis=1)
pRO14=pRO14.sort_values(by='Date')
pRO14=pRO14[pd.notnull(pRO14['Attendance'])]

def worldcupyr(row):
    if row['Tournament']==1819:
        x=4
    elif row['Tournament']==1718:
        x=3
    elif row['Tournament']==1617:
        x=2
    elif row['Tournament']==1516:
        x=1
    elif row['Tournament']==1415:
        x=4
    elif row['Tournament']==1314:
        x=3
    elif row['Tournament']==1213:
        x=2
    elif row['Tournament']==1112:
        x=1
    elif row['Tournament']==1011:
        x=4
    elif row['Tournament']==910:
        x=3
    elif row['Tournament']==809:
        x=2
    else:
        x=''
    return x

pRO14['Attendance'] = pRO14['Attendance'].map(lambda x: x.lstrip('Att: '))
pRO14['Attendance'] = pRO14['Attendance'].map(lambda x: x.replace(',',''))
pRO14['Attendance'] = pRO14['Attendance'].astype(int)
pRO14['Date'] = pRO14['Date'].map(lambda x: x.strftime('%Y-%m-%d'))
df30=pd.pivot_table(pRO14, index='Venue', values = None).reset_index()
stadium=list(df30['Venue'])

def seturl(row):
    if row['Venue']=='AVIVA Stadium':
        x='https://www.worldweatheronline.com/dublin-weather-history/dublin/ie.aspx'
    elif row['Venue']=='Aviva Stadium':
        x='https://www.worldweatheronline.com/dublin-weather-history/dublin/ie.aspx'
    elif row['Venue']=='BT Murrayfield':
        x='https://www.worldweatheronline.com/edinburgh-weather-history/city-of-edinburgh/gb.aspx'
    elif row['Venue']=='Cardiff Arms Park':
        x='https://www.worldweatheronline.com/cardiff-weather-history/cardiff/gb.aspx'
    elif row['Venue']=='Cardiff City Stadium':
        x='https://www.worldweatheronline.com/cardiff-weather-history/cardiff/gb.aspx'
    elif row['Venue']=='Celtic Park':
        x='https://www.worldweatheronline.com/glasgow-weather-history/glasgow-city/gb.aspx'
    elif row['Venue']=='Constructaquote Stadium (Virginia Park)':
        x='https://www.worldweatheronline.com/cardiff-weather-history/cardiff/gb.aspx'
    elif row['Venue']=='Eugene Cross Park':
        x='https://www.worldweatheronline.com/cardiff-weather-history/cardiff/gb.aspx'
    elif row['Venue']=='Firhill Stadium':
        x='https://www.worldweatheronline.com/glasgow-weather-history/glasgow-city/gb.aspx'
    elif row['Venue']=='Irish Independent Park':
        x='https://www.worldweatheronline.com/cork-weather-history/cork/ie.aspx'
    elif row['Venue']=='Isaac Wolfson Stadium':
        x='https://www.worldweatheronline.com/port-elizabeth-weather-history/eastern-cape/za.aspx'
    elif row['Venue']=='Kingspan Stadium':
        x='https://www.worldweatheronline.com/belfast-weather-history/belfast/gb.aspx'    
    elif row['Venue']=='Liberty Stadium':
        x='https://www.worldweatheronline.com/swansea-weather-history/swansea/gb.aspx'   
    elif row['Venue']=='Myreside':
        x='https://www.worldweatheronline.com/edinburgh-weather-history/city-of-edinburgh/gb.aspx'     
    elif row['Venue']=='NMU (Madibaz) Stadium':
        x='https://www.worldweatheronline.com/port-elizabeth-weather-history/eastern-cape/za.aspx'
    elif row['Venue']=='Outeniqua Park':
        x='https://www.worldweatheronline.com/george-weather-history/western-cape/za.aspx'
    elif row['Venue']=='Parc y Scarlets':
        x='https://www.worldweatheronline.com/llanelli-weather-history/carmarthenshire/gb.aspx'
    elif row['Venue']=='Principality Stadium':
        x='https://www.worldweatheronline.com/cardiff-weather-history/cardiff/gb.aspx'
    elif row['Venue']=='RDS Arena':
        x='https://www.worldweatheronline.com/dublin-weather-history/dublin/ie.aspx'
    elif row['Venue']=='Rodney Parade':
        x='https://www.worldweatheronline.com/cardiff-weather-history/cardiff/gb.aspx'
    elif row['Venue']=='Scotstoun Stadium':
        x='https://www.worldweatheronline.com/glasgow-weather-history/glasgow-city/gb.aspx'
    elif row['Venue']=='Sportsground':
        x='https://www.worldweatheronline.com/galway-weather-history/galway/ie.aspx'
    elif row['Venue']=='Stadio Monigo':
        x='https://www.worldweatheronline.com/treviso-weather-history/veneto/it.aspx'
    elif row['Venue']=='Stadio Sergio Lanfranchi':
        x='https://www.worldweatheronline.com/parma-weather-history/emilia-romagna/it.aspx'
    elif row['Venue']=='Stadio Tommaso Fattori':
        x='https://www.worldweatheronline.com/rome-weather-history/lazio/it.aspx'
    elif row['Venue']=='Stadio Zaffanella':
        x='https://www.worldweatheronline.com/parma-weather-history/emilia-romagna/it.aspx'    
    elif row['Venue']=='Stadio del Tricolore':
        x='https://www.worldweatheronline.com/parma-weather-history/emilia-romagna/it.aspx'   
    elif row['Venue']=='Stradey Park':
        x='https://www.worldweatheronline.com/llanelli-weather-history/carmarthenshire/gb.aspx'    
    elif row['Venue']=='Thomond Park':
        x='https://www.worldweatheronline.com/limerick-weather-history/limerick/ie.aspx'    
    elif row['Venue']=='Toyota Stadium':
        x='https://www.worldweatheronline.com/bloemfontein-weather-history/free-state/za.aspx'    
    elif row['Venue']=='Meggetland':
        x='https://www.worldweatheronline.com/edinburgh-weather-history/city-of-edinburgh/gb.aspx'    
    elif row['Venue']=='Morganstone Brewery Field':
        x='https://www.worldweatheronline.com/cardiff-weather-history/cardiff/gb.aspx' 
    elif row['Venue']=='Nelson Mandela Bay':
        x='https://www.worldweatheronline.com/port-elizabeth-weather-history/eastern-cape/za.aspx' 
    elif row['Venue']=='Rugby Park':
        x='https://www.worldweatheronline.com/galway-weather-history/galway/ie.aspx'     
    else:
        x=''
    return x
    
pRO14['Stadium URL']=pRO14.apply(lambda row:seturl(row), axis=1)    
    
pRO14['Tm Since World Cup']=pRO14.apply(lambda row:worldcupyr(row),axis=1)
    
def maxtemp(row):
    url=row['Stadium URL']
    date=row['Date']
    driver = webdriver.Firefox(executable_path=r'C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Code/geckodriver')
    #driver.maximize_window()
    
    try:
        print('getting '+date+url)
        driver.get(url)
        dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
        dateinput.send_keys(date)
        submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
        content=driver.page_source
        driver.quit()
        html=bs(content, 'html.parser')
        html2=html.find('div',attrs={'class':'weather_prim_info independent'})
        html3=html2.find('div',attrs={'class':'max_temp'})
        html4=html3.find('div',attrs={'class':'count'})
        max_temp=html4.get_text()
        return max_temp 
    except:
        try:
            driver.quit()
            print('Trying getting '+date+url)
            driver.get(url)
            dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
            dateinput.send_keys(date)
            submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
            content=driver.page_source
            driver.quit()
            html=bs(content, 'html.parser')
            html2=html.find('div',attrs={'class':'weather_prim_info independent'})
            html3=html2.find('div',attrs={'class':'max_temp'})
            html4=html3.find('div',attrs={'class':'count'})
            max_temp=html4.get_text()
            return max_temp
        except:
            driver.quit()
            print('failed '+url+date)
            max_temp=''
            return max_temp
pRO14['Max Temp']=pRO14.apply(lambda row:maxtemp(row), axis=1) 

pR014NA=pRO14[(pRO14['Max Temp']=='')]
pR0142=pRO14[(pRO14['Max Temp']!='')]
pR014NA['Max Temp']=pR014NA.apply(lambda row:maxtemp(row), axis=1)

pRO14df=pR0142.append(pR014NA)


def rain(row):
    url=row['Stadium URL']
    date=row['Date']
    driver = webdriver.Firefox(executable_path=r'C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Code/geckodriver')
    #driver.maximize_window()
    
    try:
        print('getting '+date+url)
        driver.get(url)
        dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
        dateinput.send_keys(date)
        submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
        content=driver.page_source
        driver.quit()
        html=bs(content, 'html.parser')
        html2=html.find('div',attrs={'class':'weather_prim_info independent'})
        html3=html2.find('div',attrs={'class':'info_item elem_item'})
        rain=html3.get_text()
        return rain 
    except:
        driver.quit()
        print('Returning Blank')
        rain = ''
        return rain
    
pRO14df['Rain']=pRO14df.apply(lambda row:rain(row), axis=1) 

pR014NA2=pRO14df[(pRO14df['Rain']=='')]
pR014df2=pRO14df[(pRO14df['Rain']!='')]
pR014NA2['Rain']=pR014NA2.apply(lambda row:rain(row), axis=1)

pRO14df_2=pR014df2.append(pR014NA2)    
    
pR014NA3=pRO14df_2[(pRO14df_2['Rain']=='')]
pR0143=pRO14df_2[(pRO14df_2['Rain']!='')]
pR014NA3['Rain']=pR014NA3.apply(lambda row:rain(row), axis=1)    
    
pRO14df_3=pR0143.append(pR014NA3)     
    
def wind(row):
    url=row['Stadium URL']
    date=row['Date']
    driver = webdriver.Firefox(executable_path=r'C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Code/geckodriver')
    #driver.maximize_window()
    
    try:
        print('getting '+date+url)
        driver.get(url)
        dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
        dateinput.send_keys(date)
        submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
        content=driver.page_source
        driver.quit()
        html=bs(content, 'html.parser')
        html2=html.find('div',attrs={'class':'tb_row tb_wind'})
        html3=html2.find_all('div',attrs={'class':'tb_cont_item'})
        wind=[]
        for i in html3:
            x= i.get_text()
            wind.append(x)
        windspeed=wind[6]
        return windspeed
    except:
        driver.quit()
        print('Returning Blank')
        windspeed = ''
        return windspeed
    
pRO14df_3['WindSpeed']=pRO14df_3.apply(lambda row:wind(row), axis=1)     
    
pR014NA4=pRO14df_3[(pRO14df_3['WindSpeed']=='')]
pR0144=pRO14df_3[(pRO14df_3['WindSpeed']!='')]
pR014NA4['WindSpeed']=pR014NA4.apply(lambda row:wind(row), axis=1)    
    
pRO14df_4=pR0144.append(pR014NA4) 

def gettemp(row):
    temp=row['Max Temp'].split('°')
    temps=int(temp[0])
    return temps

pRO14df_4['Temperature']=pRO14df_4.apply(lambda row:gettemp(row), axis=1)

def getrain(row):
    rain=row['Rain'].split(' ')
    raining=float(rain[1])
    return raining

pRO14df_4['Rain Level']=pRO14df_4.apply(lambda row:getrain(row), axis=1)

def getwind(row):
    wind=row['WindSpeed'].split(' ')
    windspeed=int(wind[0])
    return windspeed

pRO14df_4['Wind Speed']=pRO14df_4.apply(lambda row:getwind(row), axis=1)

pRO14df_4=pRO14df_4.rename(columns={'Tournament':'Season'})

pRO14df_5=pRO14df_4[(pRO14df_4['Pool Stage']=='Pool')]

pRO14df_6=pRO14df_5.drop(['home_played','Team Qty','Wins','Pool Stage','Stadium URL','Max Temp','Rain','WindSpeed'],axis=1)

gdp=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Data/GDP.csv',encoding='latin-1')

pRO14df_7=pd.merge(pRO14df_6,gdp,how='left',left_on=['Season','Home Country'],right_on=['Season','Home Country'])

pRO14df_7['Date']=pd.to_datetime(pRO14df_7['Date'])
pRO14df_7['Day Of Week']=pRO14df_7['Date'].dt.dayofweek

def time(row):
    ko=row['Kick Off'].split(':')
    ko2=int(ko[0])
    return ko2
pRO14df_7['Kick Off Hour']=pRO14df_7.apply(lambda row:time(row), axis=1)
pRO14df_7=pRO14df_7.reset_index(drop=True)
def stadindex(row):
    if row['Venue']=='AVIVA Stadium':
        x=1
    elif row['Venue']=='Aviva Stadium':
        x=1
    elif row['Venue']=='BT Murrayfield':
        x=2
    elif row['Venue']=='Cardiff Arms Park':
        x=3
    elif row['Venue']=='Cardiff City Stadium':
        x=4
    elif row['Venue']=='Celtic Park':
        x=5
    elif row['Venue']=='Constructaquote Stadium (Virginia Park)':
        x=6
    elif row['Venue']=='Eugene Cross Park':
        x=7
    elif row['Venue']=='Firhill Stadium':
        x=8
    elif row['Venue']=='Irish Independent Park':
        x=9
    elif row['Venue']=='Isaac Wolfson Stadium':
        x=10
    elif row['Venue']=='Kingspan Stadium':
        x=11
    elif row['Venue']=='Liberty Stadium':
        x=12
    elif row['Venue']=='Meggetland':
        x=13
    elif row['Venue']=='Morganstone Brewery Field':
        x=14
    elif row['Venue']=='Myreside':
        x=15
    elif row['Venue']=='NMU (Madibaz) Stadium':
        x=16
    elif row['Venue']=='Nelson Mandela Bay':
        x=17
    elif row['Venue']=='Outeniqua Park':
        x=18
    elif row['Venue']=='Parc y Scarlets':
        x=19
    elif row['Venue']=='Principality Stadium':
        x=20
    elif row['Venue']=='RDS Arena':
        x=21
    elif row['Venue']=='Rodney Parade':
        x=22
    elif row['Venue']=='Rugby Park':
        x=23
    elif row['Venue']=='Scotstoun Stadium':
        x=24
    elif row['Venue']=='Sportsground':
        x=25
    elif row['Venue']=='Stadio Monigo':
        x=26
    elif row['Venue']=='Stadio Sergio Lanfranchi':
        x=27
    elif row['Venue']=='Stadio Tommaso Fattori':
        x=28
    elif row['Venue']=='Stadio Zaffanella':
        x=29
    elif row['Venue']=='Stadio del Tricolore':
        x=30
    elif row['Venue']=='Stradey Park':
        x=31
    elif row['Venue']=='Thomond Park':
        x=32
    elif row['Venue']=='Toyota Stadium':
        x=33
    else:
        x='Not In List'
    return x
pRO14df_7['Stadium']=pRO14df_7.apply(lambda row:stadindex(row), axis=1)

print(teams_list)

def teamindxh(row):
    if row['Home Team']=='Aironi Rugby':
        x=1
    elif row['Home Team']=='Benetton Rugby':
        x=2
    elif row['Home Team']=='Benetton Treviso':
        x=2
    elif row['Home Team']=='Cardiff Blues':
        x=3
    elif row['Home Team']=='Connacht Rugby':
        x=4
    elif row['Home Team']=='Dragons':
        x=5
    elif row['Home Team']=='Edinburgh Rugby':
        x=6
    elif row['Home Team']=='Glasgow Warriors':
        x=7
    elif row['Home Team']=='Isuzu Southern Kings':
        x=8
    elif row['Home Team']=='Leinster Rugby':
        x=9
    elif row['Home Team']=='Llanelli Scarlets':
        x=10
    elif row['Home Team']=='Munster Rugby':
        x=11
    elif row['Home Team']=='Newport Gwent Dragons':
        x=5
    elif row['Home Team']=='Ospreys':
        x=12
    elif row['Home Team']=='Scarlets':
        x=10
    elif row['Home Team']=='Southern Kings':
        x=8
    elif row['Home Team']=='Toyota Cheetahs':
        x=13
    elif row['Home Team']== 'Ulster Rugby':
        x=14
    elif row['Home Team']== 'Zebre':
        x=1
    elif row['Home Team']== 'Zebre Rugby':
        x=1
    elif row['Home Team']== 'Zebre Rugby Club':
        x=1
    return x
pRO14df_7['Home Team Indx']=pRO14df_7.apply(lambda row:teamindxh(row), axis=1)

def teamindxa(row):
    if row['Away Team']=='Aironi Rugby':
        x=1
    elif row['Away Team']=='Benetton Rugby':
        x=2
    elif row['Away Team']=='Benetton Treviso':
        x=2
    elif row['Away Team']=='Cardiff Blues':
        x=3
    elif row['Away Team']=='Connacht Rugby':
        x=4
    elif row['Away Team']=='Dragons':
        x=5
    elif row['Away Team']=='Edinburgh Rugby':
        x=6
    elif row['Away Team']=='Glasgow Warriors':
        x=7
    elif row['Away Team']=='Isuzu Southern Kings':
        x=8
    elif row['Away Team']=='Leinster Rugby':
        x=9
    elif row['Away Team']=='Llanelli Scarlets':
        x=10
    elif row['Away Team']=='Munster Rugby':
        x=11
    elif row['Away Team']=='Newport Gwent Dragons':
        x=5
    elif row['Away Team']=='Ospreys':
        x=12
    elif row['Away Team']=='Scarlets':
        x=10
    elif row['Away Team']=='Southern Kings':
        x=8
    elif row['Away Team']=='Toyota Cheetahs':
        x=13
    elif row['Away Team']== 'Ulster Rugby':
        x=14
    elif row['Away Team']== 'Zebre':
        x=1
    elif row['Away Team']== 'Zebre Rugby':
        x=1
    elif row['Away Team']== 'Zebre Rugby Club':
        x=1
    return x
pRO14df_7['Away Team Indx']=pRO14df_7.apply(lambda row:teamindxa(row), axis=1)

pRO14df_8=pRO14df_7[(pRO14df_7['Date']>'2008-12-31 00:00:00')]
pRO14df_8=pRO14df_8.drop(['Date','Kick Off','Home Team','Away Team','Venue'],axis=1)
pRO14df_8=pRO14df_8.drop(['Season'],axis=1)

savedfile=pRO14df_8.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Data/PRO14 Data Set 5.csv',index=False)

'Day Of Week'
