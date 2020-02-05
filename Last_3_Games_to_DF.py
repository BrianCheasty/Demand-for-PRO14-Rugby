import pandas as pd
import json
from bs4 import BeautifulSoup as bs
import numpy as np

p14=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/P14 API full.csv', encoding='latin-1')
epcr=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/epcr API full.csv', encoding='latin-1')
chal=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/chal API full.csv', encoding='latin-1')

p14=list(p14['4'])
epcr=list(epcr['4'])
chal=list(chal['4'])


###############################################################################  