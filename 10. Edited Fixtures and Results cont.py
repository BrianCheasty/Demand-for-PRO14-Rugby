import pandas as pd

games=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation2.csv',encoding='latin-1')
games=games[(games['Home Team']!=('Southern Kings'))]
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


league=games[(games['Tournament'].str.contains('League'))]
cup=games[(games['Tournament'].str.contains('Cup'))]

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


league=league.rename(columns={'Home Table Pos':'Home Table Position','Away Table Pos':'Away Table Position'})

    


league4=[]
for i in teams:
    df=[]
    df1=league[(league['Home Team'].str.contains(i)) | (league['Away Team'].str.contains(i))]
    for j in season:
        df2=df1[(df1['Season'].str.contains(j))]
        df2=df2.sort_values(by=['Date'])
        df2['Home Points']=df2.apply(lambda row: tries(row), axis=1)
        df2['Home Total Points']=df2['Home Points'].expanding(1).sum()
        df2['Total Points Avail TD']=df2['Round']*5
        df3=df2[(df2['Home Team'].str.contains(i))]
        df.append(df3)
    df4=pd.concat(df)
    league4.append(df4)
league5=pd.concat(league4) 


league5.loc[((league5['Home Team'].str.contains('Munster'))&league5['Home Table Position'].isnull()),'Home Table Position']=2
league5.loc[((league5['Away Team'].str.contains('Munster'))&league5['Away Table Position'].isnull()),'Home Table Position']=2
league5.loc[((league5['Home Team'].str.contains('Glasgow'))&league5['Home Table Position'].isnull()),'Home Table Position']=1
league5.loc[((league5['Away Team'].str.contains('Glasgow'))&league5['Away Table Position'].isnull()),'Home Table Position']=1
league5.loc[((league5['Home Team'].str.contains('Ospreys'))&league5['Home Table Position'].isnull()),'Home Table Position']=3
league5.loc[((league5['Away Team'].str.contains('Ospreys'))&league5['Away Table Position'].isnull()),'Home Table Position']=3
league5.loc[((league5['Home Team'].str.contains('Ulster'))&league5['Home Table Position'].isnull()),'Home Table Position']=4
league5.loc[((league5['Away Team'].str.contains('Ulster'))&league5['Away Table Position'].isnull()),'Home Table Position']=4
league5.loc[((league5['Home Team'].str.contains('Leinster'))&league5['Home Table Position'].isnull()),'Home Table Position']=5
league5.loc[((league5['Away Team'].str.contains('Leinster'))&league5['Away Table Position'].isnull()),'Home Table Position']=5
league5.loc[((league5['Home Team'].str.contains('Scarlets'))&league5['Home Table Position'].isnull()),'Home Table Position']=6
league5.loc[((league5['Away Team'].str.contains('Scarlets'))&league5['Away Table Position'].isnull()),'Home Table Position']=6
league5.loc[((league5['Home Team'].str.contains('Connacht'))&league5['Home Table Position'].isnull()),'Home Table Position']=7
league5.loc[((league5['Away Team'].str.contains('Connacht'))&league5['Away Table Position'].isnull()),'Home Table Position']=7
league5.loc[((league5['Home Team'].str.contains('Edinburgh'))&league5['Home Table Position'].isnull()),'Home Table Position']=8
league5.loc[((league5['Away Team'].str.contains('Edinburgh'))&league5['Away Table Position'].isnull()),'Home Table Position']=8
league5.loc[((league5['Home Team'].str.contains('Dragons'))&league5['Home Table Position'].isnull()),'Home Table Position']=9
league5.loc[((league5['Away Team'].str.contains('Dragons'))&league5['Away Table Position'].isnull()),'Home Table Position']=9
league5.loc[((league5['Home Team'].str.contains('Cardiff'))&league5['Home Table Position'].isnull()),'Home Table Position']=10
league5.loc[((league5['Away Team'].str.contains('Cardiff'))&league5['Away Table Position'].isnull()),'Home Table Position']=10
league5.loc[((league5['Home Team'].str.contains('Benetton'))&league5['Home Table Position'].isnull()),'Home Table Position']=11
league5.loc[((league5['Away Team'].str.contains('Benetton'))&league5['Away Table Position'].isnull()),'Home Table Position']=11
league5.loc[((league5['Home Team'].str.contains('Zebre'))&league5['Home Table Position'].isnull()),'Home Table Position']=12
league5.loc[((league5['Away Team'].str.contains('Zebre'))&league5['Away Table Position'].isnull()),'Home Table Position']=12
league5.loc[league5['Season'].str.contains('2015/2016 Season|2016/2017 Season'),'Table Difference']=league5['Home Table Position']-league5['Away Table Position']
league5.loc[league5['Season'].str.contains('2017/2018 Season|2018/2019 Season'),'Table Difference']=(league5['Home Table Position']-league5['Away Table Position'])*2

#x=league5['Home Total Points'].where(league5['Home Table Position']==3)
league5.loc[((league5['Season'].str.contains('2015/2016|2016/2017'))&(league5['Home Table Position']==4)),'Table Marker']=4
league5.loc[((league5['Season'].str.contains('2015/2016|2016/2017'))&(league5['Away Table Position']==4)),'Table Marker']=4
league5.loc[((league5['Season'].str.contains('2015/2016|2016/2017'))&(league5['Home Table Position']==3)),'Table Marker']=3
league5.loc[((league5['Season'].str.contains('2015/2016|2016/2017'))&(league5['Away Table Position']==3)),'Table Marker']=3
league5.loc[((league5['Season'].str.contains('2017/2018|2018/2019'))&(league5['Home Table Position']==3)),'Table Marker']=3
league5.loc[((league5['Season'].str.contains('2017/2018|2018/2019'))&(league5['Away Table Position']==3)),'Table Marker']=3
league5.loc[((league5['Season'].str.contains('2017/2018|2018/2019'))&(league5['Home Table Position']==4)),'Table Marker']=4
league5.loc[((league5['Season'].str.contains('2017/2018|2018/2019'))&(league5['Away Table Position']==4)),'Table Marker']=4

def competitveness1517(row,d):
    rounds=row['Round']
    roundsleft=23-int(rounds)
    pointsleft=roundsleft*5
    if (row['Home Total Points']+pointsleft)< d:
        z='Cant Qualify'
    elif (row['Home Total Points']+pointsleft)> d:
        if (row['Home Total Points']-pointsleft)> d:
            z='Has Qualified'
        else:
            z='Can Still Qualify'
    return z
def competitveness1719(row,d):
    rounds=df2['Round']
    roundsleft=22-int(rounds)
    pointsleft=roundsleft*5
    if (row['Home Total Points']+pointsleft)< d:
        z='Cant Qualify'
    elif (row['Home Total Points']+pointsleft)> d:
        if (row['Home Total Points']-pointsleft)> d:
            z='Has Qualified'
        else:
            z='Can Still Qualify'
    return z

league5['Table Marker']=league5['Table Marker'].fillna(0)

season22=['2015/2016 Season','2016/2017 Season']
round22=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
league6=[]
for i in season22:
    dflist=[]
    df=league5[(league5['Season'].str.contains(i))]
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
    league6.append(dfconcat)
season22=['2017/2018 Season','2018/2019 Season']
round22=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
for i in season22:
    dflist=[]
    df=league5[(league5['Season'].str.contains(i))]
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
    league6.append(dfconcat)    
league7=pd.concat(league6)
        
        
league7['Date']=pd.to_datetime(league7['Date'])
league7['Day Of Week']=league7['Date'].dt.dayofweek

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
league7['Kick Off Hour']=league7.apply(lambda row:time(row), axis=1)    

league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Leinster'))),'Number ofP14 Wins']=5
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Leinster'))),'Number ofP14 Wins']=4
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Leinster'))),'Number ofP14 Wins']=3
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Leinster'))),'Number ofP14 Wins']=3
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Ospreys'))),'Number ofP14 Wins']=4
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Ospreys'))),'Number ofP14 Wins']=4
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Ospreys'))),'Number ofP14 Wins']=4
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Ospreys'))),'Number ofP14 Wins']=4
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Munster'))),'Number ofP14 Wins']=3
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Munster'))),'Number ofP14 Wins']=3
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Munster'))),'Number ofP14 Wins']=3
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Munster'))),'Number ofP14 Wins']=3
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Scarlets'))),'Number ofP14 Wins']=2
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Scarlets'))),'Number ofP14 Wins']=2
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Scarlets'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Scarlets'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Ulster'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Ulster'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Ulster'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Ulster'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Connacht'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Connacht'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Connacht'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Connacht'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Glasgow'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Glasgow'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Glasgow'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Glasgow'))),'Number ofP14 Wins']=1
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Edinburgh'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Edinburgh'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Edinburgh'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Edinburgh'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Cardiff'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Cardiff'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Cardiff'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Cardiff'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Zebre'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Zebre'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Zebre'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Zebre'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Treviso'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Treviso'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Treviso'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Treviso'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Dragons'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Dragons'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Dragons'))),'Number ofP14 Wins']=0
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Dragons'))),'Number ofP14 Wins']=0

league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Leinster'))),'Years sinceP14 Win']=0
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Leinster'))),'Years sinceP14 Win']=0
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Leinster'))),'Years sinceP14 Win']=3
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Leinster'))),'Years sinceP14 Win']=2
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Ospreys'))),'Years sinceP14 Win']=7
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Ospreys'))),'Years sinceP14 Win']=6
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Ospreys'))),'Years sinceP14 Win']=5
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Ospreys'))),'Years sinceP14 Win']=4
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Munster'))),'Years sinceP14 Win']=8
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Munster'))),'Years sinceP14 Win']=7
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Munster'))),'Years sinceP14 Win']=6
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Munster'))),'Years sinceP14 Win']=5
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Scarlets'))),'Years sinceP14 Win']=2
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Scarlets'))),'Years sinceP14 Win']=1
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Scarlets'))),'Years sinceP14 Win']=16
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Scarlets'))),'Years sinceP14 Win']=16
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Ulster'))),'Years sinceP14 Win']=13
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Ulster'))),'Years sinceP14 Win']=12
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Ulster'))),'Years sinceP14 Win']=11
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Ulster'))),'Years sinceP14 Win']=10
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Connacht'))),'Years sinceP14 Win']=3
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Connacht'))),'Years sinceP14 Win']=2
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Connacht'))),'Years sinceP14 Win']=1
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Connacht'))),'Years sinceP14 Win']=14
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Glasgow'))),'Years sinceP14 Win']=4
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Glasgow'))),'Years sinceP14 Win']=3
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Glasgow'))),'Years sinceP14 Win']=2
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Glasgow'))),'Years sinceP14 Win']=1
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Edinburgh'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Edinburgh'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Edinburgh'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Edinburgh'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Cardiff'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Cardiff'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Cardiff'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Cardiff'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Zebre'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Zebre'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Zebre'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Zebre'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Treviso'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Treviso'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Treviso'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Treviso'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2018/2019'))&(league7['Home Team'].str.contains('Dragons'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2017/2018'))&(league7['Home Team'].str.contains('Dragons'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2016/2017'))&(league7['Home Team'].str.contains('Dragons'))),'Years sinceP14 Win']=21
league7.loc[((league7['Season'].str.contains('2015/2016'))&(league7['Home Team'].str.contains('Dragons'))),'Years sinceP14 Win']=21

league7['Home Winning Percentage']=round((league7['Home Total Points']/league7['Total Points Avail TD'])*100)





