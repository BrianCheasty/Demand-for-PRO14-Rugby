import pandas as pd

df=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Data for Model.csv', encoding='latin-1')
df.info()
df.loc[(df['Venue'].str.contains('Comunale di Monigo')),'Venue']='Venue_Stadio Monigo'
df.loc[(df['Venue'].str.contains('Murrayfield')),'Venue']='Venue_BT Murrayfield'
df['Win Prob Squared']=((df['Win Probability']-.5)*100)**2
df2=pd.get_dummies(df)
df2.info()

savedfile=df2.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Final Data for Model.csv', index=False)

df3=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Data for Model2.csv', encoding='latin-1')
#df.info()

df4=pd.get_dummies(df3,drop_first=True)



savedfile=df4.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Final Data for Model2.csv', index=False)

