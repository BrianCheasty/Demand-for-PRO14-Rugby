from bs4 import BeautifulSoup as bs
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import pandas as pd
import time



p14=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports HTML/PRO14 HTML.csv', encoding='latin-1')
epcr=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports HTML/EPCR Champions HTML.csv', encoding='latin-1')
chal=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports HTML/EPCR Challenge HTML.csv', encoding='latin-1')

p14=list(p14['0'])
epcr=list(epcr['0'])
chal=list(chal['0'])


def download(url, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'\
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
    time.sleep(1)
    return html

def find_between(s,start,end):
    return (s.split(start))[1].split(end)[0]
##################################################
        
epcr_api=[]
counter=0 
for i in epcr:
    counter+=1
    print(counter)
    if type(i) is not str:
        api2=None
    else:
        first_soup = bs(i, 'html.parser')
        first_api=first_soup.find('div',attrs={'id':'sotic_wp_widget-37-content'})
        text=first_api.prettify()
        split=text.split(' ')
        url = split[8]
        widget_id=split[3]
        param=split[6]
        api_url=[url,widget_id,param]
        api=[]
        for i in api_url:
            start="\""
            end="\""
            elm = find_between(i,start,end)
            api.append(elm)
        api2='https://i7k8x8j8.ssl.hwcdn.net/'+api[1]+'?&params='+api[2]
    epcr_api.append(api2)

  
epcr_api_html=[]
for i in epcr_api:
    if type(i) is not str:
        api=None
    else:
        api=download(i)
    epcr_api_html.append(api)
time.sleep(200)   
epcr_api_df=pd.DataFrame(epcr_api_html)

savedfile=epcr_api_df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Last 3 Meetings/EPCR API.csv', index=False)

###################################################

p14_api=[]
counter=0 
for i in p14:
    counter+=1
    print(counter)
    if type(i) is not str: 
        api2=None
    else:
        first_soup = bs(i, 'html.parser')
        first_api=first_soup.find('div',attrs={'id':'sotic_wp_widget-142-content'})
        text=first_api.prettify()
        split=text.split(' ')
        url2 = split[8]
        widget_id=split[3]
        param=split[6]
        api_url=[url2,widget_id,param]
        api=[]
        for i in api_url:
            start="\""
            end="\""
            elm = find_between(i,start,end)
            api.append(elm)
        api2='https://i7k8x8j8.ssl.hwcdn.net/'+api[1]+'?&params='+api[2]
    p14_api.append(api2)
    
p14_api_html=[]
for i in p14_api:
    if type(i) is not str:
        api=None
    else:
        api=download(i)
    p14_api_html.append(api)
time.sleep(200)   
p14_api_df=pd.DataFrame(p14_api_html)

savedfile=p14_api_df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Last 3 Meetings/P14 API.csv', index=False)


###################################################

chal_api=[]
counter=0 
for i in chal:
    counter+=1
    print(counter)
    if type(i) is not str:
        api2=None
    else:
        first_soup = bs(i, 'html.parser')
        first_api=first_soup.find('div',attrs={'id':'sotic_wp_widget-37-content'})
        text=first_api.prettify()
        split=text.split(' ')
        url2 = split[8]
        widget_id=split[3]
        param=split[6]
        api_url=[url2,widget_id,param]
        api=[]
        for i in api_url:
            start="\""
            end="\""
            elm = find_between(i,start,end)
            api.append(elm)
        api2='https://i7k8x8j8.ssl.hwcdn.net/'+api[1]+'?&params='+api[2]
    chal_api.append(api2)
    
chal_api_html=[]
for i in chal_api:
    if type(i) is not str:
        api=None
    else:
        api=download(i)
    chal_api_html.append(api)
time.sleep(200)   
chal_api_df=pd.DataFrame(chal_api_html)

savedfile=chal_api_df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Last 3 Meetings/Chal API.csv', index=False)
