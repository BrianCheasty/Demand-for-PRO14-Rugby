import pandas as pd
import json
from bs4 import BeautifulSoup as bs
import numpy as np

p14=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/P14 API full.csv', encoding='latin-1')
epcr=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/epcr API full.csv', encoding='latin-1')
chal=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/chal API full.csv', encoding='latin-1')

p14=list(p14['3'])
epcr=list(epcr['3'])
chal=list(chal['3'])


############################################################################### 

Season_So_far=[]
for i in p14:
    if type(i) is not str:
        Season_So_far.append(np.nan)
    else:
        apijson = i[ i.index("(") + 1 : i.rindex(")") ]
        json_load=json.loads(apijson)
        html=(json_load['content'])
        val=bs(html,'html.parser')
        val2=val.prettify()
        info=val.find('table',attrs={'class':'seasonSoFar table'})
        table_body = info.find('tbody')
        rows = table_body.find_all('tr')
        data=[]
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty values
        Season_So_far.append(data)
    
total_points=[]
tries=[]
conversions=[]
dropgoals=[]
penalties=[]
metres_gained=[]
carries=[]
passes_made=[]
tackles_made=[]
tackles_missed=[]
turnovers_won=[]
turnovers_conceded=[]
penalties_conceded=[]
yellow_cards=[]
red_cards=[]

for i in Season_So_far:
    #total_points.append(i[0])
    tries.append(i[1])
    #conversions.append(i[2])
    #dropgoals.append(i[3])
    #penalties.append(i[4])
    metres_gained.append(i[5])
    #carries.append(i[6])
    passes_made.append(i[7])
    tackles_made.append(i[8])
    #tackles_missed.append(i[9])
    turnovers_won.append(i[10])
   #turnovers_conceded.append(i[11])
    penalties_conceded.append(i[12])
    #yellow_cards.append(i[13])
    #red_cards.append(i[14])
    
#home_total_score =[]
#for i in total_points:
#    home_total_score.append(i[0])
#away_total_score =[]
#for i in total_points:
#    away_total_score.append(i[2])  
home_total_tries =[]
for i in tries:
    home_total_tries.append(i[0])
away_total_tries =[]
for i in tries:
    away_total_tries.append(i[2])
#home_total_conversions =[]
#for i in conversions:
#    home_total_conversions.append(i[0])
#away_total_conversions =[]
#for i in conversions:
#    away_total_conversions.append(i[2])
#home_total_dropgoals =[]
#for i in dropgoals:
#    home_total_dropgoals.append(i[0])
#away_total_dropgoals =[]
#for i in dropgoals:
#    away_total_dropgoals.append(i[2])
#home_total_penalties =[]
#for i in penalties:
#    home_total_penalties.append(i[0])
#away_total_penalties =[]
#for i in penalties:
#    away_total_penalties.append(i[2])
home_total_metres_gained =[]
for i in metres_gained:
    home_total_metres_gained.append(i[0])
away_total_metres_gained =[]
for i in metres_gained:
    away_total_metres_gained.append(i[2])
#home_total_carries =[]
#for i in carries:
#    home_total_carries.append(i[0])
#away_total_carries =[]
#for i in carries:
#    away_total_carries.append(i[2])
home_total_passes_made =[]
for i in passes_made:
    home_total_passes_made.append(i[0])
away_total_passes_made =[]
for i in passes_made:
    away_total_passes_made.append(i[2])
home_total_tackles_made =[]
for i in tackles_made:
    home_total_tackles_made.append(i[0])
away_total_tackles_made =[]
for i in tackles_made:
    away_total_tackles_made.append(i[2])
#home_total_tackles_missed =[]
#for i in tackles_missed:
#    home_total_tackles_missed.append(i[0])
#away_total_tackles_missed =[] 
#for i in tackles_missed:
#    away_total_tackles_missed.append(i[2])
home_total_turnovers_won =[] 
for i in turnovers_won:
    home_total_turnovers_won.append(i[0])
away_total_turnovers_won =[]
for i in turnovers_won:
    away_total_turnovers_won.append(i[2])
home_total_turnovers_conceded =[]
#for i in turnovers_conceded:
#    home_total_turnovers_conceded.append(i[0])
#away_total_turnovers_conceded =[]
#for i in turnovers_conceded:
#    away_total_turnovers_conceded.append(i[2])
home_total_penalties_conceded =[]
for i in penalties_conceded:
    home_total_penalties_conceded.append(i[0])
away_total_penalties_conceded =[]
for i in penalties_conceded:
    away_total_penalties_conceded.append(i[2])
#home_total_yellow_cards =[]
#for i in yellow_cards:
#    home_total_yellow_cards.append(i[0])
#away_total_yellow_cards =[]
#for i in yellow_cards:
#    away_total_yellow_cards.append(i[2])
#home_total_red_cards =[]
#for i in red_cards:
#    home_total_red_cards.append(i[0])
#away_total_red_cards =[]
#for i in red_cards:
#    away_total_red_cards.append(i[2])



details=[home_total_tries,away_total_tries,\
         home_total_metres_gained,away_total_metres_gained,\
         home_total_passes_made,away_total_passes_made,\
         home_total_tackles_made,away_total_tackles_made,\
         home_total_turnovers_won,away_total_turnovers_won,\
         home_total_penalties_conceded,away_total_penalties_conceded]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List=Fixture_List.rename(columns={0:'Home Total Tries',1: 'Away Total Tries',\
                                          2:'Home Total Metres Gained',3:'Away Total Metres Gained',
                                          4:'Home Total Passes Made',5:'Away Total Passes Made',\
                                          6:'Home Total Tackles Made',7:'Away Total Tackles Made',
                                          8:'Home Total Turnovers Won',9:'Away Total Turnovers Won',\
                                          10:'Home Total Penalties Conceded',11:'Away Total Penalties Conceded'})

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Season So Far Content/P14 Season So Far.csv',index=False)

###############################################################################  

home_total_tries=[]
away_total_tries=[]
home_total_metres_gained=[]
away_total_metres_gained=[]
home_total_passes_made=[]
away_total_passes_made=[]
home_total_tackles_made=[]
away_total_tackles_made=[]
home_total_turnovers_won=[]
away_total_turnovers_won=[]
home_total_penalties_conceded=[]
away_total_penalties_conceded=[]
homeResults=[]
awayResults=[]
for i in epcr:
    if type(i) is not str:
        homeResults.append([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
        awayResults.append([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    else:    
        home_results=[]
        away_results=[]
        apijson = i[ i.index("(") + 1 : i.rindex(")") ]
        json_load=json.loads(apijson)
        html=(json_load['content'])
        val=bs(html,'html.parser')
        val2=val.prettify()
        
        home_team=val.find_all('div',attrs={'class':'stat-value stat-teamA'})
        away_team=val.find_all('div',attrs={'class':'stat-value stat-teamB'})
        if home_team is None:
            home_results.append([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
        else:
            for i in home_team:
                x=i.text
                home_results.append(x)
        if away_team is None:
            away_results.append([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
        else:
            for i in away_team:
                x=i.text
                away_results.append(x)
    homeResults.append(home_results)
    awayResults.append(away_results)
    
for i in homeResults:
    home_total_tries.append(i[0])
for i in homeResults:
    home_total_metres_gained.append(i[1])
for i in homeResults:
    home_total_passes_made.append(i[2])
for i in homeResults:
    home_total_tackles_made.append(i[3])
for i in homeResults:
    home_total_turnovers_won.append(i[4])
for i in homeResults:
    home_total_penalties_conceded.append(i[5])
    
for i in awayResults:
    away_total_tries.append(i[0])
for i in awayResults:
    away_total_metres_gained.append(i[1])
for i in awayResults:
    away_total_passes_made.append(i[2])
for i in awayResults:
    away_total_tackles_made.append(i[3])
for i in awayResults:
    away_total_turnovers_won.append(i[4])
for i in awayResults:
    away_total_penalties_conceded.append(i[5])
    
details=[home_total_tries,away_total_tries,\
         home_total_metres_gained,away_total_metres_gained,\
         home_total_passes_made,away_total_passes_made,\
         home_total_tackles_made,away_total_tackles_made,\
         home_total_turnovers_won,away_total_turnovers_won,\
         home_total_penalties_conceded,away_total_penalties_conceded]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List[0]=Fixture_List[0].str.strip()
Fixture_List[1]=Fixture_List[1].str.strip()
Fixture_List[2]=Fixture_List[2].str.strip()
Fixture_List[3]=Fixture_List[3].str.strip()
Fixture_List[4]=Fixture_List[4].str.strip()
Fixture_List[5]=Fixture_List[5].str.strip()
Fixture_List[6]=Fixture_List[6].str.strip()
Fixture_List[7]=Fixture_List[7].str.strip()
Fixture_List[8]=Fixture_List[8].str.strip()
Fixture_List[9]=Fixture_List[9].str.strip()
Fixture_List[10]=Fixture_List[10].str.strip()
Fixture_List[11]=Fixture_List[11].str.strip()
Fixture_List=Fixture_List.rename(columns={0:'Home Total Tries',1: 'Away Total Tries',\
                                          2:'Home Total Metres Gained',3:'Away Total Metres Gained',
                                          4:'Home Total Passes Made',5:'Away Total Passes Made',\
                                          6:'Home Total Tackles Made',7:'Away Total Tackles Made',
                                          8:'Home Total Turnovers Won',9:'Away Total Turnovers Won',\
                                          10:'Home Total Penalties Conceded',11:'Away Total Penalties Conceded'})

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Season So Far Content/EPCR Season So Far.csv',index=False)


#################################################################

home_total_tries=[]
away_total_tries=[]
home_total_metres_gained=[]
away_total_metres_gained=[]
home_total_passes_made=[]
away_total_passes_made=[]
home_total_tackles_made=[]
away_total_tackles_made=[]
home_total_turnovers_won=[]
away_total_turnovers_won=[]
home_total_penalties_conceded=[]
away_total_penalties_conceded=[]
homeResults=[]
awayResults=[]
for i in chal:
    if type(i) is not str:
        homeResults.append([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
        awayResults.append([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    else:    
        home_results=[]
        away_results=[]
        apijson = i[ i.index("(") + 1 : i.rindex(")") ]
        json_load=json.loads(apijson)
        html=(json_load['content'])
        val=bs(html,'html.parser')
        val2=val.prettify()
        
        home_team=val.find_all('div',attrs={'class':'stat-value stat-teamA'})
        away_team=val.find_all('div',attrs={'class':'stat-value stat-teamB'})
        if home_team is None:
            home_results.append([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
        else:
            for i in home_team:
                x=i.text
                home_results.append(x)
        if away_team is None:
            away_results.append([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
        else:
            for i in away_team:
                x=i.text
                away_results.append(x)
    homeResults.append(home_results)
    awayResults.append(away_results)
    
for i in homeResults:
    home_total_tries.append(i[0])
for i in homeResults:
    home_total_metres_gained.append(i[1])
for i in homeResults:
    home_total_passes_made.append(i[2])
for i in homeResults:
    home_total_tackles_made.append(i[3])
for i in homeResults:
    home_total_turnovers_won.append(i[4])
for i in homeResults:
    home_total_penalties_conceded.append(i[5])
    
for i in awayResults:
    away_total_tries.append(i[0])
for i in awayResults:
    away_total_metres_gained.append(i[1])
for i in awayResults:
    away_total_passes_made.append(i[2])
for i in awayResults:
    away_total_tackles_made.append(i[3])
for i in awayResults:
    away_total_turnovers_won.append(i[4])
for i in awayResults:
    away_total_penalties_conceded.append(i[5])
    
details=[home_total_tries,away_total_tries,
         home_total_metres_gained,away_total_metres_gained,
         home_total_passes_made,away_total_passes_made,
         home_total_tackles_made,away_total_tackles_made,
         home_total_turnovers_won,away_total_turnovers_won,
         home_total_penalties_conceded,away_total_penalties_conceded]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List[0]=Fixture_List[0].str.strip()
Fixture_List[1]=Fixture_List[1].str.strip()
Fixture_List[2]=Fixture_List[2].str.strip()
Fixture_List[3]=Fixture_List[3].str.strip()
Fixture_List[4]=Fixture_List[4].str.strip()
Fixture_List[5]=Fixture_List[5].str.strip()
Fixture_List[6]=Fixture_List[6].str.strip()
Fixture_List[7]=Fixture_List[7].str.strip()
Fixture_List[8]=Fixture_List[8].str.strip()
Fixture_List[9]=Fixture_List[9].str.strip()
Fixture_List[10]=Fixture_List[10].str.strip()
Fixture_List[11]=Fixture_List[11].str.strip()
Fixture_List=Fixture_List.rename(columns={0:'Home Total Tries',1: 'Away Total Tries',
                                          2:'Home Total Metres Gained',3:'Away Total Metres Gained',
                                          4:'Home Total Passes Made',5:'Away Total Passes Made',
                                          6:'Home Total Tackles Made',7:'Away Total Tackles Made',
                                          8:'Home Total Turnovers Won',9:'Away Total Turnovers Won',
                                          10:'Home Total Penalties Conceded',11:'Away Total Penalties Conceded'})

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Season So Far Content/Chal Season So Far.csv',index=False)


#################################################################