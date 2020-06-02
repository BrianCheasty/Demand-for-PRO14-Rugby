import pandas as pd

"""
Initial Results before Feature Selection
"""
savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/'
dfA1=pd.read_csv(savepath+'Attendance Regression Model/Attendance Regression.csv',encoding='latin-1')
dfA2=pd.read_csv(savepath+'Attendance (log)Regression Model/(log)Attendance Regression.csv',encoding='latin-1')
dfA3=pd.read_csv(savepath+'Stadium Percentage Regression Model/Stadium Percentage Regression.csv',encoding='latin-1')
dfA4=pd.read_csv(savepath+'Attendance Random Forest Model/Attendance Random Forest.csv',encoding='latin-1')
dfA5=pd.read_csv(savepath+'(log)Attendance Random Forest Model/(log)Attendance Random Forest.csv',encoding='latin-1')
dfA6=pd.read_csv(savepath+'Stadium Percentage Random Forest Model/Stadium Percentage Random Forest.csv',encoding='latin-1')
dfA7=pd.concat([dfA1,dfA4,dfA2,dfA5,dfA3,dfA6])
dfA7=dfA7.reset_index(drop=True)
description=pd.DataFrame(['Regression - Attendance','Random Forest - Attendance',\
              'Regression - (log)Attendance','Random Forest - (log)Attendance',\
                  'Regression - Stadium Percentage','Random Forest - Stadium Percentage'])
description=description.rename(columns={0:'Description'})
initResults=description.join(dfA7, how='outer')
columns=['RMSE Train','R2 Train','Mape Train']
for i in columns:
    initResults[i]=round(initResults[i],2)
initResults=initResults.round(decimals=2)
savedfile=initResults.to_html(savepath+'Combined Initial Results.html',index=False)   

"""
Initial Results broken down by each team
"""
savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/'
dfB1=pd.read_csv(savepath+'Attendance Regression Model/Attendance RegressionMAPE.csv',encoding='latin-1')
dfB1=dfB1.rename(columns={'Unnamed: 0':'Home_Team'})
dfB1=dfB1.set_index('Home_Team')
dfB2=pd.read_csv(savepath+'Attendance (log)Regression Model/(log)Attendance RegressionMAPE.csv',encoding='latin-1')
dfB2=dfB2.rename(columns={'Unnamed: 0':'Home_Team'})
dfB2=dfB2.set_index('Home_Team')
dfB3=pd.read_csv(savepath+'Stadium Percentage Regression Model/Stadium Percentage RegressionMAPE.csv',encoding='latin-1')
dfB3=dfB3.rename(columns={'Unnamed: 0':'Home_Team'})
dfB3=dfB3.set_index('Home_Team')
dfB4=pd.read_csv(savepath+'Attendance Random Forest Model/Attendance Random ForestMAPE.csv',encoding='latin-1')
dfB4=dfB4.rename(columns={'Unnamed: 0':'Home_Team'})
dfB4=dfB4.set_index('Home_Team')
dfB5=pd.read_csv(savepath+'(log)Attendance Random Forest Model/(log)Attendance Random ForestMAPE.csv',encoding='latin-1')
dfB5=dfB5.rename(columns={'Unnamed: 0':'Home_Team'})
dfB5=dfB5.set_index('Home_Team')
dfB6=pd.read_csv(savepath+'Stadium Percentage Random Forest Model/Stadium Percentage Random ForestMAPE.csv',encoding='latin-1')
dfB6=dfB6.rename(columns={'Unnamed: 0':'Home_Team'})
dfB6=dfB6.set_index('Home_Team')
dfB7=dfB1.join([dfB4,dfB2,dfB5,dfB3,dfB6])
dfB7=dfB7.reset_index()
dfB7=dfB7.round(decimals=2)
savedfBile=dfB7.to_html(savepath+'Results by Team.html',index=False) 


"""
Review of Residual Outliers
"""
dfC1=pd.read_csv(savepath+'Attendance Regression Model/highMAPE1.csv',encoding='latin-1')
dfC2=pd.read_csv(savepath+'Attendance (log)Regression Model/highMAPE2.csv',encoding='latin-1')
dfC3=pd.read_csv(savepath+'Stadium Percentage Regression Model/highMAPE3.csv',encoding='latin-1')
dfC4=pd.read_csv(savepath+'Attendance Random Forest Model/highMAPE4.csv',encoding='latin-1')
dfC5=pd.read_csv(savepath+'(log)Attendance Random Forest Model/highMAPE5.csv',encoding='latin-1')
dfC6=pd.read_csv(savepath+'Stadium Percentage Random Forest Model/highMAPE6.csv',encoding='latin-1')
dfC7=dfC1.append([dfC2,dfC3,dfC4,dfC5,dfC6])
dfC7=dfC7.append(dfC7.sum(),ignore_index=True)
dfC8=dfC7[(dfC7['Home_Team_Connacht Rugby']==1)]
dfC8=dfC8.append(dfC8.sum(),ignore_index=True)
dfC9=dfC7[(dfC7['Home_Team_Cardiff Blues']==1)]
dfC9=dfC9.append(dfC9.sum(),ignore_index=True)
dfC10=dfC7[(dfC7['Home_Team_Ospreys']==1)]
dfC10=dfC10.append(dfC10.sum(),ignore_index=True)

"""
Train Test Split results
"""
dfD1=pd.read_csv(savepath+'Attendance Regression Model/Attendance TrainTestSplit.csv',encoding='latin-1')
dfD2=pd.read_csv(savepath+'Attendance (log)Regression Model/(log)Attendance TrainTestSplit.csv',encoding='latin-1')
dfD3=pd.read_csv(savepath+'Stadium Percentage Regression Model/Stadium_Percentage TrainTestSplit.csv',encoding='latin-1')
dfD4=dfD1.append([dfD2,dfD3])
dfD4=dfD4.rename(columns={'0':'DataSet','1':'Percent Split','2':'Train Mean','3':'Test Mean','4':'Train Std','5':'Test Std','Mean':'Difference Mean','std':'Difference Std'})
dfD4=dfD4.round(decimals=2)
savedfDile=dfD4.to_html(savepath+'TrainTestSplit.html',index=False) 

"""
Multicolinearity results
"""
dfE1=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif1.csv',encoding='latin-1')
dfE2=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif2.csv',encoding='latin-1')
vif1=dfE1.append(dfE2)
dfE3=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif3.csv',encoding='latin-1')
dfE4=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif4.csv',encoding='latin-1')
vif2=dfE3.append(dfE4)
dfE5=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif5.csv',encoding='latin-1')
dfE6=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif6.csv',encoding='latin-1')
vif3=dfE5.append(dfE6)
dfE7=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif7.csv',encoding='latin-1')
dfE8=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif8.csv',encoding='latin-1')
vif4=dfE7.append(dfE8)
dfE9=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif9.csv',encoding='latin-1')
dfE10=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif10.csv',encoding='latin-1')
vif5=dfE9.append(dfE10)
dfE11=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif11.csv',encoding='latin-1')
dfE12=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/vif12.csv',encoding='latin-1')
vif6=dfE11.append(dfE12)
vifa=vif1.merge(vif2)
vifb=vifa.merge(vif3)
vifc=vifb.merge(vif4)
vifd=vifc.merge(vif5)
vife=vifd.merge(vif6)
savedfEile=vife.to_html(savepath+'VIF on Training.html',index=False) 

"""
RFE Feature Ranking
"""
dfF1=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Attendance Regression Model/Regression Attendance Feature Selection Rankings.csv',encoding='latin-1')
dfF1=dfF1.sort_values(by='Ranking')
dfF1=dfF1.rename(columns={'Features':'Attendance Regression'})
dfF2=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Attendance (log)Regression Model/(log)Regression Feature Selection Rankings.csv',encoding='latin-1')
dfF2=dfF2.sort_values(by='Ranking')
dfF2=dfF2.rename(columns={'Features':'(log)Attendance Regression'})
dfF3=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Stadium Percentage Regression Model/Regression Stadium Percentage Feature Selection Rankings.csv',encoding='latin-1')
dfF3=dfF3.sort_values(by='Ranking')
dfF3=dfF3.rename(columns={'Features':'Stadium Percentage Regression'})
dfF4=dfF1.merge(dfF2,how='outer')
dfF5=dfF4.merge(dfF3,how='outer')
savedfFile=dfF5.to_html(savepath+'Feature Rankings.html',index=False) 

savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/'
allFeat=pd.read_csv(savepath+'All Features.csv', encoding='latin-1')
allFeat=pd.merge(allFeat,dfF1,left_on='0',right_on='Attendance Regression',how='left')
allFeat=pd.merge(allFeat,dfF2,left_on='0',right_on='(log)Attendance Regression',how='left')
allFeat=pd.merge(allFeat,dfF3,left_on='0',right_on='Stadium Percentage Regression',how='left')
allFeat=allFeat.drop(columns=['Ranking_x','Ranking_y','Ranking'])

"""
Model Selection 
"""
savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/'
dfE1=pd.read_csv(savepath+'Attendance Random Forest Model/modelselect1.csv', encoding='latin-1')
dfE1=dfE1.rename(columns={'Attendance':'Attendance RFR'})
dfE2=pd.read_csv(savepath+'(log)Attendance Random Forest Model/modelselect2.csv', encoding='latin-1')
dfE2=dfE2.rename(columns={'Attendance':'(log)Attendance RFR'})
dfE3=pd.read_csv(savepath+'Stadium Percentage Random Forest Model/modelselect3.csv', encoding='latin-1')
dfE3=dfE3.rename(columns={'Attendance':'Stadium Percentage RFR'})

allFeat=pd.merge(allFeat,dfE1,left_on='0',right_on='Attendance RFR',how='left')
allFeat=pd.merge(allFeat,dfE2,left_on='0',right_on='(log)Attendance RFR',how='left')
allFeat=pd.merge(allFeat,dfE3,left_on='0',right_on='Stadium Percentage RFR',how='left')

"""
pvalue Feature Ranking
"""
dfF1=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Stadium Percentage Regression Model/Regression Stadium Percentage pvalue.csv',encoding='latin-1')
dfF1=dfF1.rename(columns={'0':'Stadium Percentage MLR COE'})
dfF1=dfF1.reset_index()

dfF2=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Attendance (log)Regression Model/Regression (log)Attendance pvalue.csv',encoding='latin-1')
dfF2=dfF2.rename(columns={'0':'(log)Attendance MLR COE'})
dfF2=dfF2.reset_index()

dfF3=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Attendance Regression Model/Regression Attendance pvalue.csv',encoding='latin-1')
dfF3=dfF3.rename(columns={'0':'Attendance MLR COE'})
dfF3=dfF3.reset_index()

dfF4=dfF3.merge(dfF2,how='outer')
dfF5=dfF4.merge(dfF1,how='outer')
dfF5=dfF5.drop(columns=['index'])
savedfFile=dfF5.to_html(savepath+'Feature Rankings OLS.html',index=False) 

allFeat=pd.merge(allFeat,dfF3,left_on='0',right_on='Attendance MLR COE',how='left')
allFeat=pd.merge(allFeat,dfF2,left_on='0',right_on='(log)Attendance MLR COE',how='left')
allFeat=pd.merge(allFeat,dfF1,left_on='0',right_on='Stadium Percentage MLR COE',how='left')
allFeat=allFeat.drop(columns=['index_x','index_y','index'])

"""
Shapiro Wilks results
"""
dfG1=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue1.csv',encoding='latin-1')
dfG2=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue2.csv',encoding='latin-1')
dfG3=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue3.csv',encoding='latin-1')
dfG4=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue4.csv',encoding='latin-1')
dfG5=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue5.csv',encoding='latin-1')
dfG6=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue6.csv',encoding='latin-1')
dfG7=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue7.csv',encoding='latin-1')
dfG8=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue8.csv',encoding='latin-1')
dfG9=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/pvalue9.csv',encoding='latin-1')
dfG10=dfG1.append([dfG2,dfG3,dfG4,dfG5,dfG6,dfG9,dfG8,dfG7])
savedfGile=dfG10.to_html(savepath+'Shapiro Wilks.html',index=False) 

"""
Breuschpagan test
"""
dfH1=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp1.csv',encoding='latin-1')
dfH2=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp2.csv',encoding='latin-1')
dfH3=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp3.csv',encoding='latin-1')
dfH4=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp4.csv',encoding='latin-1')
dfH5=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp5.csv',encoding='latin-1')
dfH6=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp6.csv',encoding='latin-1')
dfH7=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp7.csv',encoding='latin-1')
dfH8=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp8.csv',encoding='latin-1')
dfH9=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/bp9.csv',encoding='latin-1')
dfH10=dfH1.append([dfH2,dfH3,dfH4,dfH5,dfH6,dfH9,dfH8,dfH7])
savedfHile=dfH10.to_html(savepath+'Breuschpagan test.html',index=False) 

"""
Final Results
"""
savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/'
dfI1=pd.read_csv(savepath+'Attendance Regression Model/Attendance Regression Test.csv',encoding='latin-1')
dfI2=pd.read_csv(savepath+'Attendance (log)Regression Model/(log)Attendance Regression Test.csv',encoding='latin-1')
dfI3=pd.read_csv(savepath+'Stadium Percentage Regression Model/Stadium Percentage Regression Test.csv',encoding='latin-1')
dfI4=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Attendance Random Forest Model/Attendance Random Forest Test.csv',encoding='latin-1')
dfI5=pd.read_csv(savepath+'(log)Attendance Random Forest Model/(log)Attendance Random Forest Test.csv',encoding='latin-1')
dfI6=pd.read_csv(savepath+'Stadium Percentage Random Forest Model/Stadium Percentage Random Forest Test.csv',encoding='latin-1')
dfI7=pd.read_csv(savepath+'Attendance Regression Model/Attendance Regression Test pvalue.csv',encoding='latin-1')
dfI8=pd.read_csv(savepath+'Attendance (log)Regression Model/(log)Attendance Regression Test pvalue.csv',encoding='latin-1')
dfI9=pd.read_csv(savepath+'Stadium Percentage Regression Model/Stadium Percentage Regression Test pvalue.csv',encoding='latin-1')

dfI7=pd.concat([dfI1,dfI4,dfI7,dfI2,dfI5,dfI8,dfI3,dfI6,dfI9])
dfI7=dfI7.round(decimals=2)
dfI7=dfI7.sort_values(by='Mape Test')
savedfIile=dfI7.to_html(savepath+'Combined Final Test Results.html',index=False)


"""
Combined Features Selected
"""

cat=['Tournament','Home_Team','Away_Team','Venue','Away_Country','Round','Win_Probability','Win_Probability_Squared','Win_Probability_Dummy',\
     'Round_Significance','Table_Difference','Game_Competitiveness','Yrs_P14_Win','Yrs_EPCR_Win','No._P14_Wins',\
         'No._EPCR_Wins','HvsA_Winning_Percentage','Home_Table_Position','Away_Table_Position','Home_Lst_5_Win','Away_Lst_5_Win','Home_Lst_3_Win',\
             'Home_Lst_5_in_Comp','Away_Lst_5_in_Comp','Derby','Home_Winning_Percentage','Medium_Term_Uncertainty','Days_Since_Last_Game',\
                 'Days_Since_Lst_Game_Dummy','Lst_Game_in_Comp','Lst_Game_in_Comp_Dummy','Day_of_Week','Month_of_Year','Kick_off_Hour','Sentiment',\
                     'Temperature','Rain','Wind','Temp_Dummy','Wind_Dummy','Rain_Dummy','Stadium_Age_Dummy','Stadium_Age']
import numpy as np
allFeat2=[]
for i in cat:
    df=allFeat[(allFeat['0'].str.contains(i))]
    df=df.append(df.count(),ignore_index=True)
    columns=df.columns
    for j in columns:
        df[j]=df[j].astype(str)
        df[j]=df[j].replace(r'0',np.nan,regex=True)
    df['Count']=df.count(axis='columns')
    df['0']=df['0'].astype(str)
    df=df[(~df['0'].str.contains(i))]
    num=df['Count'].max()
    numb=num-1
    x={i:numb}
    x=pd.DataFrame.from_dict(x, orient='index')
    allFeat2.append(x)

allFeat3=pd.concat(allFeat2)
allFeat3=allFeat3.rename(columns={0:'Quantity'})
allFeat3=allFeat3.reset_index()
allFeat3=allFeat3.rename(columns={'index':'Features'})
allFeat3.loc[(allFeat3['Features'].str.contains('Tournament|Home_Team|Away_Team|Venue|Munster_Euro|Away_Country|Round')),'Category']='Match Details'
allFeat3.loc[(allFeat3['Features'].str.contains('Win_Probability|Win_Probability_Squared|Win_Probability_Dummy|Round_Significance|Table_Difference')),'Category']='Match Level Uncertainty of Outcome'
allFeat3.loc[(allFeat3['Features'].str.contains('Game_Competitiveness|Yrs_P14_Win|Yrs_EPCR_Win')),'Category']='Season Level Uncertanty of Outcome'
allFeat3.loc[(allFeat3['Features'].str.contains('No._P14_Wins|No._EPCR_Wins|HvsA_Winning_Percentage')),'Category']='Long Run Uncertainty of Outcome'
allFeat3.loc[(allFeat3['Features'].str.contains('Home_Table_Position|Away_Table_Position|Home_Lst_5_Win|Away_Lst_5_Win|Home_Lst_3_Win|Home_Lst_5_in_Comp|Away_Lst_5_in_Comp')),'Category']='Team Quality'
allFeat3.loc[(allFeat3['Features'].str.contains('Derby|Home_Winning_Percentage|Medium_Term_Uncertainty')),'Category']='Contest Quality'
allFeat3.loc[(allFeat3['Features'].str.contains('Days_Since_Last_Game|Days_Since_Lst_Game_Dummy|Lst_Game_in_Comp|Lst_Game_in_Comp_Dummy|Day_of_Week|Month_of_Year|Kick_off_Hour|Sentiment')),'Category']='Economic Theory'
allFeat3.loc[(allFeat3['Features'].str.contains('Temperature|Rain|Wind|Temp_Dummy|Wind_Dummy|Rain_Dummy|Stadium_Age_Dummy|Stadium_Age')),'Category']='Quality of Viewing'
allFeat3=allFeat3[['Category','Features','Quantity']]
savedfIile=allFeat3.to_html(savepath+'Categories Used.html',index=False)


allFeat['Count']=allFeat.count(axis='columns')
allFeat.loc[(allFeat['0'].str.contains('Tournament|Home_Team|Away_Team|Venue|Munster_Euro|Away_Country|Round')),'Category']='Match Details'
allFeat.loc[(allFeat['0'].str.contains('Win_Probability|Win_Probability_Squared|Win_Probability_Dummy|Round_Significance|Table_Difference')),'Category']='Match Level Uncertainty of Outcome'
allFeat.loc[(allFeat['0'].str.contains('Game_Competitiveness|Yrs_P14_Win|Yrs_EPCR_Win')),'Category']='Season Level Uncertanty of Outcome'
allFeat.loc[(allFeat['0'].str.contains('No._P14_Wins|No._EPCR_Wins|HvsA_Winning_Percentage')),'Category']='Long Run Uncertainty of Outcome'
allFeat.loc[(allFeat['0'].str.contains('Home_Table_Position|Away_Table_Position|Home_Lst_5_Win|Away_Lst_5_Win|Home_Lst_3_Win|Home_Lst_5_in_Comp|Away_Lst_5_in_Comp')),'Category']='Team Quality'
allFeat.loc[(allFeat['0'].str.contains('Derby|Home_Winning_Percentage|Medium_Term_Uncertainty')),'Category']='Contest Quality'
allFeat.loc[(allFeat['0'].str.contains('Days_Since_Last_Game|Days_Since_Lst_Game_Dummy|Lst_Game_in_Comp|Lst_Game_in_Comp_Dummy|Day_of_Week|Month_of_Year|Kick_off_Hour|Sentiment')),'Category']='Economic Theory'
allFeat.loc[(allFeat['0'].str.contains('Temperature|Rain|Wind|Temp_Dummy|Wind_Dummy|Rain_Dummy|Stadium_Age_Dummy|Stadium_Age')),'Category']='Quality of Viewing'

   
allFeat=allFeat.drop(columns=['0'])
allFeat=allFeat.dropna(subset=['Attendance Regression','(log)Attendance Regression','Stadium Percentage Regression',\
                            'Attendance RFR','(log)Attendance RFR','Stadium Percentage RFR',\
                                'Attendance MLR COE','(log)Attendance MLR COE','Stadium Percentage MLR COE'],how='all')
allFeat=allFeat.sort_values(by='Category')
allFeat=allFeat[['Category','Count','Attendance Regression','(log)Attendance Regression','Stadium Percentage Regression',\
                            'Attendance RFR','(log)Attendance RFR','Stadium Percentage RFR',\
                                'Attendance MLR COE','(log)Attendance MLR COE','Stadium Percentage MLR COE']]
allFeat['Count']=allFeat['Count']-1
savedfIile=allFeat.to_html(savepath+'Features Used.html',index=False)
