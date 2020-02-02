import pandas as pd

epcr=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Last 3 Meetings/EPCR API.csv', encoding='latin-1')
p14=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Last 3 Meetings/P14 API.csv', encoding='latin-1')
chal=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Match Report APIs/Last 3 Meetings/Chal API.csv', encoding='latin-1')

p14=list(p14['0'])
epcr=list(epcr['0'])
chal=list(chal['0'])


############################################################################### 