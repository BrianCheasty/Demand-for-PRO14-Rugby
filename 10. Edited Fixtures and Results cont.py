import pandas as pd
import numpy as np

gamesa=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation2.csv',encoding='latin-1')
gamesb=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation2b.csv',encoding='latin-1')
games=gamesa.append(gamesb)
games=games.reset_index()
games=games.drop(columns=['index'])
#games=games[(games['Home Team']!=('Southern Kings'))]
#games=games[(games['Away Team']!=('Southern Kings'))]
games['Last_EPCR']=games['Last_EPCR'].fillna(0)
games['Last_P14']=games['Last_P14'].fillna(0)
games['Last Game in Comp']=games['Last_P14']+games['Last_EPCR']
games=games.drop(columns=['Last_EPCR','Last_P14'])

games['Home Last_5_W/L_P14']=games['Home Last_5_W/L_P14'].fillna(0)
games['Home Last_5_W/L_EPCR']=games['Home Last_5_W/L_EPCR'].fillna(0)
games['Home Win/Loss in Comp']=games['Home Last_5_W/L_P14']+games['Home Last_5_W/L_EPCR']
games=games.drop(columns=['Home Last_5_W/L_P14','Home Last_5_W/L_EPCR'])

games['Away Last_5_W/L_P14']=games['Away Last_5_W/L_P14'].fillna(0)
games['Away Last_5_W/L_EPCR']=games['Away Last_5_W/L_EPCR'].fillna(0)
games['Away Win/Loss in Comp']=games['Away Last_5_W/L_P14']+games['Away Last_5_W/L_EPCR']
games=games.drop(columns=['Away Last_5_W/L_P14','Away Last_5_W/L_EPCR','Ref','Home Total Tries','Away Total Tries',\
                          'Home Total Metres Gained','Away Total Metres Gained','Home Total Passes Made','Away Total Passes Made',\
                          'Home Total Tackles Made','Away Total Tackles Made','Home Total Turnovers Won','Away Total Turnovers Won',\
                          'Home Total Penalties Conceded','Away Total Penalties Conceded'])
games['Played']=games['Played'].fillna(games['Home Wins']+games['Away Wins']+games['Draws'])

teams=list(games['Home Team'].drop_duplicates())
season=list(games['Season'].drop_duplicates())
rounds=list(games['Round'].drop_duplicates())
teamsAway=list(games['Away Team'].drop_duplicates())
stadium=list(games['Venue'].drop_duplicates())




def tries(row):
    if i in row['Home Team']:
        x=row['Home Score']
        if int(x/7)>3:
            add=1
        else:
            add=0
        if 'Win' in row['Home Win/loss/draw']:
            y=4
        elif 'Draw' in row['Home Win/loss/draw']:
            y=2
        else:
            y=0
        points=add+y
    elif i in row['Away Team']:
        x=row['Away Score']
        if int(x/7)>3:
            add=1
        else:
            add=0
        if 'Win' in row['Away Win/loss/draw']:
            y=4
        elif 'Draw' in row['Away Win/loss/draw']:
            y=2
        else:
            y=0
        points=add+y
    return points

gamesA=[]
for i in teams:
    df=[]
    df1=games[(games['Home Team'].str.contains(i)) | (games['Away Team'].str.contains(i))]
    for j in season:
        df2=df1[(df1['Season'].str.contains(j))]
        if len(df2)==0:
            continue
        else:
            df2=df2.sort_values(by=['Date'])
            df2['Home Points']=df2.apply(lambda row: tries(row), axis=1)
            df2['Home Total P']=df2['Home Points'].expanding(1).sum()
            df2['Home Total Points']=df2['Home Total P'].shift(1)
            df2['Total Points Avail TD']=(df2['Round'].shift(1))*5
            df3=df2[(df2['Home Team'].str.contains(i))]
            df.append(df3)
    df4=pd.concat(df)
    gamesA.append(df4)
gamesB=pd.concat(gamesA) 



gamesB['Date']=pd.to_datetime(gamesB['Date'])
gamesB['Day Of Week']=gamesB['Date'].dt.dayofweek
gamesB['Month of Year']=gamesB['Date'].dt.month

checktime=pd.pivot_table(gamesB,index='Kick Off', columns='Home Team', values='Date',aggfunc='count')

gamesB['Kick Off']=gamesB['Kick Off'].fillna('16:00:00')
def time(row):
    ko=row['Kick Off'].split(':')
    ko2=int(ko[0])
    if ko2 < 14:
        x='Early'
    elif ko2 >= 14:
        if ko2 < 18:
            x='Afternoon'
        else:
            x='Evening'
    return x
gamesB['Kick Off Hour']=gamesB.apply(lambda row:time(row), axis=1) 

gamesB['Home Winning Percentage']=round(gamesB['Home Total Points']/gamesB['Total Points Avail TD'],2)
gamesB['Home Winning Percentage']=gamesB['Home Winning Percentage'].fillna(0)

gamesB.loc[((gamesB['Home Team'].str.contains('Munster|Leinster|Connacht|Ulster'))&(gamesB['Away Team'].str.contains('Munster|Leinster|Connacht|Ulster'))),'Derby']='Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Edinburgh|Glasgow'))&(gamesB['Away Team'].str.contains('Edinburgh|Glasgow'))),'Derby']='Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Kings|Cheetahs'))&(gamesB['Away Team'].str.contains('Kings|Cheetahs'))),'Derby']='Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Treviso|Zebre'))&(gamesB['Away Team'].str.contains('Treviso|Zebre'))),'Derby']='Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Ospreys|Dragons|Cardiff|Scarlets'))&(gamesB['Away Team'].str.contains('Ospreys|Dragons|Cardiff|Scarlets'))),'Derby']='Derby'
gamesB['Derby']=gamesB['Derby'].fillna('Non Derby')
gamesB['homeVSaway Winning Percentage']=round(gamesB['Home Wins']/gamesB['Played'],2)
gamesB['homeVSaway Winning Percentage']=gamesB['homeVSaway Winning Percentage'].fillna(0.5)
check=gamesB[(gamesB['homeVSaway Winning Percentage'].isnull())]

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Leinster'))),'Number ofP14 Wins']=5
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Leinster'))),'Number ofP14 Wins']=4
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Leinster'))),'Number ofP14 Wins']=3
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Leinster'))),'Number ofP14 Wins']=3
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Leinster'))),'Number ofEPCR Wins']=4
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Leinster'))),'Number ofEPCR Wins']=3
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Leinster'))),'Number ofEPCR Wins']=3
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Leinster'))),'Number ofEPCR Wins']=3

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Number ofP14 Wins']=4
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Number ofP14 Wins']=4
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Number ofP14 Wins']=4
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Number ofP14 Wins']=4
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Number ofEPCR Wins']=0

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Munster'))),'Number ofP14 Wins']=3
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Munster'))),'Number ofP14 Wins']=3
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Munster'))),'Number ofP14 Wins']=3
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Munster'))),'Number ofP14 Wins']=3
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Munster'))),'Number ofEPCR Wins']=2
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Munster'))),'Number ofEPCR Wins']=2
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Munster'))),'Number ofEPCR Wins']=2
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Munster'))),'Number ofEPCR Wins']=2

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Number ofP14 Wins']=2
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Number ofP14 Wins']=2
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Number ofEPCR Wins']=0

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Ulster'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Ulster'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Ulster'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Ulster'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Ulster'))),'Number ofEPCR Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Ulster'))),'Number ofEPCR Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Ulster'))),'Number ofEPCR Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Ulster'))),'Number ofEPCR Wins']=1

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Connacht'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Connacht'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Connacht'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Connacht'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Connacht'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Connacht'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Connacht'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Connacht'))),'Number ofEPCR Wins']=0

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Number ofP14 Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Number ofEPCR Wins']=0

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Number ofEPCR Wins']=0

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Number ofEPCR Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Number ofEPCR Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Number ofEPCR Wins']=1
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Number ofEPCR Wins']=1

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Zebre'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Zebre'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Zebre'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Zebre'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Zebre'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Zebre'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Zebre'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Zebre'))),'Number ofEPCR Wins']=0

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Treviso'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Treviso'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Treviso'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Treviso'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Treviso'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Treviso'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Treviso'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Treviso'))),'Number ofEPCR Wins']=0

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Dragons'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Dragons'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Dragons'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Dragons'))),'Number ofP14 Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Dragons'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Dragons'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Dragons'))),'Number ofEPCR Wins']=0
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Dragons'))),'Number ofEPCR Wins']=0

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Leinster'))),'Years sinceP14 Win']=0
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Leinster'))),'Years sinceP14 Win']=0
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Leinster'))),'Years sinceP14 Win']=3
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Leinster'))),'Years sinceP14 Win']=2
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Leinster'))),'Years sinceEPCR Win']=1
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Leinster'))),'Years sinceEPCR Win']=6
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Leinster'))),'Years sinceEPCR Win']=5
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Leinster'))),'Years sinceEPCR Win']=4

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Years sinceP14 Win']=7
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Years sinceP14 Win']=6
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Years sinceP14 Win']=5
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Years sinceP14 Win']=4
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Ospreys'))),'Years sinceEPCR Win']=25

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Munster'))),'Years sinceP14 Win']=8
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Munster'))),'Years sinceP14 Win']=7
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Munster'))),'Years sinceP14 Win']=6
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Munster'))),'Years sinceP14 Win']=5
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Munster'))),'Years sinceEPCR Win']=11
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Munster'))),'Years sinceEPCR Win']=10
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Munster'))),'Years sinceEPCR Win']=9
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Munster'))),'Years sinceEPCR Win']=8

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Years sinceP14 Win']=2
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Years sinceP14 Win']=1
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Years sinceP14 Win']=16
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Years sinceP14 Win']=16
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Scarlets'))),'Years sinceEPCR Win']=25

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Ulster'))),'Years sinceP14 Win']=13
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Ulster'))),'Years sinceP14 Win']=12
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Ulster'))),'Years sinceP14 Win']=11
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Ulster'))),'Years sinceP14 Win']=10
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Ulster'))),'Years sinceEPCR Win']=18
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Ulster'))),'Years sinceEPCR Win']=17
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Ulster'))),'Years sinceEPCR Win']=16
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Ulster'))),'Years sinceEPCR Win']=15

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Connacht'))),'Years sinceP14 Win']=3
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Connacht'))),'Years sinceP14 Win']=2
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Connacht'))),'Years sinceP14 Win']=1
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Connacht'))),'Years sinceP14 Win']=14
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Connacht'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Connacht'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Connacht'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Connacht'))),'Years sinceEPCR Win']=25

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Years sinceP14 Win']=4
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Years sinceP14 Win']=3
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Years sinceP14 Win']=2
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Years sinceP14 Win']=1
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Glasgow'))),'Years sinceEPCR Win']=25

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Edinburgh'))),'Years sinceEPCR Win']=25

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Years sinceEPCR Win']=22
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Years sinceEPCR Win']=21
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Years sinceEPCR Win']=20
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Cardiff'))),'Years sinceEPCR Win']=19

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Zebre'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Zebre'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Zebre'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Zebre'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Zebre'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Zebre'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Zebre'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Zebre'))),'Years sinceEPCR Win']=25

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Treviso'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Treviso'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Treviso'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Treviso'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Treviso'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Treviso'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Treviso'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Treviso'))),'Years sinceEPCR Win']=25

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Dragons'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Dragons'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Dragons'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Dragons'))),'Years sinceP14 Win']=19
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Home Team'].str.contains('Dragons'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Home Team'].str.contains('Dragons'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Home Team'].str.contains('Dragons'))),'Years sinceEPCR Win']=25
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Home Team'].str.contains('Dragons'))),'Years sinceEPCR Win']=25

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Liberty Stadium'))),'Stadium Age']=13
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Liberty Stadium'))),'Stadium Age']=12
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Liberty Stadium'))),'Stadium Age']=11
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Liberty Stadium'))),'Stadium Age']=10
gamesB.loc[(gamesB['Venue'].str.contains('Liberty Stadium')),'Stadium Capacity']=21088

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Rodney'))),'Stadium Age']=141
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Rodney'))),'Stadium Age']=140
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Rodney'))),'Stadium Age']=139
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Rodney'))),'Stadium Age']=138
gamesB.loc[(gamesB['Venue'].str.contains('Rodney')),'Stadium Capacity']=8700

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Murrayfield'))),'Stadium Age']=23
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Murrayfield'))),'Stadium Age']=22
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Murrayfield'))),'Stadium Age']=21
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Murrayfield'))),'Stadium Age']=20
gamesB.loc[(gamesB['Venue'].str.contains('Murrayfield')),'Stadium Capacity']=67144

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Lanfranchi'))),'Stadium Age']=10
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Lanfranchi'))),'Stadium Age']=9
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Lanfranchi'))),'Stadium Age']=8
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Lanfranchi'))),'Stadium Age']=7
gamesB.loc[(gamesB['Venue'].str.contains('Lanfranchi')),'Stadium Capacity']=5000

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Monigo'))),'Stadium Age']=45
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Monigo'))),'Stadium Age']=44
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Monigo'))),'Stadium Age']=43
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Monigo'))),'Stadium Age']=42
gamesB.loc[(gamesB['Venue'].str.contains('Monigo')),'Stadium Capacity']=6700

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('RDS'))),'Stadium Age']=9
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('RDS'))),'Stadium Age']=8
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('RDS'))),'Stadium Age']=7
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('RDS'))),'Stadium Age']=6
gamesB.loc[(gamesB['Venue'].str.contains('RDS')),'Stadium Capacity']=18500

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Cardiff'))),'Stadium Age']=20
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Cardiff'))),'Stadium Age']=19
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Cardiff'))),'Stadium Age']=18
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Cardiff'))),'Stadium Age']=17
gamesB.loc[(gamesB['Venue'].str.contains('Cardiff')),'Stadium Capacity']=53000

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Scarlets'))),'Stadium Age']=9
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Scarlets'))),'Stadium Age']=8
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Scarlets'))),'Stadium Age']=7
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Scarlets'))),'Stadium Age']=6
gamesB.loc[(gamesB['Venue'].str.contains('Scarlets')),'Stadium Capacity']=14870

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Aviva'))),'Stadium Age']=9
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Aviva'))),'Stadium Age']=8
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Aviva'))),'Stadium Age']=7
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Aviva'))),'Stadium Age']=6
gamesB.loc[(gamesB['Venue'].str.contains('Aviva')),'Stadium Capacity']=51700

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Independent'))),'Stadium Age']=3
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Independent'))),'Stadium Age']=2
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Independent'))),'Stadium Age']=1
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Independent'))),'Stadium Age']=0
gamesB.loc[(gamesB['Venue'].str.contains('Independent')),'Stadium Capacity']=8008

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Kingspan'))),'Stadium Age']=4
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Kingspan'))),'Stadium Age']=3
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Kingspan'))),'Stadium Age']=2
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Kingspan'))),'Stadium Age']=1
gamesB.loc[(gamesB['Venue'].str.contains('Kingspan')),'Stadium Capacity']=18196

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Sportsground'))),'Stadium Age']=91
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Sportsground'))),'Stadium Age']=90
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Sportsground'))),'Stadium Age']=89
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Sportsground'))),'Stadium Age']=88
gamesB.loc[(gamesB['Venue'].str.contains('Sportsground')),'Stadium Capacity']=8129

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Thomond'))),'Stadium Age']=10
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Thomond'))),'Stadium Age']=9
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Thomond'))),'Stadium Age']=8
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Thomond'))),'Stadium Age']=7
gamesB.loc[(gamesB['Venue'].str.contains('Thomond')),'Stadium Capacity']=25600

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Scotstoun'))),'Stadium Age']=8
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Scotstoun'))),'Stadium Age']=7
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Scotstoun'))),'Stadium Age']=6
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Scotstoun'))),'Stadium Age']=5
gamesB.loc[(gamesB['Venue'].str.contains('Scotstoun')),'Stadium Capacity']=4765

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Myreside'))),'Stadium Age']=81
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Myreside'))),'Stadium Age']=80
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Myreside'))),'Stadium Age']=79
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Myreside'))),'Stadium Age']=78
gamesB.loc[(gamesB['Venue'].str.contains('Myreside')),'Stadium Capacity']=5500

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Constructaquote'))),'Stadium Age']=131
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Constructaquote'))),'Stadium Age']=130
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Constructaquote'))),'Stadium Age']=129
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Constructaquote'))),'Stadium Age']=128
gamesB.loc[(gamesB['Venue'].str.contains('Constructaquote')),'Stadium Capacity']=6000

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Morganstone'))),'Stadium Age']=98
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Morganstone'))),'Stadium Age']=97
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Morganstone'))),'Stadium Age']=96
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Morganstone'))),'Stadium Age']=95
gamesB.loc[(gamesB['Venue'].str.contains('Morganstone')),'Stadium Capacity']=8000

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Fattori'))),'Stadium Age']=81
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Fattori'))),'Stadium Age']=80
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Fattori'))),'Stadium Age']=79
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Fattori'))),'Stadium Age']=78
gamesB.loc[(gamesB['Venue'].str.contains('Fattori')),'Stadium Capacity']=10000

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Eugene'))),'Stadium Age']=99
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Eugene'))),'Stadium Age']=98
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Eugene'))),'Stadium Age']=98
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Eugene'))),'Stadium Age']=96
gamesB.loc[(gamesB['Venue'].str.contains('Eugene')),'Stadium Capacity']=8000

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Ghirada'))),'Stadium Age']=33
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Ghirada'))),'Stadium Age']=32
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Ghirada'))),'Stadium Age']=31
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Ghirada'))),'Stadium Age']=30
gamesB.loc[(gamesB['Venue'].str.contains('Ghirada')),'Stadium Capacity']=6000
 
gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Meggetland'))),'Stadium Age']=12
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Meggetland'))),'Stadium Age']=11
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Meggetland'))),'Stadium Age']=10
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Meggetland'))),'Stadium Age']=9
gamesB.loc[(gamesB['Venue'].str.contains('Meggetland')),'Stadium Capacity']=4388

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Zaffanella'))),'Stadium Age']=8
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Zaffanella'))),'Stadium Age']=7
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Zaffanella'))),'Stadium Age']=6
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Zaffanella'))),'Stadium Age']=5
gamesB.loc[(gamesB['Venue'].str.contains('Zaffanella')),'Stadium Capacity']=6000

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Rugby Park'))),'Stadium Age']=23
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Rugby Park'))),'Stadium Age']=22
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Rugby Park'))),'Stadium Age']=21
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Rugby Park'))),'Stadium Age']=20
gamesB.loc[(gamesB['Venue'].str.contains('Rugby Park')),'Stadium Capacity']=18128

gamesB.loc[((gamesB['Season'].str.contains('2018/2019'))&(gamesB['Venue'].str.contains('Principality'))),'Stadium Age']=21
gamesB.loc[((gamesB['Season'].str.contains('2017/2018'))&(gamesB['Venue'].str.contains('Principality'))),'Stadium Age']=20
gamesB.loc[((gamesB['Season'].str.contains('2016/2017'))&(gamesB['Venue'].str.contains('Principality'))),'Stadium Age']=19
gamesB.loc[((gamesB['Season'].str.contains('2015/2016'))&(gamesB['Venue'].str.contains('Principality'))),'Stadium Age']=18
gamesB.loc[(gamesB['Venue'].str.contains('Principality')),'Stadium Capacity']=74500

gamesB['Stadium Percentage']=round(gamesB['Attendance']/gamesB['Stadium Capacity'],2)
check=gamesB[(gamesB['Stadium Percentage']>0.99)]
gamesB=gamesB.rename(columns={'Home Table Pos':'Home Table Position','Away Table Pos':'Away Table Position'})
league=gamesB[(gamesB['Tournament'].str.contains('League'))]
cup=gamesB[(gamesB['Tournament'].str.contains('Cup'))]


league.loc[((league['Home Team'].str.contains('Munster'))&league['Home Table Position'].isnull()),'Home Table Position']=2
league.loc[((league['Away Team'].str.contains('Munster'))&league['Away Table Position'].isnull()),'Home Table Position']=2
league.loc[((league['Home Team'].str.contains('Glasgow'))&league['Home Table Position'].isnull()),'Home Table Position']=1
league.loc[((league['Away Team'].str.contains('Glasgow'))&league['Away Table Position'].isnull()),'Home Table Position']=1
league.loc[((league['Home Team'].str.contains('Ospreys'))&league['Home Table Position'].isnull()),'Home Table Position']=3
league.loc[((league['Away Team'].str.contains('Ospreys'))&league['Away Table Position'].isnull()),'Home Table Position']=3
league.loc[((league['Home Team'].str.contains('Ulster'))&league['Home Table Position'].isnull()),'Home Table Position']=4
league.loc[((league['Away Team'].str.contains('Ulster'))&league['Away Table Position'].isnull()),'Home Table Position']=4
league.loc[((league['Home Team'].str.contains('Leinster'))&league['Home Table Position'].isnull()),'Home Table Position']=5
league.loc[((league['Away Team'].str.contains('Leinster'))&league['Away Table Position'].isnull()),'Home Table Position']=5
league.loc[((league['Home Team'].str.contains('Scarlets'))&league['Home Table Position'].isnull()),'Home Table Position']=6
league.loc[((league['Away Team'].str.contains('Scarlets'))&league['Away Table Position'].isnull()),'Home Table Position']=6
league.loc[((league['Home Team'].str.contains('Connacht'))&league['Home Table Position'].isnull()),'Home Table Position']=7
league.loc[((league['Away Team'].str.contains('Connacht'))&league['Away Table Position'].isnull()),'Home Table Position']=7
league.loc[((league['Home Team'].str.contains('Edinburgh'))&league['Home Table Position'].isnull()),'Home Table Position']=8
league.loc[((league['Away Team'].str.contains('Edinburgh'))&league['Away Table Position'].isnull()),'Home Table Position']=8
league.loc[((league['Home Team'].str.contains('Dragons'))&league['Home Table Position'].isnull()),'Home Table Position']=9
league.loc[((league['Away Team'].str.contains('Dragons'))&league['Away Table Position'].isnull()),'Home Table Position']=9
league.loc[((league['Home Team'].str.contains('Cardiff'))&league['Home Table Position'].isnull()),'Home Table Position']=10
league.loc[((league['Away Team'].str.contains('Cardiff'))&league['Away Table Position'].isnull()),'Home Table Position']=10
league.loc[((league['Home Team'].str.contains('Benetton'))&league['Home Table Position'].isnull()),'Home Table Position']=11
league.loc[((league['Away Team'].str.contains('Benetton'))&league['Away Table Position'].isnull()),'Home Table Position']=11
league.loc[((league['Home Team'].str.contains('Zebre'))&league['Home Table Position'].isnull()),'Home Table Position']=12
league.loc[((league['Away Team'].str.contains('Zebre'))&league['Away Table Position'].isnull()),'Home Table Position']=12

cup.loc[((cup['Home Team'].str.contains('Munster'))&cup['Home Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Munster'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Home Team'].str.contains('Glasgow'))&cup['Home Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Glasgow'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Home Team'].str.contains('Ospreys'))&cup['Home Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Ospreys'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Home Team'].str.contains('Ulster'))&cup['Home Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Ulster'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Home Team'].str.contains('Leinster'))&cup['Home Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Leinster'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Home Team'].str.contains('Scarlets'))&cup['Home Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Away Team'].str.contains('Scarlets'))&cup['Away Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Home Team'].str.contains('Connacht'))&cup['Home Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('Connacht'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Home Team'].str.contains('Edinburgh'))&cup['Home Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Edinburgh'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Home Team'].str.contains('Dragons'))&cup['Home Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Dragons'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Home Team'].str.contains('Cardiff'))&cup['Home Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('Cardiff'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Home Team'].str.contains('Benetton'))&cup['Home Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Away Team'].str.contains('Benetton'))&cup['Away Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Home Team'].str.contains('Zebre'))&cup['Home Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Zebre'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Clermont'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Saracens'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('Sale'))&cup['Away Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Away Team'].str.contains('Wasps'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('Harlequins'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Castres'))&cup['Away Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Away Team'].str.contains('Toulon'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Leicester'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('Bath'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Toulouse'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('Montpellier'))&cup['Away Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Away Team'].str.contains('Racing'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Northampton'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('London Irish'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Grenoble'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Rovigo'))&cup['Away Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Away Team'].str.contains('Exeter'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Bayonne'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Rochelle'))&cup['Away Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Away Team'].str.contains('Falcons'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('Francais'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('Bucharest'))&cup['Away Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Away Team'].str.contains('Lyon'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('Begles'))&cup['Away Table Position'].isnull()),'Home Table Position']=3
cup.loc[((cup['Away Team'].str.contains('London Welsh'))&cup['Away Table Position'].isnull()),'Home Table Position']=4
cup.loc[((cup['Away Team'].str.contains('Gloucester'))&cup['Away Table Position'].isnull()),'Home Table Position']=1
cup.loc[((cup['Away Team'].str.contains('Oyonnax'))&cup['Away Table Position'].isnull()),'Home Table Position']=2
cup.loc[((cup['Away Team'].str.contains('Brive'))&cup['Away Table Position'].isnull()),'Home Table Position']=4


check=league[(league['Home Table Position'].isnull())]
league.loc[league['Season'].str.contains('2015/2016 Season|2016/2017 Season'),'Table Difference']=(league['Home Table Position']-league['Away Table Position'])
league.loc[league['Season'].str.contains('2017/2018 Season|2018/2019 Season'),'Table Difference']=(((league['Home Table Position']-league['Away Table Position'])+1)*2)
cup['Table Difference']=((cup['Home Table Position']-cup['Away Table Position']))*4


league.loc[((league['Season'].str.contains('2015/2016|2016/2017'))&(league['Home Table Position']==4)),'Table Marker']=4
league.loc[((league['Season'].str.contains('2015/2016|2016/2017'))&(league['Away Table Position']==4)),'Table Marker']=4
league.loc[((league['Season'].str.contains('2015/2016|2016/2017'))&(league['Home Table Position']==3)),'Table Marker']=3
league.loc[((league['Season'].str.contains('2015/2016|2016/2017'))&(league['Away Table Position']==3)),'Table Marker']=3
league.loc[((league['Season'].str.contains('2017/2018|2018/2019'))&(league['Home Table Position']==3)),'Table Marker']=3
league.loc[((league['Season'].str.contains('2017/2018|2018/2019'))&(league['Away Table Position']==3)),'Table Marker']=3
league.loc[((league['Season'].str.contains('2017/2018|2018/2019'))&(league['Home Table Position']==4)),'Table Marker']=4
league.loc[((league['Season'].str.contains('2017/2018|2018/2019'))&(league['Away Table Position']==4)),'Table Marker']=4

cup.loc[cup['Home Table Position']==1,'Table Marker']=1
cup.loc[cup['Away Table Position']==1,'Table Marker']=1
cup.loc[cup['Home Table Position']==2,'Table Marker']=2
cup.loc[cup['Away Table Position']==2,'Table Marker']=2

league.loc[league['Season'].str.contains('2015/2016|2016/2017'),'Points Left']=(23-league['Round'])*5
league.loc[league['Season'].str.contains('2017/2018|2018/2019'),'Points Left']=(22-league['Round'])*5
cup['Points Left']=(7-cup['Round'])*5
def competitveness1517(row,d):
    if (row['Home Total Points']+row['Points Left'])< d:
        z='Cant Qualify'
    elif (row['Home Total Points']+row['Points Left'])>= d:
        if (row['Home Total Points']-row['Points Left'])> d:
            z='Has Qualified'
        else:
            z='Can Still Qualify'
    else:
        z='Check Problem'
    return z
def competitveness1719(row,d):
    if (row['Home Total Points']+row['Points Left'])< d:
        z='Cant Qualify'
    elif (row['Home Total Points']+row['Points Left'])>= d:
        if (row['Home Total Points']-row['Points Left'])> d:
            z='Has Qualified'
        else:
            z='Can Still Qualify'
    else:
        z='Check Problem'
    return z

def epcrcompetitveness(row,d):
    if (row['Home Total Points']+row['Points Left'])< d:
        z='Cant Qualify'
    elif (row['Home Total Points']+row['Points Left'])>= d:
        if (row['Home Total Points']-row['Points Left'])> d:
            z='Has Qualified'
        else:
            z='Can Still Qualify'
    else:
        z='Check Problem'
    return z


league['Table Marker']=league['Table Marker'].fillna(0)
cup['Table Marker']=cup['Table Marker'].fillna(0)

season22=['2015/2016 Season','2016/2017 Season']
round22=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
league2=[]
for i in season22:
    dflist=[]
    df=league[(league['Season'].str.contains(i))]
    for j in round22:
        df2=df[(df['Round']==j)]
        dfcomb=[]
        a=df2[(df2['Table Marker']==4)]
        print(len(a))
        if len(a)==0:
            a1=df2[(df2['Table Marker']==3)]
            b=a1[['Home Total Points']]
            c=list(b['Home Total Points'])
            d=c[0]
            print(d)
            df2['Game Competitiveness']=df2.apply(lambda row: competitveness1517(row,d), axis=1 )
        else:
            b=a[['Home Total Points']]
            c=list(b['Home Total Points'])
            d=c[0]
            print(d)
            df2['Game Competitiveness']=df2.apply(lambda row: competitveness1517(row,d), axis=1 )
        dflist.append(df2)
    dfconcat=pd.concat(dflist)
    league2.append(dfconcat)
    
season22=['2017/2018 Season','2018/2019 Season']
round22=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
for i in season22:
    dflist=[]
    df=league[(league['Season'].str.contains(i))]
    for j in round22:
        df2=df[(df['Round']==j)]
        dfcomb=[]
        a=df2[(df2['Table Marker']==4)]
        print(len(a))
        if len(a)==0:
            a1=df2[(df2['Table Marker']==3)]
            b=a1[['Home Total Points']]
            c=list(b['Home Total Points'])
            d=c[0]
            print(d)
            df2['Game Competitiveness']=df2.apply(lambda row: competitveness1517(row,d), axis=1 )
        else:
            b=a[['Home Total Points']]
            c=list(b['Home Total Points'])
            d=c[0]
            print(d)
            df2['Game Competitiveness']=df2.apply(lambda row: competitveness1517(row,d), axis=1 )
        dflist.append(df2)
    dfconcat=pd.concat(dflist)
    league2.append(dfconcat)    
league3=pd.concat(league2)
        

roundsepcr=[1,2,3,4,5,6]
cup2=[]
for i in season:
    dflist=[]
    df=cup[(cup['Season'].str.contains(i))]
    for j in roundsepcr:
        df2=df[(df['Round']==j)]
        dfcomb=[]
        a=df2[(df2['Table Marker']==1)]
        print(len(a))
        if len(a)==0:
            a1=df2[(df2['Table Marker']==2)]
            b=a1[['Home Total Points']]
            c=list(b['Home Total Points'])
            d=c[0]
            print(d)
            df2['Game Competitiveness']=df2.apply(lambda row: epcrcompetitveness(row,d), axis=1 )
        else:
            b=a[['Home Total Points']]
            c=list(b['Home Total Points'])
            d=c[0]
            print(d)
            df2['Game Competitiveness']=df2.apply(lambda row: epcrcompetitveness(row,d), axis=1 )
        dflist.append(df2)
    dfconcat=pd.concat(dflist)
    cup2.append(dfconcat)
cup3=pd.concat(cup2)
games2=league3.append(cup3)        
 
check=games2[(games2['Game Competitiveness'].str.contains('Check Problem'))]

games2.loc[((games2['Tournament'].str.contains('Champions|Challenge'))&(games2['Last Game in Comp']==999)),'Last Game in Comp']=240
games2.loc[((games2['Tournament'].str.contains('League'))&(games2['Last Game in Comp']==999)),'Last Game in Comp']=140
games2.loc[((games2['Tournament'].str.contains('League'))&(games2['LastGame']==999)),'LastGame']=140

games3=[]
for i in teams:
    df=games2[(games2['Home Team'].str.contains(i))]
    df=df.sort_values(by='Date')
    df['Time']=df['Date']-df['Date'].shift(1)
    df['Days']=df['Time'].dt.days
    df.loc[((df['Tournament'].str.contains('Champions|Challenge'))&(df['LastGame']==999)),'LastGame']=df['Days']
    games3.append(df)
games4=pd.concat(games3)

games4.loc[(games4['Home Last_5_W/L']==999),'Home Last_5_W/L']=np.nan
games4.loc[(games4['Away Last_5_W/L']==999),'Away Last_5_W/L']=np.nan
games4.loc[(games4['Home Win/Loss in Comp']==999),'Home Win/Loss in Comp']=np.nan
games4.loc[(games4['Away Win/Loss in Comp']==999),'Away Win/Loss in Comp']=np.nan

averages=[]
for i in teams:
    df=games4[(games4['Home Team'].str.contains(i))]
    average=round(df['Home Last_5_W/L'].mean(skipna=True))
    averages.append({i:average})
for i in averages:
    for j,i in i.items():
        games4.loc[((games4['Home Team'].str.contains(j))&(games4['Home Last_5_W/L'].isnull())),'Home Last_5_W/L']=i
        
averages=[]
for i in teams:
    df=games4[(games4['Away Team'].str.contains(i))]
    average=round(df['Away Last_5_W/L'].mean(skipna=True))
    averages.append({i:average})
for i in averages:
    for j,i in i.items():
        games4.loc[((games4['Away Team'].str.contains(j))&(games4['Away Last_5_W/L'].isnull())),'Away Last_5_W/L']=i
games4['Away Last_5_W/L']=games4['Away Last_5_W/L'].fillna(0)
        
averages=[]
for i in teams:
    df=games4[(games4['Home Team'].str.contains(i))]
    average=round(df['Home Win/Loss in Comp'].mean(skipna=True))
    averages.append({i:average})
for i in averages:
    for j,i in i.items():
        games4.loc[((games4['Home Team'].str.contains(j))&(games4['Home Win/Loss in Comp'].isnull())),'Home Win/Loss in Comp']=i
        
averages=[]
for i in teams:
    df=games4[(games4['Away Team'].str.contains(i))]
    average=round(df['Away Win/Loss in Comp'].mean(skipna=True))
    averages.append({i:average})
for i in averages:
    for j,i in i.items():
        games4.loc[((games4['Away Team'].str.contains(j))&(games4['Away Win/Loss in Comp'].isnull())),'Away Win/Loss in Comp']=i
games4['Away Win/Loss in Comp']=games4['Away Win/Loss in Comp'].fillna(0) 

games4=games4.drop(columns=['Points Left','Kick Off','Table Marker','Stadium Percentage','Stadium Capacity','Total Points Avail TD','Home Total Points',\
                          'Home Points','Away Win/loss/draw','Home Win/loss/draw','Home Score','Away Score','Home h2htries','Away h2htries','Home Wins',\
                          'Away Wins','Draws','Played','Time','Days'])
games4['Uncertainty']=games4['Home Winning Percentage']*games4['homeVSaway Winning Percentage']

print(games4['Max Temperature'].mean())
print(games4['Max Temperature'].median())
print(games4['Max Temperature'].min())
print(games4['Max Temperature'].max())
print(games4['Max Temperature'].std())
def tempdummy(row):
    if row['Max Temperature'] < 8.5:
        x='Cold'
    elif row['Max Temperature'] > 13.5:
        x='Warm'
    else:
        x='Mild'
    return x

games4['Temperature']=games4.apply(lambda row: tempdummy(row), axis=1)

print(games4['Wind Speed'].mean())
print(games4['Wind Speed'].median())
print(games4['Wind Speed'].min())
print(games4['Wind Speed'].max())
print(games4['Wind Speed'].std())
def winddummy(row):
    if row['Wind Speed'] < 14:
        x='Calm'
    elif row['Wind Speed'] > 26:
        x='Wild'
    else:
        x='Normal'
    return x

games4['Wind']=games4.apply(lambda row: winddummy(row), axis=1)

print(games4['Rain Level'].mean())
print(games4['Rain Level'].median())
print(games4['Rain Level'].min())
print(games4['Rain Level'].max())
print(games4['Rain Level'].std())
def raindummy(row):
    if row['Rain Level'] <= 0.00:
        x='Dry'
    elif row['Rain Level'] > 8:
        x='Wet'
    else:
        x='Damp'
    return x

games4['Rain']=games4.apply(lambda row: raindummy(row), axis=1)
games4=games4[(~games['Home Team'].str.contains('Southern Kings|Cheetahs|Glasgow'))]

#games4=games4[(games4['Attendance']<30000)]
savedfile=games4.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/For Exploration.csv', index=False)
games5=games4.drop(columns=['Season','Date'])
savedfile=games5.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Data for Model.csv', index=False)

from matplotlib import pyplot as plt
plt.hist(games5['Attendance'],histtype='bar')

#games5.columns
#games5.info()
#
#games6=games5
#games6['NAttendance'] = (games6['Attendance'] - games6['Attendance'].min()) / (games6['Attendance'].max() - games6['Attendance'].min())
#games6['NRound'] = (games6['Round'] - games6['Round'].min()) / (games6['Round'].max() - games6['Round'].min())
#games6['NHome Table Position'] = (games6['Home Table Position'] - games6['Home Table Position'].min()) / (games6['Home Table Position'].max() - games6['Home Table Position'].min())
#games6['NAway Table Position'] = (games6['Away Table Position'] - games6['Away Table Position'].min()) / (games6['Away Table Position'].max() - games6['Away Table Position'].min())
#games6['NHome Last_5_W/L'] = (games6['Home Last_5_W/L'] - games6['Home Last_5_W/L'].min()) / (games6['Home Last_5_W/L'].max() - games6['Home Last_5_W/L'].min())
#games6['NLastGame'] = (games6['LastGame'] - games6['LastGame'].min()) / (games6['LastGame'].max() - games6['LastGame'].min())
#games6['NAway Last_5_W/L'] = (games6['Away Last_5_W/L'] - games6['Away Last_5_W/L'].min()) / (games6['Away Last_5_W/L'].max() - games6['Away Last_5_W/L'].min())
#games6['NMax Temperature'] = (games6['Max Temperature'] - games6['Max Temperature'].min()) / (games6['Max Temperature'].max() - games6['Max Temperature'].min())
#games6['NRain Level'] = (games6['Rain Level'] - games6['Rain Level'].min()) / (games6['Rain Level'].max() - games6['Rain Level'].min())
#games6['NWind Speed'] = (games6['Wind Speed'] - games6['Wind Speed'].min()) / (games6['Wind Speed'].max() - games6['Wind Speed'].min())
#games6['NLast Game in Comp'] = (games6['Last Game in Comp'] - games6['Last Game in Comp'].min()) / (games6['Last Game in Comp'].max() - games6['Last Game in Comp'].min())
#games6['NHome Win/Loss in Comp'] = (games6['Home Win/Loss in Comp'] - games6['Home Win/Loss in Comp'].min()) / (games6['Home Win/Loss in Comp'].max() - games6['Home Win/Loss in Comp'].min())
#games6['NAway Win/Loss in Comp'] = (games6['Away Win/Loss in Comp'] - games6['Away Win/Loss in Comp'].min()) / (games6['Away Win/Loss in Comp'].max() - games6['Away Win/Loss in Comp'].min())
#games6['NDay Of Week'] = (games6['Day Of Week'] - games6['Day Of Week'].min()) / (games6['Day Of Week'].max() - games6['Day Of Week'].min())
#games6['NMonth of Year'] = (games6['Month of Year'] - games6['Month of Year'].min()) / (games6['Month of Year'].max() - games6['Month of Year'].min())
#games6['NHome Winning Percentage'] = (games6['Home Winning Percentage'] - games6['Home Winning Percentage'].min()) / (games6['Home Winning Percentage'].max() - games6['Home Winning Percentage'].min())
#games6['NhomeVSaway Winning Percentage'] = (games6['homeVSaway Winning Percentage'] - games6['homeVSaway Winning Percentage'].min()) / (games6['homeVSaway Winning Percentage'].max() - games6['homeVSaway Winning Percentage'].min())
#games6['NNumber ofP14 Wins'] = (games6['Number ofP14 Wins'] - games6['Number ofP14 Wins'].min()) / (games6['Number ofP14 Wins'].max() - games6['Number ofP14 Wins'].min())
#games6['NNumber ofEPCR Wins'] = (games6['Number ofEPCR Wins'] - games6['Number ofEPCR Wins'].min()) / (games6['Number ofEPCR Wins'].max() - games6['Number ofEPCR Wins'].min())
#games6['NYears sinceP14 Win'] = (games6['Years sinceP14 Win'] - games6['Years sinceP14 Win'].min()) / (games6['Years sinceP14 Win'].max() - games6['Years sinceP14 Win'].min())
#games6['NYears sinceEPCR Win'] = (games6['Years sinceEPCR Win'] - games6['Years sinceEPCR Win'].min()) / (games6['Years sinceEPCR Win'].max() - games6['Years sinceEPCR Win'].min())
#games6['NStadium Age'] = (games6['Stadium Age'] - games6['Stadium Age'].min()) / (games6['Stadium Age'].max() - games6['Stadium Age'].min())
#games6['NTable Difference'] = (games6['Table Difference'] - games6['Table Difference'].min()) / (games6['Table Difference'].max() - games6['Table Difference'].min())
#games6['NUncertainty'] = (games6['Uncertainty'] - games6['Uncertainty'].min()) / (games6['Uncertainty'].max() - games6['Uncertainty'].min())
#
#games6=games6[['Tournament', 'NRound', 'Home Team', 'Away Team', 'Venue', 'NAttendance',\
#               'NHome Table Position', 'NAway Table Position', 'NHome Last_5_W/L',\
#               'NLastGame', 'NAway Last_5_W/L', 'NMax Temperature', 'NRain Level',\
#               'NWind Speed', 'NLast Game in Comp', 'NHome Win/Loss in Comp',\
#               'NAway Win/Loss in Comp', 'NDay Of Week', 'NMonth of Year',\
#               'NHome Winning Percentage', 'Derby',\
#               'NhomeVSaway Winning Percentage', 'NNumber ofP14 Wins',\
#               'NNumber ofEPCR Wins', 'NYears sinceP14 Win', 'NYears sinceEPCR Win',\
#               'NStadium Age', 'NTable Difference', 'Game Competitiveness',\
#               'NUncertainty', 'Temperature', 'Wind', 'Rain']]
#
#savedfile=games6.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/NData for Model.csv', index=False)
#
#munster=games6[(games6['Home Team'].str.contains('Munster'))]
#munster=munster.drop(columns=['Home Team'])
#savedfile=munster.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/MunsterData for Model.csv', index=False)
