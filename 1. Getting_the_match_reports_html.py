from bs4 import BeautifulSoup as bs
import itertools
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import pandas as pd
import time


#This script is used to download the html of the relevant match reports from the PRO14
#and EPCR websites

#The following urls are the pages where the match reports are stored, PRO14 has been updated, suggest editing to site map
p14url='https://www.pro14rugby.org/report/page/'
epcrurl='https://www.epcrugby.com/category/champions-cup-match-reports/page/'
chalurl='https://www.epcrugby.com/category/challenge-cup-match-reports/page/'

# A function called download is created to download the html from any pages required
def download(url, user_agent='Insert user agent'\
             , num_retries=2, charset='utf-8'):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    time.sleep(2)
    return html

#The PRO14 page is used first, each page has multiple match reports
p14html=[]
num_errors = 0
max_errors=1
for page in itertools.count(1):
    pg_url = '{}{}'.format(p14url, page)
    each_html= download(pg_url)
    
    if each_html is None:
        num_errors += 1
        if num_errors == max_errors:
                # reached max number of errors, so exit
            break
        else:
            num_errors = 0
    p14html.append(each_html)
time.sleep(200)
#The links for each page are reviewed to pull the link for each match report    
p14links=[]
counter=0
for i in p14html:
    if i is None:
        p14links.append(None)
    else:
        soup=bs(i,'html.parser')
        for j in soup.find_all('h3'):
            for k in j.find_all('a'):
                link2=k.get('href')
                p14links.append(link2)
                counter+=1
                print('Downloading html',counter)
#As we only want the seasons 2015/16 to 2018/19 we split the list to only include the relevant links
#https://www.pro14rugby.org/report/leinster-hold-firm-to-defend-guinness-pro14-title-in-glasgow/
#https://www.pro14rugby.org/report/hoyland-double-allows-edinburgh-to-see-off-leinster/
p14links=p14links[69:643]

p14html_list=[]
for i in p14links:
    x=download(i)
    p14html_list.append(x)

p14htmldf=pd.DataFrame(p14html_list)
savedfile=p14htmldf.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports HTML/PRO14 HTML.csv', index=False)


time.sleep(200) 
#The EPCR Champions cup page is used next   
epcrhtml=[]
num_errors = 0
max_errors=1
for page in itertools.count(1):
    pg_url = '{}{}'.format(epcrurl, page)
    each_html= download(pg_url)
    
    if each_html is None:
        num_errors += 1
        if num_errors == max_errors:
                # reached max number of errors, so exit
            break
        else:
            num_errors = 0
    epcrhtml.append(each_html) 
time.sleep(200) 
#The links for each page are reviewed to pull the link for each match report  
epcrlinks=[]    
for i in epcrhtml:
    soup=bs(i,'html.parser')
    
    for j in soup.find_all('div',attrs={'class':'agg-icon'}):
        for k in j.find_all('a'):
            link2=k.get('href')
            epcrlinks.append(link2)
    
subs='/report/'
res = [i for i in epcrlinks if subs in i]

#As we only want the seasons 2015/16 to 2018/19 we split the list to only include the relevant links
#https://www.epcrugby.com/report/saracens-lift-third-heineken-champions-cup-after-victory-over-leinster/
#to https://www.epcrugby.com/report/report-oconnor-makes-dream-euro-debut/"""
res=res[58:328]

epcrhtml_list=[]
for i in res:
    x=download(i)
    epcrhtml_list.append(x)

epcrhtmldf=pd.DataFrame(epcrhtml_list)
savedfile=epcrhtmldf.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports HTML/EPCR Champions HTML.csv', index=False)

chalhtml=[]
num_errors = 0
max_errors=1
for page in itertools.count(1):
    pg_url = '{}{}'.format(chalurl, page)
    each_html= download(pg_url)
    
    if each_html is None:
        num_errors += 1
        if num_errors == max_errors:
                # reached max number of errors, so exit
            break
        else:
            num_errors = 0
    chalhtml.append(each_html) 

time.sleep(200)    
challinks=[]    
for i in chalhtml:
    soup=bs(i,'html.parser')
    
    for j in soup.find_all('div',attrs={'class':'aggregatorImage'}):
        for k in j.find_all('a'):
            link2=k.get('href')
            challinks.append(link2)
    
subs='/report/'
chalres = [i for i in challinks if subs in i]

chalres=chalres[60:313]
#https://www.epcrugby.com/report/clermont-beat-spirited-harlequins-to-set-up-all-french-final/
#https://www.epcrugby.com/report/report-mighty-quins-hit-montpellier-with-six-of-the-best/

chalhtml_list=[]
for i in chalres:
    x=download(i)
    chalhtml_list.append(x)
    
chalhtmldf=pd.DataFrame(chalhtml_list)
savedfile=chalhtmldf.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports HTML/EPCR Challenge HTML.csv', index=False)
