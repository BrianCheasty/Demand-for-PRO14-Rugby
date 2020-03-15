import pandas as pd
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

#time1=time.time()
#
#games=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation1.csv',encoding='latin-1')
##games=games.loc[0:1,:]
#def maxtemp(row):
#    url=row['Stadium URL']
#    date=row['Date']
#    driver = webdriver.Firefox(executable_path=r'C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Code/Demand-for-PRO14-Rugby/geckodriver')
#    #driver.maximize_window()
#    
#    try:
#            print('Trying getting '+date+url)
#            driver.get(url)
#            dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
#            dateinput.send_keys(date)
#            submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
#            content=driver.page_source
#            driver.quit()
#            html=bs(content, 'html.parser')
#            
#            html2=html.find('div',attrs={'class':'weather_prim_info independent'})
#            html3=html2.find('div',attrs={'class':'max_temp'})
#            html4=html3.find('div',attrs={'class':'count'})
#            max_temp=html4.get_text()
#            html5=html2.find('div',attrs={'class':'info_item elem_item'})
#            rain=html5.get_text()
#            html5=html.find('div',attrs={'class':'tb_row tb_wind'})
#            html6=html5.find_all('div',attrs={'class':'tb_cont_item'})
#            wind=[]
#            for i in html6:
#                x= i.get_text()
#                wind.append(x)
#            windspeed=wind[6]
#            return max_temp,rain,windspeed
#    except:
#        try:
#            driver.quit()
#            print('Trying getting '+date+url)
#            driver.get(url)
#            dateinput= driver.find_element_by_id('ctl00_MainContentHolder_txtPastDate')
#            dateinput.send_keys(date)
#            submit=driver.find_element_by_id("ctl00_MainContentHolder_butShowPastWeather").click()
#            content=driver.page_source
#            driver.quit()
#            html=bs(content, 'html.parser')
#            
#            html2=html.find('div',attrs={'class':'weather_prim_info independent'})
#            html3=html2.find('div',attrs={'class':'max_temp'})
#            html4=html3.find('div',attrs={'class':'count'})
#            max_temp=html4.get_text()
#            html5=html2.find('div',attrs={'class':'info_item elem_item'})
#            rain=html5.get_text()
#            html5=html.find('div',attrs={'class':'tb_row tb_wind'})
#            html6=html5.find_all('div',attrs={'class':'tb_cont_item'})
#            wind=[]
#            for i in html6:
#                x= i.get_text()
#                wind.append(x)
#            windspeed=wind[6]
#            return max_temp,rain,windspeed
#        except:
#            driver.quit()
#            print('failed '+url+date)
#            max_temp=np.nan
#            rain=np.nan
#            windspeed=np.nan
#            return max_temp,rain,windspeed
#games['Temperature'],games['Rain'],games['Wind']=zip(*games.apply(lambda row:maxtemp(row), axis=1))
#time2=time.time()
#tottime=(time2-time1)/60
#print('The total time was '+str(tottime)+' Minutes')
#
#
#def gettemp(row):
#    temp=row['Temperature'].split('°')
#    temps=int(temp[0])
#    return temps
#games['Max Temperature']=games.apply(lambda row:gettemp(row), axis=1)
#
#def getrain(row):
#    rain=row['Rain'].split(' ')
#    raining=float(rain[1])
#    return raining
#games['Rain Level']=games.apply(lambda row:getrain(row), axis=1)
#
#def getwind(row):
#    wind=row['Wind'].split(' ')
#    windspeed=int(wind[0])
#    return windspeed
#games['Wind Speed']=games.apply(lambda row:getwind(row), axis=1)
#
#games.info()
#
#games=games.drop(columns=['Temperature','Rain','Wind','Stadium URL','Pool Stage'])
#
#savedfile=games.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation2.csv',index=False)


time1=time.time()

games=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation1b.csv',encoding='latin-1')
#games=games.loc[0:1,:]
def maxtemp(row):
    url=row['Stadium URL']
    date=row['Date']
    driver = webdriver.Firefox(executable_path=r'C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Code/Demand-for-PRO14-Rugby/geckodriver')
    #driver.maximize_window()
    
    try:
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
            html5=html2.find('div',attrs={'class':'info_item elem_item'})
            rain=html5.get_text()
            html5=html.find('div',attrs={'class':'tb_row tb_wind'})
            html6=html5.find_all('div',attrs={'class':'tb_cont_item'})
            wind=[]
            for i in html6:
                x= i.get_text()
                wind.append(x)
            windspeed=wind[6]
            return max_temp,rain,windspeed
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
            html5=html2.find('div',attrs={'class':'info_item elem_item'})
            rain=html5.get_text()
            html5=html.find('div',attrs={'class':'tb_row tb_wind'})
            html6=html5.find_all('div',attrs={'class':'tb_cont_item'})
            wind=[]
            for i in html6:
                x= i.get_text()
                wind.append(x)
            windspeed=wind[6]
            return max_temp,rain,windspeed
        except:
            driver.quit()
            print('failed '+url+date)
            max_temp=np.nan
            rain=np.nan
            windspeed=np.nan
            return max_temp,rain,windspeed
games['Temperature'],games['Rain'],games['Wind']=zip(*games.apply(lambda row:maxtemp(row), axis=1))
time2=time.time()
tottime=(time2-time1)/60
print('The total time was '+str(tottime)+' Minutes')


def gettemp(row):
    temp=row['Temperature'].split('°')
    temps=int(temp[0])
    return temps
games['Max Temperature']=games.apply(lambda row:gettemp(row), axis=1)

def getrain(row):
    rain=row['Rain'].split(' ')
    raining=float(rain[1])
    return raining
games['Rain Level']=games.apply(lambda row:getrain(row), axis=1)

def getwind(row):
    wind=row['Wind'].split(' ')
    windspeed=int(wind[0])
    return windspeed
games['Wind Speed']=games.apply(lambda row:getwind(row), axis=1)

games.info()

games=games.drop(columns=['Temperature','Rain','Wind','Stadium URL','Pool Stage'])

savedfile=games.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Feature Creation2b.csv',index=False)
