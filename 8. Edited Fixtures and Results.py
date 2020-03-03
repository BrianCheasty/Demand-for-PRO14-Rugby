import pandas as pd
import numpy as np

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


games['Home Team']=games['Home Team'].replace(r'Benetton Rugby','Benetton Treviso',regex=True)
games['Home Team']=games['Home Team'].replace(r'Newport Gwent Dragons','Dragons',regex=True)
games['Home Team']=games['Home Team'].replace(r'Isuzu Southern Kings','Southern Kings',regex=True)
games['Home Team']=games['Home Team'].replace(r'Zebre Rugby Club','Zebre Rugby',regex=True)
games['Home Team']=games['Home Team'].replace(r'Bristol Bears','Bristol Rugby',regex=True)

teams=pd.pivot_table(games,index='Home Team')
teams=teams.reset_index()
home_teams=list(teams['Home Team'])


awayteams=pd.pivot_table(games,index='Away Team')
awayteams=awayteams.reset_index()
away_teams=list(awayteams['Away Team'])

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
games=games.drop_duplicates(subset=['Date','Home Team','Away Team','Ref'])
check=pd.pivot_table(games, index='Home Team', columns='Season',values='Tournament',aggfunc='count')

pro14=games[(games['Tournament'].str.contains('League'))]
epcr=games[(~games['Tournament'].str.contains('League'))]

season=pd.pivot_table(games, index='Season')
season=season.reset_index()
seasons=list(season['Season'])



df1=[]
for i in home_teams:
    df2=[]
    df3=pro14[(pro14['Home Team'].str.contains(i)) | (games['Away Team'].str.contains(i))]
    for j in seasons:
        df4=df3[(df3['Season'].str.contains(j))]
        df4=df4.sort_values(by=['Date'])
        df5=df4[(df4['Tournament'].str.contains('League'))]
        df5['rc']=1
        df5['Round2']=df5['rc'].expanding(1).sum()
        df5=df5.drop(columns=['rc'],axis=1)
        df2.append(df5)
    df6=pd.concat(df2)
    df1.append(df6)
pro142=pd.concat(df1)
pro142=pro142.drop_duplicates(subset=['Date','Home Team','Away Team','Ref'])
pro142['Round']=pro142['Round'].fillna(pro142['Round2'])
pro142['Round2']=pro142['Round2'].astype(str)
pro142=pro142.drop(columns=['Round2']) 
pro142.info() 


                                   
epcrround=epcr[(epcr['Round'].str.contains('1|2|3|4|5|6'))]
epcrnoround=epcr[(~epcr['Round'].str.contains('1|2|3|4|5|6'))]

epcrround.loc[epcrround['Round'].str.contains('1'),'Round']='1'
epcrround.loc[epcrround['Round'].str.contains('2'),'Round']='2'
epcrround.loc[epcrround['Round'].str.contains('3'),'Round']='3'
epcrround.loc[epcrround['Round'].str.contains('4'),'Round']='4'
epcrround.loc[epcrround['Round'].str.contains('5'),'Round']='5'
epcrround.loc[epcrround['Round'].str.contains('6'),'Round']='6'
epcrround.info()
df1=[]
for i in home_teams:
    df2=[]
    df3=epcrnoround[(epcrnoround['Home Team'].str.contains(i)) | (epcrnoround['Away Team'].str.contains(i))]
    for j in seasons:
        df4=df3[(df3['Season'].str.contains(j))]
        df4=df4.sort_values(by=['Date'])
        df4['rc']=1
        df4['Round2']=df4['rc'].expanding(1).sum()
        df4=df4.drop(columns=['rc'],axis=1)
        print(len(df4))
        df2.append(df4)
    df6=pd.concat(df2)
    df1.append(df6)
    
epcrnoround2=pd.concat(df1)
epcrnoround2=epcrnoround2.drop_duplicates(subset=['Date','Home Team','Away Team','Ref'])
epcrnoround2['Round2']=epcrnoround2['Round2'].astype(str)
epcrnoround2.loc[epcrnoround2['Round2'].str.contains('1'),'Round']='7'
epcrnoround2.loc[epcrnoround2['Round2'].str.contains('2'),'Round']='8'
epcrnoround2.loc[epcrnoround2['Round2'].str.contains('3'),'Round']='9'
epcrnoround2.loc[epcrnoround2['Round2'].str.contains('4'),'Round']='10'
epcrnoround2.loc[epcrnoround2['Round2'].str.contains('5'),'Round']='11'
epcrnoround2.loc[epcrnoround2['Round2'].str.contains('6'),'Round']='12'

epcrnoround2=epcrnoround2.drop(columns='Round2')
epcr2=epcrround.append(epcrnoround2)

epcr2.info()
epcr2=epcr2.sort_index()
pro142.info()
pro142=pro142.sort_index()



df1=[]
for i in home_teams:
    df3=epcr2[(epcr2['Home Team'].str.contains(i)) | (epcr2['Away Team'].str.contains(i))]
    if len(df3) > 0:
        df3.loc[((df3['Home Team'].str.contains(i))&(df3['Home Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3.loc[((df3['Away Team'].str.contains(i))&(df3['Away Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3['Win']=df3['Win'].fillna(0)
        df3=df3.sort_values(by=['Date'])
        df3['Last_5_W/L']=df3['Win'].rolling(5).sum()
        df3.loc[(df3['Home Team']==(i)),'Home Last_5_W/L_EPCR']=df3['Last_5_W/L']
        df3['Home Last_5_W/L_EPCR']=df3['Home Last_5_W/L_EPCR'].fillna(999)
        df4=df3[(df3['Home Team']==(i))]
        df4['Time']=df4['Date']-df4['Date'].shift(1)
        df4['Last_EPCR']=df4['Time'].dt.days
        df4['Last_EPCR']=df4['Last_EPCR'].fillna(999)
        df4=df4.drop(columns=['Win','Last_5_W/L','Time'])
        df1.append(df4)
    else:
        continue
epcr3=pd.concat(df1)

df1=[]
for i in away_teams:
    df3=epcr3[(epcr3['Home Team'].str.contains(i)) | (epcr3['Away Team'].str.contains(i))]
    if len(df3) > 0:
        df3.loc[((df3['Home Team'].str.contains(i))&(df3['Home Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3.loc[((df3['Away Team'].str.contains(i))&(df3['Away Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3['Win']=df3['Win'].fillna(0)
        df3=df3.sort_values(by=['Date'])
        df3['Last_5_W/L']=df3['Win'].rolling(5).sum()
        df3.loc[(df3['Away Team']==(i)),'Away Last_5_W/L_EPCR']=df3['Last_5_W/L']
        df3['Away Last_5_W/L_EPCR']=df3['Away Last_5_W/L_EPCR'].fillna(999)
        df4=df3[(df3['Away Team']==(i))]
        df4=df4.drop(columns=['Win','Last_5_W/L'])
        df1.append(df4)
    else:
        continue
epcr4=pd.concat(df1)

df1=[]
for i in home_teams:
    df3=pro142[(pro142['Home Team'].str.contains(i)) | (pro142['Away Team'].str.contains(i))]
    if len(df3) > 0:
        df3.loc[((df3['Home Team'].str.contains(i))&(df3['Home Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3.loc[((df3['Away Team'].str.contains(i))&(df3['Away Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3['Win']=df3['Win'].fillna(0)
        df3=df3.sort_values(by=['Date'])
        df3['Last_5_W/L']=df3['Win'].rolling(5).sum()
        df3.loc[(df3['Home Team']==(i)),'Home Last_5_W/L_P14']=df3['Last_5_W/L']
        df3['Home Last_5_W/L_P14']=df3['Home Last_5_W/L_P14'].fillna(999)
        df4=df3[(df3['Home Team']==(i))]
        df4['Time']=df4['Date']-df4['Date'].shift(1)
        df4['Last_P14']=df4['Time'].dt.days
        df4['Last_P14']=df4['Last_P14'].fillna(999)
        df4=df4.drop(columns=['Win','Last_5_W/L','Time'])
        df1.append(df4)
    else:
        continue
pro143=pd.concat(df1)

df1=[]
for i in away_teams:
    df3=pro143[(pro143['Home Team'].str.contains(i)) | (pro143['Away Team'].str.contains(i))]
    if len(df3) > 0:
        df3.loc[((df3['Home Team'].str.contains(i))&(df3['Home Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3.loc[((df3['Away Team'].str.contains(i))&(df3['Away Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3['Win']=df3['Win'].fillna(0)
        df3=df3.sort_values(by=['Date'])
        df3['Last_5_W/L']=df3['Win'].rolling(5).sum()
        df3.loc[(df3['Away Team']==(i)),'Away Last_5_W/L_P14']=df3['Last_5_W/L']
        df3['Away Last_5_W/L_P14']=df3['Away Last_5_W/L_P14'].fillna(999)
        df4=df3[(df3['Away Team']==(i))]
        df4=df4.drop(columns=['Win','Last_5_W/L'])
        df1.append(df4)
    else:
        continue
pro144=pd.concat(df1)


games2=pro144.append(epcr4)
df1=[]
for i in home_teams:
    df3=games2[(games2['Home Team'].str.contains(i)) | (games2['Away Team'].str.contains(i))]
    if len(df3) > 0:
        df3.loc[((df3['Home Team'].str.contains(i))&(df3['Home Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3.loc[((df3['Away Team'].str.contains(i))&(df3['Away Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3['Win']=df3['Win'].fillna(0)
        df3=df3.sort_values(by=['Date'])
        df3['Last_5_W/L']=df3['Win'].shift(1).rolling(5).sum()
        df3.loc[(df3['Home Team']==(i)),'Home Last_5_W/L']=df3['Last_5_W/L']
        df3['Home Last_5_W/L']=df3['Home Last_5_W/L'].fillna(999)
        df4=df3[(df3['Home Team']==(i))]
        df4['Time']=df4['Date']-df4['Date'].shift(1)
        df4['LastGame']=df4['Time'].dt.days
        df4['LastGame']=df4['Last_P14'].fillna(999)
        df4=df4.drop(columns=['Win','Last_5_W/L','Time'])
        df1.append(df4)
    else:
        continue
games3=pd.concat(df1)

df1=[]
for i in away_teams:
    df3=games3[(games3['Home Team'].str.contains(i)) | (games3['Away Team'].str.contains(i))]
    if len(df3) > 0:
        df3.loc[((df3['Home Team'].str.contains(i))&(df3['Home Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3.loc[((df3['Away Team'].str.contains(i))&(df3['Away Win/loss/draw'].str.contains('Win'))),'Win']=1
        df3['Win']=df3['Win'].fillna(0)
        df3=df3.sort_values(by=['Date'])
        df3['Last_5_W/L']=df3['Win'].shift(1).rolling(5).sum()
        df3.loc[(df3['Away Team']==(i)),'Away Last_5_W/L']=df3['Last_5_W/L']
        df3['Away Last_5_W/L']=df3['Away Last_5_W/L'].fillna(999)
        df4=df3[(df3['Away Team']==(i))]
        df4=df4.drop(columns=['Win','Last_5_W/L'])
        df1.append(df4)
    else:
        continue
games4=pd.concat(df1)

games4.info()

games4=games4[(games4['Home Team'].str.contains('Benetton Rugby|Benetton Treviso|Cardiff Blues|Connacht Rugby|Dragons|Edinburgh Rugby|Glasgow Warriors|Leinster Rugby|Munster Rugby|Newport Gwent Dragons|Ospreys|Scarlets|Southern Kings|Ulster Rugby|Zebre Rugby|Zebre Rugby Club'))]
games4['Round']=games4['Round'].astype(int)
games4.loc[((games4['Round']>6)&(games4['Tournament'].str.contains('Champions Cup|Challenge Cup'))),'Pool Stage']='Knock Out'
games4.loc[((games4['Round']<7)&(games4['Tournament'].str.contains('Champions Cup|Challenge Cup'))),'Pool Stage']='Pool'
games4.loc[((games4['Round']>21)&(games4['Tournament'].str.contains('League'))&(games4['Season'].str.contains('2018/2019 Season|2017/2018 Season'))),'Pool Stage']='Knock Out'
games4.loc[((games4['Round']<22)&(games4['Tournament'].str.contains('League'))&(games4['Season'].str.contains('2018/2019 Season|2017/2018 Season'))),'Pool Stage']='Pool'
games4.loc[((games4['Round']>22)&(games4['Tournament'].str.contains('League'))&(games4['Season'].str.contains('2015/2016 Season|2016/2017 Season'))),'Pool Stage']='Knock Out'
games4.loc[((games4['Round']<23)&(games4['Tournament'].str.contains('League'))&(games4['Season'].str.contains('2015/2016 Season|2016/2017 Season'))),'Pool Stage']='Pool'
games5=games4[(games4['Pool Stage'].str.contains('Pool'))]
games5=games5[(games5['Attendance'].notnull())]       
games5['Attendance'] = games5['Attendance'].map(lambda x: x.lstrip('Att: '))
games5['Attendance'] = games5['Attendance'].map(lambda x: x.replace(',',''))
games5['Attendance'] = games5['Attendance'].astype(int)
games5['Date'] = games5['Date'].map(lambda x: x.strftime('%Y-%m-%d'))
df=pd.pivot_table(games5, index='Venue', values = None).reset_index()
stadium=list(df['Venue'])

def seturl(row):
    if row['Venue']=='AVIVA Stadium':
        x='https://www.worldweatheronline.com/dublin-weather-history/dublin/ie.aspx'
    elif row['Venue']=='Aviva Stadium':
        x='https://www.worldweatheronline.com/dublin-weather-history/dublin/ie.aspx'
    elif row['Venue']=='BT Murrayfield':
        x='https://www.worldweatheronline.com/edinburgh-weather-history/city-of-edinburgh/gb.aspx'
    elif row['Venue']=='BT Murrayfield Stadium':
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
    elif row['Venue']=='The Sportsground':
        x='https://www.worldweatheronline.com/galway-weather-history/galway/ie.aspx'
    elif row['Venue']=='Stadio Comunale di Monigo':
        x='https://www.worldweatheronline.com/treviso-weather-history/veneto/it.aspx'
    elif row['Venue']=='Stadio Monigo':
        x='https://www.worldweatheronline.com/treviso-weather-history/veneto/it.aspx'
    elif row['Venue']=='Stadio Sergio Lanfranchi':
        x='https://www.worldweatheronline.com/parma-weather-history/emilia-romagna/it.aspx'
    elif row['Venue']=='La Ghirada':
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
        x=np.nan
    return x
    
games5['Stadium URL']=games5.apply(lambda row:seturl(row), axis=1) 
check=games5[(games5['Stadium URL'].isnull())]

savedfile=games5.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation1.csv', index=False) 

def test(row):
    if row['Tournament']=='League':
        x='Test 1'
    if row['Tournament']=='League':
        y='Test 2'
    return x,y
    
games5['test']=games5.apply(lambda row:test(row), axis=1) 
    
