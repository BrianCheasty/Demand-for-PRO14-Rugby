import pandas as pd
import json
from bs4 import BeautifulSoup as bs
import numpy as np

p14=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Game Stats/P14 API.csv', encoding='latin-1')
epcr=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Game Stats/EPCR API.csv', encoding='latin-1')
chal=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Game Stats/CHAL API.csv', encoding='latin-1')

p14=list(p14['0'])
epcr=list(epcr['0'])
chal=list(chal['0'])


###############################################################################  
p14tournament=[]
p14matchRound=[]
p14hometeam=[]
p14Score=[]
p14awayteam=[]
p14date=[]
p14venue=[]
p14attend=[]
p14kick_off=[]
p14ref=[]
   
# The JSON data contains a value which is html code, the following extracts the 
# html code, parses it and extracts the values 


for i in p14:
    if type(i) is not str:
        p14tournament.append(np.nan)
        p14matchRound.append(np.nan)
        p14hometeam.append(np.nan)
        p14Score.append(np.nan)
        p14awayteam.append(np.nan)
        p14date.append(np.nan)
        p14venue.append(np.nan)
        p14attend.append(np.nan)
        p14kick_off.append(np.nan)
        p14ref.append(np.nan)
    else:    
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
        p14hometeam.append(home_Team)
        score_ = val.find('div',attrs={'class':'team-fixtureInfo-score'})
        score__= score_.find('span',attrs={'class':'fixtureInfo-v_score'})
        if score__ is None:
            score=''
        else:
            score=score__.text
        p14Score.append(score)
        away_ = val.find('div',attrs={'class':'teamb_name name'})
        away__= away_.find('span',attrs={'class':'fullname'})
        if away__ is None:
            away_Team=''
        else:
            away_Team=away__.text
        p14awayteam.append(away_Team)
        fixinfo_ = val.find('div',attrs={'class':'fixtureInfo-meta-top'})
        info__= fixinfo_.find('span',attrs={'class':'fix-date'})
        if info__ is None:
            match_date=''
        else:
            match_date=info__.text
        p14date.append(match_date)
        info__= fixinfo_.find('span',attrs={'class':'fix-ven'})
        if info__ is None:
            match_venue=''
        else:
            match_venue=info__.text
        p14venue.append(match_venue)
        fixinfo_ = val.find('div',attrs={'class':'fixtureInfo-meta-bottom'})
        info__= fixinfo_.find('span',attrs={'class':'fix-ref'})
        if info__ is None:
            match_ref=''
        else:
            match_ref=info__.text
        p14ref.append(match_ref)
        p14tournament.append('League')
        info__= fixinfo_.find('span',attrs={'class':'fix-att'})
        if info__ is None:
            attendance=''
        else:
            attendance=info__.text
        p14attend.append(attendance)
        fixinfo_ = val.find('script',attrs={'type':'text/javascript'})
        fixtime=fixinfo_.prettify()
        left = 'var countdownendtime = \"'
        time1=((fixtime.split(left))[1])
        time2=time1.split('\"')
        Kick_Off=time2[0]
        p14kick_off.append(Kick_Off)
    




details=[p14tournament,p14matchRound,p14date,p14kick_off,p14hometeam,p14Score,p14awayteam,p14venue,\
         p14attend,p14ref]
p14fixture_list=pd.DataFrame(details)
p14Fixture_List=p14fixture_list.T
p14Fixture_List=p14Fixture_List.rename(columns={0:'Tournament',1:'Round',2:'Date',\
                                          3:'Kick Off',4:'Home Team',5:'Score'\
                                          ,6:'Away Team',7:'Venue',8:'Attendance',9:'Ref'})
    
p14Fixture_List.info()

p14Fixture_List['Date']=pd.to_datetime(p14Fixture_List['Date'],errors='coerce')

p14Fixture_List=p14Fixture_List[(p14Fixture_List['Date'].notnull())]
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

p14Fixture_List['Season']=p14Fixture_List.apply(lambda row: addSeason(row), axis=1)

savedFile=p14Fixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Main Content/P14 Main Content.csv'\
                              ,index=False)

############################################################################### 

epcrtournament=[]
epcrmatchRound=[]
epcrhometeam=[]
epcrScore=[]
epcrawayteam=[]
epcrdate=[]
epcrvenue=[]
epcrattend=[]
epcrkick_off=[]
epcrref=[]

for i in epcr:
    if type(i) is not str:
        epcrtournament.append(np.nan)
        epcrmatchRound.append(np.nan)
        epcrhometeam.append(np.nan)
        epcrScore.append(np.nan)
        epcrawayteam.append(np.nan)
        epcrdate.append(np.nan)
        epcrvenue.append(np.nan)
        epcrattend.append(np.nan)
        epcrkick_off.append(np.nan)
        epcrref.append(np.nan)
    else:    
        apijson = i[ i.index("(") + 1 : i.rindex(")") ]
        json_load=json.loads(apijson)
        html=(json_load['content'])
        val=bs(html,'html.parser')
        
        home_team=val.find('div',attrs={'class':'matchNames-teamA teamName'})
        if home_team is None:
            home_Team=''
        else:
            home_Team=home_team.text
        epcrhometeam.append(home_Team)
        hscore_ = val.find('div',attrs={'class':'matchScore-teamA'})
        if hscore_ is None:
            hscore=''
        else:
            hscore=hscore_.text
        ascore_ = val.find('div',attrs={'class':'matchScore-teamB'})
        if ascore_ is None:
            ascore=''
        else:
            ascore=ascore_.text
        score=str(hscore)+' - '+str(ascore)
        epcrScore.append(score)
        away__ = val.find('div',attrs={'class':'matchNames-teamB teamName'})
        if away__ is None:
            away_Team=''
        else:
            away_Team=away__.text
        epcrawayteam.append(away_Team)
        fixinfo_ = val.find('div',attrs={'class':'matchPage-matchMeta'})
        if fixinfo_ is None:
            match_date=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchDate'})
            match_date=info__.text
        epcrdate.append(match_date)
        if fixinfo_ is None:
            match_venue=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchVenue'})
            match_venue=info__.text
        epcrvenue.append(match_venue)
        fixinfo_ = val.find('div',attrs={'class':'matchMeta-bottom'})
        if fixinfo_ is None:
            match_ref=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchRef'})
            if info__ is None:
                match_ref=''
            else:
                match_ref=info__.text
        epcrref.append(match_ref)
        epcrtournament.append('Champions Cup')
        if fixinfo_ is None:
            attendance=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchAtt'})
            if info__ is None:
                attendance=''
            else:
                attendance=info__.text
        epcrattend.append(attendance)
        epcrkick_off.append(np.nan)
        fixinfo_ = val.find('div',attrs={'class':'matchMeta-middle'})
        if fixinfo_ is None:
            mround=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchRound'})
            mround=info__.text
        epcrmatchRound.append(mround)
    
details=[epcrtournament,epcrmatchRound,epcrdate,epcrkick_off,epcrhometeam,epcrScore,epcrawayteam,epcrvenue,
         epcrattend,epcrref]
epcrfixture_list=pd.DataFrame(details)
epcrFixture_List=epcrfixture_list.T
epcrFixture_List=epcrFixture_List.rename(columns={0:'Tournament',1:'Round',2:'Date',
                                          3:'Kick Off',4:'Home Team',5:'Score'
                                          ,6:'Away Team',7:'Venue',8:'Attendance',9:'Ref'})
    
epcrFixture_List.info()

epcrFixture_List['Date']=pd.to_datetime(epcrFixture_List['Date'],errors='coerce')

epcrFixture_List=epcrFixture_List[(epcrFixture_List['Date'].notnull())]

epcrFixture_List['Season']=epcrFixture_List.apply(lambda row: addSeason(row), axis=1)
epcrFixture_List['Round']=epcrFixture_List['Round'].str.strip()
epcrFixture_List['Score']=epcrFixture_List['Score'].str.strip()
epcrFixture_List['Venue']=epcrFixture_List['Venue'].str.strip()
epcrFixture_List['Attendance']=epcrFixture_List['Attendance'].str.strip()
epcrFixture_List['Ref']=epcrFixture_List['Ref'].str.strip()
savedFile=epcrFixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Main Content/EPCR Main Content.csv'
                              ,index=False)



############################################################################### 

chaltournament=[]
chalmatchRound=[]
chalhometeam=[]
chalScore=[]
chalawayteam=[]
chaldate=[]
chalvenue=[]
chalattend=[]
chalkick_off=[]
chalref=[]

for i in chal:
    if type(i) is not str:
        chaltournament.append(np.nan)
        chalmatchRound.append(np.nan)
        chalhometeam.append(np.nan)
        chalScore.append(np.nan)
        chalawayteam.append(np.nan)
        chaldate.append(np.nan)
        chalvenue.append(np.nan)
        chalattend.append(np.nan)
        chalkick_off.append(np.nan)
        chalref.append(np.nan)
    else:    
        apijson = i[ i.index("(") + 1 : i.rindex(")") ]
        json_load=json.loads(apijson)
        html=(json_load['content'])
        val=bs(html,'html.parser')
        
        home_team=val.find('div',attrs={'class':'matchNames-teamA teamName'})
        if home_team is None:
            home_Team=''
        else:
            home_Team=home_team.text
        chalhometeam.append(home_Team)
        hscore_ = val.find('div',attrs={'class':'matchScore-teamA'})
        if hscore_ is None:
            hscore=''
        else:
            hscore=hscore_.text
        ascore_ = val.find('div',attrs={'class':'matchScore-teamB'})
        if ascore_ is None:
            ascore=''
        else:
            ascore=ascore_.text
        score=str(hscore)+' - '+str(ascore)
        chalScore.append(score)
        away__ = val.find('div',attrs={'class':'matchNames-teamB teamName'})
        if away__ is None:
            away_Team=''
        else:
            away_Team=away__.text
        chalawayteam.append(away_Team)
        fixinfo_ = val.find('div',attrs={'class':'matchPage-matchMeta'})
        if fixinfo_ is None:
            match_date=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchDate'})
            match_date=info__.text
        chaldate.append(match_date)
        if fixinfo_ is None:
            match_venue=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchVenue'})
            match_venue=info__.text
        chalvenue.append(match_venue)
        fixinfo_ = val.find('div',attrs={'class':'matchMeta-bottom'})
        if fixinfo_ is None:
            match_ref=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchRef'})
            if info__ is None:
                match_ref=''
            else:
                match_ref=info__.text
        chalref.append(match_ref)
        chaltournament.append('Champions Cup')
        if fixinfo_ is None:
            attendance=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchAtt'})
            if info__ is None:
                attendance=''
            else:
                attendance=info__.text
        chalattend.append(attendance)
        chalkick_off.append(np.nan)
        fixinfo_ = val.find('div',attrs={'class':'matchMeta-middle'})
        if fixinfo_ is None:
            mround=''
        else:
            info__= fixinfo_.find('span',attrs={'class':'matchRound'})
            mround=info__.text
        chalmatchRound.append(mround)
    
details=[chaltournament,chalmatchRound,chaldate,chalkick_off,chalhometeam,chalScore,chalawayteam,chalvenue,
         chalattend,chalref]
chalfixture_list=pd.DataFrame(details)
chalFixture_List=chalfixture_list.T
chalFixture_List=chalFixture_List.rename(columns={0:'Tournament',1:'Round',2:'Date',
                                          3:'Kick Off',4:'Home Team',5:'Score'
                                          ,6:'Away Team',7:'Venue',8:'Attendance',9:'Ref'})
    
chalFixture_List.info()

chalFixture_List['Date']=pd.to_datetime(chalFixture_List['Date'],errors='coerce')

chalFixture_List=chalFixture_List[(chalFixture_List['Date'].notnull())]

chalFixture_List['Season']=chalFixture_List.apply(lambda row: addSeason(row), axis=1)
chalFixture_List['Round']=chalFixture_List['Round'].str.strip()
chalFixture_List['Score']=chalFixture_List['Score'].str.strip()
chalFixture_List['Venue']=chalFixture_List['Venue'].str.strip()
chalFixture_List['Attendance']=chalFixture_List['Attendance'].str.strip()
chalFixture_List['Ref']=chalFixture_List['Ref'].str.strip()
savedFile=chalFixture_List.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Main Content/CHAL Main Content.csv'
                              ,index=False)