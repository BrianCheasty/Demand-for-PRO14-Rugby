import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs

p14_main_content=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Main Content/P14 Main Content.csv',encoding='latin-1')
epcr_main_content=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Main Content/EPCR Main Content.csv',encoding='latin-1')
chal_main_content=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Main Content/CHAL Main Content.csv',encoding='latin-1')

p14_current_standing=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Current Standing Content/P14 Current Standing.csv', encoding='latin-1')
epcr_current_standing=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Current Standing Content/EPCR Current Standing.csv', encoding='latin-1')
chal_current_standing=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Current Standing Content/Chal Current Standing.csv', encoding='latin-1')

p14_ssf=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Season So Far Content/P14 Season So Far.csv', encoding='latin-1')
epcr_ssf=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Season So Far Content/EPCR Season So Far.csv', encoding='latin-1')
chal_ssf=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Season So Far Content/Chal Season So Far.csv', encoding='latin-1')

p14_h2h=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Head to Head Content/P14 Head to Head.csv', encoding='latin-1')
epcr_h2h=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Head to Head Content/EPCR Head to Head.csv', encoding='latin-1')
chal_h2h=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Head to Head Content/Chal Head to Head.csv', encoding='latin-1')


p14A=pd.merge(p14_main_content,p14_current_standing,left_index=True, right_index=True)
p14B=pd.merge(p14_ssf,p14_h2h,left_index=True, right_index=True)
p14=pd.merge(p14A,p14B,left_index=True, right_index=True)
epcrA=pd.merge(epcr_main_content,epcr_current_standing,left_index=True, right_index=True)
epcrB=pd.merge(epcr_ssf,epcr_h2h,left_index=True, right_index=True)
epcr=pd.merge(epcrA,epcrB,left_index=True, right_index=True)
chalA=pd.merge(chal_main_content,chal_current_standing,left_index=True, right_index=True)
chalB=pd.merge(chal_ssf,chal_h2h,left_index=True, right_index=True)
chal=pd.merge(chalA,chalB,left_index=True, right_index=True)

allgames=p14.append([epcr,chal])
savedfile=allgames.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Reports Content/Combined Content/Fixtures and Results.csv', index=False)












   