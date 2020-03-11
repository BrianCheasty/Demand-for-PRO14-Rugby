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
league5.loc[((league5['Season'].str.contains('2015/2016|2016/2017'))&(league5['Home Table Position']==4)|(league5['Away Table Position']==4)),'Table Marker']=4
league5.loc[((league5['Season'].str.contains('2017/2018|2018/2019'))&(league5['Home Table Position']==3)|(league5['Away Table Position']==3)),'Table Marker']=3

def competitveness1517(row,x,y):
    rounds=df2['Round']
    roundsleft=23-int(rounds)
    pointsleft=roundsleft*5
    if (row['Home Total Points']+pointsleft)< x:
        z=0
    elif (row['Home Total Points']+pointsleft)> x:
        if (row['Home Total Points']-pointsleft)> y:
            z=0
        else:
            z=1
    return z
def competitveness1719(row,x,y):
    rounds=df2['Round']
    roundsleft=22-int(rounds)
    pointsleft=roundsleft*5
    if (row['Home Total Points']+pointsleft)< x:
        z=0
    elif (row['Home Total Points']+pointsleft)> x:
        if (row['Home Total Points']-pointsleft)> y:
            z=0
        else:
            z=1
    return z

league5['Table Marker']=league5['Table Marker'].fillna(0)


league6=[]
for i in season:
    df=league5[(league5['Season'].str.contains(i))]
    for j in rounds:
        df2=df[(df['Round']==j)]
        dfcomb=[]
        if len(df2)==0:
            continue
        else:
            df3=df2[(df2['Season'].str.contains('2017/2018|2018/2019'))]
            if len(df3)==0:
                print('0')
                a=df2[(df2['Table Marker']==4)]
                b=a[['Home Total Points']]
                c=list(b['Home Total Points'])
                d=c[0]
                print(d)
                y=list(df2['Home Total Points'].where(df2['Table Marker']==5))
                y=y[0]
                df2['Game Competitiveness']=df2.apply(lambda row: competitveness1517(row,x,y), axis=1 )
                dfcomb.append(df2)
            else:
                x=list(df3['Home Total Points'].where(df3['Table Marker']==3))
                x=x[0]
                y=list(df3['Home Total Points'].where(df3['Table Marker']==4))
                y=y[0]
                df3['Game Competitiveness']=df3.apply(lambda row: competitveness1719(row,x,y), axis=1 )
                dfcomb.append(df3)
        league6.append(dfcomb)
                


