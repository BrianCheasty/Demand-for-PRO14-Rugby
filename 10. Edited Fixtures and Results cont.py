import pandas as pd
import numpy as np

gamesa=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation2.csv',encoding='latin-1')
gamesb=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation2b.csv',encoding='latin-1')
missedaway=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Missed Away Games.csv',encoding='latin-1')
bettingodds=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Betting Odds.csv',encoding='latin-1')
threeWins=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Three Game Wins.csv',encoding='latin-1')
sentiment=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Consumer Sentiment.csv',encoding='latin-1')
sentiment['Date']=pd.to_datetime(sentiment['Date'],format='%d/%m/%Y')

threeWins.columns
bettingodds['Date']=pd.to_datetime(bettingodds['Date'],format='%d/%m/%Y')
missedaway=missedaway.drop(columns=['Pool Stage','Stadium URL'])
missedaway['Max Temperature']=np.nan
missedaway['Rain Level']=np.nan
missedaway['Wind Speed']=np.nan


game=gamesa.append([gamesb,missedaway])
game=game.reset_index()
game=game.drop(columns=['index'])
game['Date']=pd.to_datetime(game['Date'],format='%Y-%m-%d')
threeWins['Date']=pd.to_datetime(threeWins['Date'],format='%Y-%m-%d')
bettingodds['Home Team']=bettingodds['Home Team'].str.strip()
bteam=list(bettingodds['Home Team'].drop_duplicates())
gameteam=list(game['Home Team'].drop_duplicates())

bettingodds.loc[bettingodds['Home Team'].str.contains('Ospreys'),'Home Team']='Ospreys'
bettingodds.loc[bettingodds['Home Team'].str.contains('Dragons'),'Home Team']='Dragons'
bettingodds.loc[bettingodds['Home Team'].str.contains('Edinburgh'),'Home Team']='Edinburgh Rugby'
bettingodds.loc[bettingodds['Home Team'].str.contains('Zebre'),'Home Team']='Zebre Rugby'
bettingodds.loc[bettingodds['Home Team'].str.contains('Benetton'),'Home Team']='Benetton Treviso'
bettingodds.loc[bettingodds['Home Team'].str.contains('Leinster'),'Home Team']='Leinster Rugby'
bettingodds.loc[bettingodds['Home Team'].str.contains('Cardiff'),'Home Team']='Cardiff Blues'
bettingodds.loc[bettingodds['Home Team'].str.contains('Scarlets'),'Home Team']='Scarlets'
bettingodds.loc[bettingodds['Home Team'].str.contains('Munster'),'Home Team']='Munster Rugby'
bettingodds.loc[bettingodds['Home Team'].str.contains('Ulster'),'Home Team']='Ulster Rugby'
bettingodds.loc[bettingodds['Home Team'].str.contains('Connacht'),'Home Team']='Connacht Rugby'
bettingodds.loc[bettingodds['Home Team'].str.contains('Glasgow'),'Home Team']='Glasgow Warriors'
bettingodds.loc[bettingodds['Home Team'].str.contains('Kings'),'Home Team']='Southern Kings'
bettingodds.loc[bettingodds['Home Team'].str.contains('Cheetahs'),'Home Team']='Toyota Cheetahs'
bettingodds.loc[bettingodds['Home Team'].str.contains('Francais'),'Home Team']='Stade Francais Paris'
bettingodds.loc[bettingodds['Home Team'].str.contains('Leicester'),'Home Team']='Leicester Tigers'
bettingodds.loc[bettingodds['Home Team'].str.contains('Gloucester'),'Home Team']='Gloucester Rugby'
bettingodds.loc[bettingodds['Home Team'].str.contains('Bayonne'),'Home Team']='Bayonne'
bettingodds.loc[bettingodds['Home Team'].str.contains('Rochelle'),'Home Team']='La Rochelle'
bettingodds.loc[bettingodds['Home Team'].str.contains('Bath'),'Home Team']='Bath Rugby'
bettingodds.loc[bettingodds['Home Team'].str.contains('Agen'),'Home Team']='Agen'
bettingodds.loc[bettingodds['Home Team'].str.contains('Harlequins'),'Home Team']='Harlequins'
bettingodds.loc[bettingodds['Home Team'].str.contains('Grenoble'),'Home Team']='Grenoble'
bettingodds.loc[bettingodds['Home Team'].str.contains('Calvisano'),'Home Team']='Rugby Calvisano'
bettingodds.loc[bettingodds['Home Team'].str.contains('Montpellier'),'Home Team']='Montpellier'
bettingodds.loc[bettingodds['Home Team'].str.contains('Bristol'),'Home Team']='Bristol Rugby'
bettingodds.loc[bettingodds['Home Team'].str.contains('Pau'),'Home Team']='Pau'
#bettingodds.loc[bettingodds['Home Team'].str.contains('RC Toulonnai'),'Home Team']='Toulouse'
#bettingodds.loc[bettingodds['Home Team'].str.contains('Toulon'),'Home Team']='RC Toulon'
bettingodds.loc[bettingodds['Home Team'].str.contains('Sale'),'Home Team']='Sale Sharks'
bettingodds.loc[bettingodds['Home Team'].str.contains('Lyon'),'Home Team']='Lyon'
bettingodds.loc[bettingodds['Home Team'].str.contains('Saracens'),'Home Team']='Saracens'
bettingodds.loc[bettingodds['Home Team'].str.contains('Enisei|Enisey'),'Home Team']='Enisei-STM'
bettingodds.loc[bettingodds['Home Team'].str.contains('Newcastle'),'Home Team']='Newcastle Falcons'
bettingodds.loc[bettingodds['Home Team'].str.contains('Brive'),'Home Team']='Brive'
bettingodds.loc[bettingodds['Home Team'].str.contains('Wasps'),'Home Team']='Wasps'
bettingodds.loc[bettingodds['Home Team'].str.contains('Oyonnax'),'Home Team']='Oyonnax'
bettingodds.loc[bettingodds['Home Team'].str.contains('Worcester'),'Home Team']='Worcester Warriors'
bettingodds.loc[bettingodds['Home Team'].str.contains('Perpignan'),'Home Team']='Perpignan'
bettingodds.loc[bettingodds['Home Team'].str.contains('Bordeaux'),'Home Team']='Bordeaux-Begles'
bettingodds.loc[bettingodds['Home Team'].str.contains('Castres'),'Home Team']='Castres Olympique'
bettingodds.loc[bettingodds['Home Team'].str.contains('Northampton'),'Home Team']='Northampton Saints'
bettingodds.loc[bettingodds['Home Team'].str.contains('Clermont'),'Home Team']='ASM Clermont Auvergne'
bettingodds.loc[bettingodds['Home Team'].str.contains('Irish'),'Home Team']='London Irish'
bettingodds.loc[bettingodds['Home Team'].str.contains('Timisoara'),'Home Team']='Timisoara Saracens'
bettingodds.loc[bettingodds['Home Team'].str.contains('Krasny'),'Home Team']='Krasny Yar'
bettingodds.loc[bettingodds['Home Team'].str.contains('Racing'),'Home Team']='Racing 92'
bettingodds.loc[bettingodds['Home Team'].str.contains('Exeter'),'Home Team']='Exeter Chiefs'


bteam=list(bettingodds['Home Team'].drop_duplicates())
games=pd.merge(game,bettingodds, on=['Date','Home Team'], how='left')
games=pd.merge(games,threeWins, on=['Date','Home Team'], how='left')
games=games.drop(columns=['Away Team_y'])
games=games.rename(columns={'Away Team_x':'Away Team'})
check=game[(games['Home Win'].isnull())]
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
games['Played']=games['Played'].fillna(0)
games['Home Wins']=games['Home Wins'].fillna(0)
games['Away Wins']=games['Away Wins'].fillna(0)
games['Draws']=games['Draws'].fillna(0)
games.info()
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
            print(i +' is length 0 in '+j)
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
gamesB['Home Total Points']=gamesB['Home Total Points'].fillna(0)
gamesB['Total Points Avail TD']=gamesB['Total Points Avail TD'].fillna(0)
gamesB.info()

#gamesB['Date']=pd.to_datetime(gamesB['Date'])
gamesB['Day Of Week']=gamesB['Date'].dt.dayofweek
gamesB['Month of Year']=gamesB['Date'].dt.month

checktime=pd.pivot_table(gamesB,index='Kick Off', columns='Home Team', values='Date',aggfunc='count')

gamesB['Kick Off']=gamesB['Kick Off'].fillna(gamesB['Time'])
gamesB['Kick Off']=gamesB['Kick Off'].fillna('16:00:00')
gamesB.info()
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
gamesB.info()

gamesB['Home Winning Percentage']=round(gamesB['Home Total Points']/gamesB['Total Points Avail TD'],2)
gamesB['Home Winning Percentage']=gamesB['Home Winning Percentage'].fillna(0)

gamesB.loc[((gamesB['Home Team'].str.contains('Munster|Leinster|Connacht|Ulster'))&(gamesB['Away Team'].str.contains('Munster|Leinster|Connacht|Ulster'))),'Derby']='Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Edinburgh|Glasgow'))&(gamesB['Away Team'].str.contains('Edinburgh|Glasgow'))),'Derby']='Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Kings|Cheetahs'))&(gamesB['Away Team'].str.contains('Kings|Cheetahs'))),'Derby']='Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Treviso|Zebre'))&(gamesB['Away Team'].str.contains('Treviso|Zebre'))),'Derby']='Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Ospreys|Dragons|Cardiff|Scarlets'))&(gamesB['Away Team'].str.contains('Ospreys|Dragons|Cardiff|Scarlets'))),'Derby']='Derby'

gamesB.loc[((gamesB['Home Team'].str.contains('Munster'))&(gamesB['Away Team'].str.contains('Leinster'))),'Derby']='Extra Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Leinster'))&(gamesB['Away Team'].str.contains('Munster'))),'Derby']='Extra Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Connacht'))&(gamesB['Away Team'].str.contains('Leinster'))),'Derby']='Extra Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Ulster'))&(gamesB['Away Team'].str.contains('Leinster'))),'Derby']='Extra Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Edinburgh'))&(gamesB['Away Team'].str.contains('Glasgow'))),'Derby']='Extra Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Cardiff'))&(gamesB['Away Team'].str.contains('Ospreys'))),'Derby']='Extra Derby'
gamesB.loc[((gamesB['Home Team'].str.contains('Dragons'))&(gamesB['Away Team'].str.contains('Scarlets'))),'Derby']='Extra Derby'

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
gamesB.loc[(gamesB['Venue'].str.contains('RDS')),'Stadium Capacity']=19100

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
gamesB.loc[(gamesB['Venue'].str.contains('Thomond')),'Stadium Capacity']=26267

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
gamesB.info()

gamesB['Stadium Percentage']=round(gamesB['Attendance']/gamesB['Stadium Capacity'],2)
check=gamesB[(gamesB['Stadium Percentage']>0.99)]
gamesB=gamesB.rename(columns={'Home Table Pos':'Home Table Position','Away Table Pos':'Away Table Position'})
league=gamesB[(gamesB['Tournament'].str.contains('League'))]
league.info()
cup=gamesB[(gamesB['Tournament'].str.contains('Cup'))]
cup.info()

#   percentage
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

cup.info()
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
league.info()
cup.info()
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
games2.info() 
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
games4.info()




games4.loc[(games4['Home Last_3_W/L']==999),'Home Last_3_W/L']=np.nan
games4.loc[(games4['Home Last_5_W/L']==999),'Home Last_5_W/L']=np.nan
games4.loc[(games4['Away Last_5_W/L']==999),'Away Last_5_W/L']=np.nan
games4.loc[(games4['Home Win/Loss in Comp']==999),'Home Win/Loss in Comp']=np.nan
games4.loc[(games4['Away Win/Loss in Comp']==999),'Away Win/Loss in Comp']=np.nan
games4=games4[(games4['Home Team'].str.contains('Ospreys|Dragons|Edinburgh Rugby|Zebre Rugby|Benetton Treviso|Leinster Rugby|Cardiff Blues|Scarlets|Munster Rugby|Ulster Rugby|Connacht Rugby|Glasgow Warriors|Southern Kings|Toyota Cheetahs'))]
teams=list(games4['Home Team'].drop_duplicates())
awayteams=list(games4['Away Team'].drop_duplicates())
games4.loc[((games4['Away Team'].str.contains('Munster|Leinster|Connacht|Ulster'))),'Away Country']='Ireland'
games4.loc[((games4['Away Team'].str.contains('Glasgow|Edinburgh'))),'Away Country']='Scotland'
games4.loc[((games4['Away Team'].str.contains('Zebre|Treviso'))),'Away Country']='Italy'
games4.loc[((games4['Away Team'].str.contains('Cardiff|Ospreys|Dragons|Scarlets'))),'Away Country']='Wales'
games4['Away Country']=games4['Away Country'].fillna('EngFra')

#from scipy.stats import shapiro
averages=[]
#import matplotlib.pyplot as plt
#plt.hist(games4['Home Last_5_W/L'])
for i in teams:
    df=games4[(games4['Home Team'].str.contains(i))]
    #stat, p = shapiro(df['Home Last_5_W/L'])
    #print('Statistics=%.3f, p=%.3f' % (stat, p))
    #plt.hist(df['Home Last_5_W/L'])
    average=round(df['Home Last_5_W/L'].mean(skipna=True))
    #print(average)
    averages.append({i:average})
for i in averages:
    for j,i in i.items():
        games4.loc[((games4['Home Team'].str.contains(j))&(games4['Home Last_5_W/L'].isnull())),'Home Last_5_W/L']=i
        
#checkmedian=[]
#for i in teams:
#    df=games4[(games4['Home Team'].str.contains(i))]
#    print(df['Home Last_5_W/L'].median())
#    median=round(df['Home Last_5_W/L'].median())
#    checkmedian.append({i:median})

averages=[]
for i in teams:
    df=games4[(games4['Home Team'].str.contains(i))]
    average=round(df['Home Last_3_W/L'].mean(skipna=True))
    print(average)
    averages.append({i:average})
for i in averages:
    for j,i in i.items():
        games4.loc[((games4['Home Team'].str.contains(j))&(games4['Home Last_3_W/L'].isnull())),'Home Last_3_W/L']=i
        
#checkmedian=[]
#for i in teams:
#    df=games4[(games4['Home Team'].str.contains(i))]
#    print(df['Home Last_3_W/L'].median())
#    median=round(df['Home Last_3_W/L'].median())
#    checkmedian.append({i:median})
        
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
games4['Uncertainty']=games4['Home Winning Percentage']*games4['homeVSaway Winning Percentage']
games4=games4.drop(columns=['Points Left','Kick Off','Table Marker','Total Points Avail TD','Home Total Points',\
                          'Home Points','Away Win/loss/draw','Home Win/loss/draw','Home Score','Away Score','Home h2htries','Away h2htries','Home Wins',\
                          'Away Wins','Draws','Played','Time','Days'])  #Removed 'Stadium Capacity',


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
games4=games4[(~games['Away Team'].str.contains('Southern Kings|Cheetahs'))]
games5=pd.merge(games4,sentiment, on=['Date','Home Team'], how='left')
def stadiumage(row):
    if row['Stadium Age'] < 5:
        x='New'
    elif row['Stadium Age']>20:
        x='Old'
    else:
        x='Middle Age'
    return x
games5['Age of Stadium']=games5.apply(lambda row: stadiumage(row), axis=1)
games5=games5[(games5['Odds1'].notnull())]
def probability(row):
    odds=row['Odds1'].split(':')
    homeodd=int(odds[0])
    awayodd=int(odds[1])
    if (homeodd > 0)&(awayodd > 0):
        home=homeodd/awayodd
        both=home+1
        prob=1/both
    elif(homeodd == 0)&(awayodd > 0):
        home=1/awayodd
        both=home+1
        prob=1/both
    elif(homeodd > 0)&(awayodd == 0):
        home=homeodd
        both=home+1
        prob=1/both
    return prob
    
games5['Win Probability']=games5.apply(lambda row:probability(row), axis=1)
def uncertaintydummy(row):
    if row['Win Probability'] >= 0.6 or row['Win Probability'] <= 0.4:
        x='Uneven'
    else:
        x='Even'
    return x
games5['Win Probability Dummy']=games5.apply(lambda row:uncertaintydummy(row), axis=1)
games5=games5.drop(columns=['Odds1','Home Win','Draw','Away Win','Odds6'])       

savedfile=games5.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/For Exploration.csv', index=False)
games6=games5.drop(columns=['Season','Date','Stadium Percentage'])
savedfile=games6.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Data for Model.csv', index=False)
games5['Stadium Perc']=games5['Stadium Percentage']*100
games7=games5.drop(columns=['Season','Date','Attendance','Stadium Percentage'])
games7=games7.rename(columns={'Stadium Perc':'Stadium Percentage'})
savedfile=games7.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Data for Model2.csv', index=False)


