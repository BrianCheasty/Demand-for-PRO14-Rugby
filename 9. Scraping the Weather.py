import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs

games=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation1.csv',encoding='latin-1')

def maxtemp(row):
    url=row['Stadium URL']
    date=row['Date']
    driver = webdriver.Firefox(executable_path=r'C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Code/geckodriver')
    #driver.maximize_window()
    
    try:
        print('getting '+date+url)
        driver.get(url)
        dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
        dateinput.send_keys(date)
        submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
        content=driver.page_source
        driver.quit()
        html=bs(content, 'html.parser')
        html2=html.find('div',attrs={'class':'weather_prim_info independent'})
        html3=html2.find('div',attrs={'class':'max_temp'})
        html4=html3.find('div',attrs={'class':'count'})
        max_temp=html4.get_text()
        return max_temp 
    except:
        try:
            driver.quit()
            print('Trying getting '+date+url)
            driver.get(url)
            dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
            dateinput.send_keys(date)
            submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
            content=driver.page_source
            driver.quit()
            html=bs(content, 'html.parser')
            html2=html.find('div',attrs={'class':'weather_prim_info independent'})
            html3=html2.find('div',attrs={'class':'max_temp'})
            html4=html3.find('div',attrs={'class':'count'})
            max_temp=html4.get_text()
            return max_temp
        except:
            driver.quit()
            print('failed '+url+date)
            max_temp=''
            return max_temp
pRO14['Max Temp']=pRO14.apply(lambda row:maxtemp(row), axis=1) 

pR014NA=pRO14[(pRO14['Max Temp']=='')]
pR0142=pRO14[(pRO14['Max Temp']!='')]
pR014NA['Max Temp']=pR014NA.apply(lambda row:maxtemp(row), axis=1)

pRO14df=pR0142.append(pR014NA)


def rain(row):
    url=row['Stadium URL']
    date=row['Date']
    driver = webdriver.Firefox(executable_path=r'C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Code/geckodriver')
    #driver.maximize_window()
    
    try:
        print('getting '+date+url)
        driver.get(url)
        dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
        dateinput.send_keys(date)
        submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
        content=driver.page_source
        driver.quit()
        html=bs(content, 'html.parser')
        html2=html.find('div',attrs={'class':'weather_prim_info independent'})
        html3=html2.find('div',attrs={'class':'info_item elem_item'})
        rain=html3.get_text()
        return rain 
    except:
        driver.quit()
        print('Returning Blank')
        rain = ''
        return rain
    
pRO14df['Rain']=pRO14df.apply(lambda row:rain(row), axis=1) 

pR014NA2=pRO14df[(pRO14df['Rain']=='')]
pR014df2=pRO14df[(pRO14df['Rain']!='')]
pR014NA2['Rain']=pR014NA2.apply(lambda row:rain(row), axis=1)

pRO14df_2=pR014df2.append(pR014NA2)    
    
pR014NA3=pRO14df_2[(pRO14df_2['Rain']=='')]
pR0143=pRO14df_2[(pRO14df_2['Rain']!='')]
pR014NA3['Rain']=pR014NA3.apply(lambda row:rain(row), axis=1)    
    
pRO14df_3=pR0143.append(pR014NA3)     
    
def wind(row):
    url=row['Stadium URL']
    date=row['Date']
    driver = webdriver.Firefox(executable_path=r'C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Code/geckodriver')
    #driver.maximize_window()
    
    try:
        print('getting '+date+url)
        driver.get(url)
        dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
        dateinput.send_keys(date)
        submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
        content=driver.page_source
        driver.quit()
        html=bs(content, 'html.parser')
        html2=html.find('div',attrs={'class':'tb_row tb_wind'})
        html3=html2.find_all('div',attrs={'class':'tb_cont_item'})
        wind=[]
        for i in html3:
            x= i.get_text()
            wind.append(x)
        windspeed=wind[6]
        return windspeed
    except:
        driver.quit()
        print('Returning Blank')
        windspeed = ''
        return windspeed
    
pRO14df_3['WindSpeed']=pRO14df_3.apply(lambda row:wind(row), axis=1)     
    
pR014NA4=pRO14df_3[(pRO14df_3['WindSpeed']=='')]
pR0144=pRO14df_3[(pRO14df_3['WindSpeed']!='')]
pR014NA4['WindSpeed']=pR014NA4.apply(lambda row:wind(row), axis=1)    
    
pRO14df_4=pR0144.append(pR014NA4) 

def gettemp(row):
    temp=row['Max Temp'].split('°')
    temps=int(temp[0])
    return temps

pRO14df_4['Temperature']=pRO14df_4.apply(lambda row:gettemp(row), axis=1)

def getrain(row):
    rain=row['Rain'].split(' ')
    raining=float(rain[1])
    return raining

pRO14df_4['Rain Level']=pRO14df_4.apply(lambda row:getrain(row), axis=1)

def getwind(row):
    wind=row['WindSpeed'].split(' ')
    windspeed=int(wind[0])
    return windspeed

pRO14df_4['Wind Speed']=pRO14df_4.apply(lambda row:getwind(row), axis=1)

pRO14df_4=pRO14df_4.rename(columns={'Tournament':'Season'})

pRO14df_5=pRO14df_4[(pRO14df_4['Pool Stage']=='Pool')]

pRO14df_6=pRO14df_5.drop(['home_played','Team Qty','Wins','Pool Stage','Stadium URL','Max Temp','Rain','WindSpeed'],axis=1)

gdp=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Data/GDP.csv',encoding='latin-1')

pRO14df_7=pd.merge(pRO14df_6,gdp,how='left',left_on=['Season','Home Country'],right_on=['Season','Home Country'])

pRO14df_7['Date']=pd.to_datetime(pRO14df_7['Date'])
pRO14df_7['Day Of Week']=pRO14df_7['Date'].dt.dayofweek

def time(row):
    ko=row['Kick Off'].split(':')
    ko2=int(ko[0])
    return ko2
pRO14df_7['Kick Off Hour']=pRO14df_7.apply(lambda row:time(row), axis=1)
pRO14df_7=pRO14df_7.reset_index(drop=True)

pRO14df_8=pRO14df_8.drop(['Date','Kick Off','Home Team','Away Team','Venue'],axis=1)
pRO14df_8=pRO14df_8.drop(['Season'],axis=1)

savedfile=pRO14df_8.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data_set_creation/PRO14/Data/PRO14 Data Set 5.csv',index=False)

'Day Of Week'
