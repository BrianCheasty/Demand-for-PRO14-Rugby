import pandas as pd
import json
from bs4 import BeautifulSoup as bs

p14=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Game Stats/P14 API.csv', encoding='latin-1')
epcr=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Game Stats/EPCR API.csv', encoding='latin-1')
chal=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Game Stats/CHAL API.csv', encoding='latin-1')

p14=list(p14['0'])
epcr=list(epcr['0'])
chal=list(chal['0'])

tournament=[]
matchRound=[]
hometeam=[]
Score=[]
awayteam=[]
date=[]
venue=[]
attend=[]
kick_off=[]
ref=[]
   
# The JSON data contains a value which is html code, the following extracts the 
# html code, parses it and extracts the values    
for i in p14:
    apijson = i[ i.index("(") + 1 : i.rindex(")") ]
    json_load=json.loads(apijson)
    html=(json_load['content'])
    val=bs(html,'html.parser')
    val2=val.prettify()
    Home_team=val.find('div',attrs={'class':'teama_name name'})
    home_team=Home_team.find('span',attrs={'class':'fullname'})
    if home_team is None:
        home_Team=''
    else:
        home_Team=home_team.text
    hometeam.append(home_Team)
    score_ = val.find('div',attrs={'class':'team-fixtureInfo-score'})
    score__= score_.find('span',attrs={'class':'fixtureInfo-v_score'})
    if score__ is None:
        score=''
    else:
        score=score__.text
    Score.append(score)
    away_ = val.find('div',attrs={'class':'teamb_name name'})
    away__= away_.find('span',attrs={'class':'fullname'})
    if away__ is None:
        away_Team=''
    else:
        away_Team=away__.text
    awayteam.append(away_Team)
    fixinfo_ = val.find('div',attrs={'class':'fixtureInfo-meta-top'})
    info__= fixinfo_.find('span',attrs={'class':'fix-date'})
    if info__ is None:
        match_date=''
    else:
        match_date=info__.text
    date.append(match_date)
    info__= fixinfo_.find('span',attrs={'class':'fix-ven'})
    if info__ is None:
        match_venue=''
    else:
        match_venue=info__.text
    venue.append(match_venue)
    fixinfo_ = val.find('div',attrs={'class':'fixtureInfo-meta-bottom'})
    info__= fixinfo_.find('span',attrs={'class':'fix-ref'})
    if info__ is None:
        match_ref=''
    else:
        match_ref=info__.text
    ref.append(match_ref)
    tournament.append('League')
    info__= fixinfo_.find('span',attrs={'class':'fix-att'})
    if info__ is None:
        attendance=''
    else:
        attendance=info__.text
    attend.append(attendance)
    fixinfo_ = val.find('script',attrs={'type':'text/javascript'})
    fixtime=fixinfo_.prettify()
    left = 'var countdownendtime = \"'
    time1=((fixtime.split(left))[1])
    time2=time1.split('\"')
    Kick_Off=time2[0]
    kick_off.append(Kick_Off)
    




details=[tournament,matchRound,date,kick_off,hometeam,Score,awayteam,venue,\
         attend,ref]
fixture_list=pd.DataFrame(details)
Fixture_List=fixture_list.T
Fixture_List=Fixture_List.rename(columns={0:'Tournament',1:'Round',2:'Date',\
                                          3:'Kick Off',4:'Home Team',5:'Score'\
                                          ,6:'Away Team',7:'Venue',8:'Attendance',9:'Ref'})
    
Fixture_List.info()

Fixture_List['Date']=pd.to_datetime(Fixture_List['Date'],errors='coerce')

test=pd.to_datetime('2003-07-15 00:00:00')
Fixture_List=Fixture_List[(Fixture_List['Date'].notnull())]
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

Fixture_List['Season']=Fixture_List.apply(lambda row: addSeason(row), axis=1)

savedFile=Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Data/Main Statistics B.csv'\
                              ,index=False)
