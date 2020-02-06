import pandas as pd
import json
from bs4 import BeautifulSoup as bs
import numpy as np

p14=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/P14 API full.csv', encoding='latin-1')
epcr=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/epcr API full.csv', encoding='latin-1')
chal=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/chal API full.csv', encoding='latin-1')

p14=list(p14['1'])
epcr=list(epcr['2'])
chal=list(chal['2'])


############################################################################### 

hometeam_position=[]
awayteam_position=[]

for i in p14:
    if type(i) is not str:
        hometeam_position.append(np.nan)
        awayteam_position.append(np.nan)
    else:
       results=[]
       apijson = i[ i.index("(") + 1 : i.rindex(")") ]
       json_load=json.loads(apijson)
       html=(json_load['content'])
       val=bs(html,'html.parser')
       val2=val.prettify()
       info1=val.find_all('div',attrs={'class':'team-current-standing'})
       for i in info1:
           results.append(i.text) 
    hometeam_position.append(results[0])
    awayteam_position.append(results[1])

details=[hometeam_position,awayteam_position]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List[0]=Fixture_List[0].str.strip()
Fixture_List[1]=Fixture_List[1].str.strip()
Fixture_List=Fixture_List.rename(columns={0:'Home Table Pos',1:'Away Table Pos'})

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Current Standing Content/P14 Current Standing.csv',index=False)


###############################################################################

homeResults=[]
awayResults=[]
for i in epcr:
    if type(i) is not str:
        homeResults.append(np.nan)
        awayResults.append(np.nan)
    else:    
        apijson = i[ i.index("(") + 1 : i.rindex(")") ]
        json_load=json.loads(apijson)
        html=(json_load['content'])
        val=bs(html,'html.parser')
        val2=val.prettify()
        
        home_team=val.find('div',attrs={'class':'stat-value stat-teamA'})
        away_team=val.find('div',attrs={'class':'stat-value stat-teamB'})
        x=home_team.text
        homeResults.append(x)
        x=away_team.text
        awayResults.append(x)
    
   
details=[homeResults,awayResults]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List[0]=Fixture_List[0].str.strip()
Fixture_List[1]=Fixture_List[1].str.strip()
Fixture_List=Fixture_List.rename(columns={0:'Home Table Pos',1:'Away Table Pos'})

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Current Standing Content/EPCR Current Standing.csv',index=False)


###############################################################################

homeResults=[]
awayResults=[]
for i in chal:
    if type(i) is not str:
        homeResults.append(np.nan)
        awayResults.append(np.nan)
    else:    
        apijson = i[ i.index("(") + 1 : i.rindex(")") ]
        json_load=json.loads(apijson)
        html=(json_load['content'])
        val=bs(html,'html.parser')
        val2=val.prettify()
        
        home_team=val.find('div',attrs={'class':'stat-value stat-teamA'})
        away_team=val.find('div',attrs={'class':'stat-value stat-teamB'})
        x=home_team.text
        homeResults.append(x)
        x=away_team.text
        awayResults.append(x)
    
   
details=[homeResults,awayResults]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List[0]=Fixture_List[0].str.strip()
Fixture_List[1]=Fixture_List[1].str.strip()
Fixture_List=Fixture_List.rename(columns={0:'Home Table Pos',1:'Away Table Pos'})

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Current Standing Content/Chal Current Standing.csv',index=False)
