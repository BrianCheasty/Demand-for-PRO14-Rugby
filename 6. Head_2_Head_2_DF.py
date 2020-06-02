import pandas as pd
import json
from bs4 import BeautifulSoup as bs
import numpy as np

p14=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/P14 API full.csv', encoding='latin-1')
epcr=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/epcr API full.csv', encoding='latin-1')
chal=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/chal API full.csv', encoding='latin-1')

p14=list(p14['2'])
epcr=list(epcr['1'])
chal=list(chal['1'])

head2head=[]
for i in p14:
    apijson = i[ i.index("(") + 1 : i.rindex(")") ]
    json_load=json.loads(apijson)
    html=(json_load['content'])
    val=bs(html,'html.parser')
    val2=val.prettify()
    info=val.find('table',attrs={'class':'table overviewHeadtoHead'})
    table_body = info.find('tbody')
    rows = table_body.find_all('tr')
    data2=[]
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data2.append([ele for ele in cols if ele]) # Get rid of empty values
    head2head.append(data2)
    
played=[]
wins=[]
losses=[]
draws=[]
h2htries=[]

for i in head2head:
    played.append(i[0])
    wins.append(i[1])
    losses.append(i[2])
    draws.append(i[3])
    h2htries.append(i[4])

_played =[]
for i in played:
    _played.append(i[0])
away_played =[]
for i in played:
    away_played.append(i[2]) 
    
home_wins =[]
for i in wins:
    home_wins.append(i[0])
away_wins =[]
for i in wins:
    away_wins.append(i[2]) 
    
home_losses =[]
for i in losses:
    home_losses.append(i[0])
away_losses =[]
for i in losses:
    away_losses.append(i[2]) 
    
_draws =[]
for i in draws:
    _draws.append(i[0])
away_draws =[]
for i in draws:
    away_draws.append(i[2]) 
    
home_h2htries =[]
for i in h2htries:
    home_h2htries.append(i[0])
away_h2htries =[]
for i in h2htries:
    away_h2htries.append(i[2]) 
    

details=[_played,home_wins,away_wins,_draws,home_h2htries,away_h2htries]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List=Fixture_List.rename(columns={0:'Played',1:'Home Wins',2:'Away Wins',\
                                          3:'Draws',4:'Home h2htries',5:'Away h2htries'})

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Head to Head Content/P14 Head to Head.csv',index=False)

_played =[]
home_wins =[]
away_wins =[]
_draws =[]
home_h2htries =[]
away_h2htries =[]
for i in epcr:
    if type(i) is not str:
        _played.append(np.nan)
        home_wins.append(np.nan)
        away_wins.append(np.nan)
        _draws.append(np.nan)
        home_h2htries.append(np.nan)
        away_h2htries.append(np.nan)
    else:    
        apijson = i[ i.index("(") + 1 : i.rindex(")") ]
        json_load=json.loads(apijson)
        html=(json_load['content'])
        val=bs(html,'html.parser')
        val2=val.prettify()
       
        homewins=val.find('div',attrs={'class':'stat-value stat-teamA'})
        awaywins=val.find('div',attrs={'class':'stat-value stat-teamB'})
        draws=val.find('div',attrs={'class':'labelBelow-value'})
        h=homewins.getText()
        if type(h) is not str:
            home_wins.append('0')
        else:
            home_wins.append(h)
        a=awaywins.getText()
        if type(a) is not str:
            away_wins.append('0')
        else:
            away_wins.append(a)
        d=draws.getText()
        if type(d) is not str:
            _draws.append('0')
        else:
            _draws.append(d)
        home_h2htries.append(np.nan)
        away_h2htries.append(np.nan)
        _played.append(np.nan)
        
details=[_played,home_wins,away_wins,_draws,home_h2htries,away_h2htries]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List=Fixture_List.rename(columns={0:'Played',1:'Home Wins',2:'Away Wins',\
                                          3:'Draws',4:'Home h2htries',5:'Away h2htries'})
Fixture_List['Played']=Fixture_List['Played'].str.strip()
Fixture_List['Home Wins']=Fixture_List['Home Wins'].str.strip()
Fixture_List['Away Wins']=Fixture_List['Away Wins'].str.strip()
Fixture_List['Draws']=Fixture_List['Draws'].str.strip()
Fixture_List['Home h2htries']=Fixture_List['Home h2htries'].str.strip()
Fixture_List['Away h2htries']=Fixture_List['Away h2htries'].str.strip()

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Head to Head Content/EPCR Head to Head.csv',index=False)

_played =[]
home_wins =[]
away_wins =[]
_draws =[]
home_h2htries =[]
away_h2htries =[]
for i in chal:
    if type(i) is not str:
        _played.append(np.nan)
        home_wins.append(np.nan)
        away_wins.append(np.nan)
        _draws.append(np.nan)
        home_h2htries.append(np.nan)
        away_h2htries.append(np.nan)
    else:    
        apijson = i[ i.index("(") + 1 : i.rindex(")") ]
        json_load=json.loads(apijson)
        html=(json_load['content'])
        val=bs(html,'html.parser')
        val2=val.prettify()
       
        homewins=val.find('div',attrs={'class':'stat-value stat-teamA'})
        awaywins=val.find('div',attrs={'class':'stat-value stat-teamB'})
        draws=val.find('div',attrs={'class':'labelBelow-value'})
        h=homewins.getText()
        if type(h) is not str:
            home_wins.append('0')
        else:
            home_wins.append(h)
        a=awaywins.getText()
        if type(a) is not str:
            away_wins.append('0')
        else:
            away_wins.append(a)
        d=draws.getText()
        if type(d) is not str:
            _draws.append('0')
        else:
            _draws.append(d)
        home_h2htries.append(np.nan)
        away_h2htries.append(np.nan)
        _played.append(np.nan)
        
details=[_played,home_wins,away_wins,_draws,home_h2htries,away_h2htries]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List=Fixture_List.rename(columns={0:'Played',1:'Home Wins',2:'Away Wins',
                                          3:'Draws',4:'Home h2htries',5:'Away h2htries'})
    
Fixture_List['Played']=Fixture_List['Played'].str.strip()
Fixture_List['Home Wins']=Fixture_List['Home Wins'].str.strip()
Fixture_List['Away Wins']=Fixture_List['Away Wins'].str.strip()
Fixture_List['Draws']=Fixture_List['Draws'].str.strip()
Fixture_List['Home h2htries']=Fixture_List['Home h2htries'].str.strip()
Fixture_List['Away h2htries']=Fixture_List['Away h2htries'].str.strip()

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Head to Head Content/Chal Head to Head.csv',index=False)
