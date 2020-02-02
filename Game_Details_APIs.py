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

check=p14[0]

p14content=['sotic_wp_widget-132-content','sotic_wp_widget-134-content','sotic_wp_widget-136-content','sotic_wp_widget-141-content','sotic_wp_widget-142-content']
epcrcontent=['sotic_wp_widget-83-content','sotic_wp_widget-36-content','sotic_wp_widget-158-content','sotic_wp_widget-155-content','sotic_wp_widget-37-content','sotic_wp_widget-121-content','sotic_wp_widget-122-content']


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
link=0
for j in epcrcontent:
    link+=1
    counter=0
    print(link)
    apiz=[]
    for i in epcr:
        if type(i) is not str:
            api2=None
        else:
            counter+=1
            print(str(link) + ' & ' + str(counter))
            first_soup = bs(i, 'html.parser')
            first_api=first_soup.find('div',attrs={'id':j})
            if type(first_api) is None:
                api2=None
            else:
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
        apiz.append(api2)
    epcr_api.append(apiz)
 
epcr_api_html=[]
for i in epcr_api:
    apix=[]
    for j in i:
        if type(j) is not str:
            api=None
        else:
            api=download(j)
        apix.append(api)
    epcr_api_html.append(apix)
time.sleep(200)   
epcr_api_df=pd.DataFrame(epcr_api_html)
epcr_Api_df=epcr_api_df.T

savedfile=epcr_Api_df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/epcr API Full.csv', index=False)

###################################################

p14_api=[]
link=0
for j in p14content:
    link+=1
    counter=0
    print(link)
    apiz=[]
    for i in p14:
        counter+=1
        print(str(link) + ' & ' + str(counter))
        first_soup = bs(i, 'html.parser')
        first_api=first_soup.find('div',attrs={'id':j})
        if type(first_api) is None:
            api2=None
        else:
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
        apiz.append(api2)
    p14_api.append(apiz)
 
p14_api_html=[]
for i in p14_api:
    apix=[]
    for j in i:
        if type(j) is not str:
            api=None
        else:
            api=download(j)
        apix.append(api)
    p14_api_html.append(apix)
time.sleep(200)   
p14_api_df=pd.DataFrame(p14_api_html)
p14_Api_df=p14_api_df.T

savedfile=p14_Api_df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/P14 API Full.csv', index=False)


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
        first_api=first_soup.find('div',attrs={'class':'sotic-widget-content'})
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
for type(i) in chal_api:
    if i is not str:
        api=None
    else:
        api=download(i)
    chal_api_html.append(api)
time.sleep(200)   
chal_api_df=pd.DataFrame(chal_api_html)

savedfile=chal_api_df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Game Stats/Chal API.csv', index=False)
