import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn') # pretty matplotlib plots
plt.rc('font', size=14)
plt.rc('figure', titlesize=18)
plt.rc('axes', labelsize=15)
plt.rc('axes', titlesize=18)

attend=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Attendance DataA.csv', encoding='latin-1')
attend.info()
df=pd.get_dummies(attend)



df=df[['Win_Probability','Round','Win_Probability_Squared','Round_Significance','Table_Difference','No._P14_Wins','No._EPCR_Wins','HvsA_Winning_Percentage','Home_Table_Position',\
       'Away_Table_Position','Home_Lst_5_Win','Away_Lst_5_Win','Home_Lst_3_Win','Home_Lst_5_in_Comp','Away_Lst_5_in_Comp','Home_Winning_Percentage',\
           'Medium_Term_Uncertainty','Days_Since_Last_Game','Lst_Game_in_Comp','Sentiment_Under 105','Sentiment_Under 110','Sentiment_Under 115','Temperature','Rain','Wind','Stadium_Age','Tournament_Champions Cup',\
               'Tournament_League','Home_Team_Benetton Treviso','Home_Team_Cardiff Blues','Home_Team_Connacht Rugby','Home_Team_Dragons','Home_Team_Ospreys',\
                   'Home_Team_Scarlets','Home_Team_Ulster Rugby','Home_Team_Zebre Rugby','Away_Team_Benetton Treviso','Away_Team_Cardiff Blues',\
                       'Away_Team_Connacht Rugby','Away_Team_Dragons','Away_Team_Edinburgh Rugby','Away_Team_Glasgow Warriors','Away_Team_Leinster Rugby',\
                           'Away_Team_Munster Rugby','Away_Team_Ospreys','Away_Team_Scarlets','Away_Team_Ulster Rugby','Away_Team_Zebre Rugby',\
                               'Venue_Aviva Stadium','Venue_BT Murrayfield','Venue_Irish Independent Park','Venue_Myreside','Venue_RDS Arena',\
                                   'Venue_Thomond Park','Away_Country_Ireland','Away_Country_Italy','Away_Country_Scotland','Away_Country_Wales',\
                                       'Win_Probability_Dummy_Even','Game_Competitiveness_Cant Qualify','Game_Competitiveness_Has Qualified','Yrs_P14_Win_Four to Six',\
                                           'Yrs_P14_Win_Greater than Six','Yrs_P14_Win_Within Three','Yrs_EPCR_Win_Four to Six','Yrs_EPCR_Win_Greater than Six',\
                                               'Yrs_EPCR_Win_Within Three','Derby_Extra Derby','Derby_Non Derby','Days_Since_Lst_Game_Dummy_Within Two Weeks','Days_Since_Lst_Game_Dummy_Within Month',\
                                                   'Lst_Game_in_Comp_Dummy_Within Month','Lst_Game_in_Comp_Dummy_Within Two Weeks','Day_of_Week_Friday','Day_of_Week_Saturday','Month_of_Year_First Q',\
                                                       'Month_of_Year_Second Q','Month_of_Year_Third Q','Kick_off_Hour_Early','Kick_off_Hour_Evening','Temp_Dummy_Mild',\
                                                           'Temp_Dummy_Warm','Wind_Dummy_Normal','Wind_Dummy_Wild','Rain_Dummy_Dry','Rain_Dummy_Wet',\
                                                               'Stadium_Age_Dummy_New','Stadium_Age_Dummy_Old','Venue_Stadio Monigo','Venue_The Sportsground',\
                                                                   'Venue_Rodney Parade','Venue_Liberty Stadium','Venue_Parc y Scarlets','Venue_Kingspan Stadium',\
                                                                       'Venue_Stadio Sergio Lanfranchi','Venue_Cardiff Arms Park','Away_Team_NotPRO14',\
                                                                           'Tournament_Challenge Cup','Home_Team_Edinburgh Rugby','Home_Team_Leinster Rugby',\
                                                                               'Home_Team_Munster Rugby','Away_Country_EngFra','Win_Probability_Dummy_Uneven',\
                                                                                   'Game_Competitiveness_Can Still Qualify','Yrs_P14_Win_Never','Yrs_EPCR_Win_Never',\
                                                                                       'Derby_Derby','Days_Since_Lst_Game_Dummy_Over a Month',\
                                                                                           'Lst_Game_in_Comp_Dummy_Over a Month','Day_of_Week_Non Trad Day',\
                                                                                               'Month_of_Year_Fourth Q','Kick_off_Hour_Afternoon','Temp_Dummy_Cold',\
                                                                                                   'Wind_Dummy_Calm','Rain_Dummy_Damp','Stadium_Age_Dummy_Middle Age',\
                                                                                                       'Attendance']]
 
df=df.drop(columns=['Sentiment_Under 105','Temperature','Rain','Wind','Days_Since_Last_Game','Lst_Game_in_Comp','Venue_Stadio Monigo','Venue_The Sportsground','Venue_Rodney Parade','Venue_Liberty Stadium','Venue_Parc y Scarlets','Venue_Kingspan Stadium',\
                    'Venue_Stadio Sergio Lanfranchi','Venue_Cardiff Arms Park','Away_Team_NotPRO14','Tournament_Challenge Cup','Home_Team_Edinburgh Rugby','Home_Team_Leinster Rugby','Home_Team_Munster Rugby','Away_Country_EngFra','Win_Probability_Dummy_Uneven','Game_Competitiveness_Can Still Qualify',\
                        'Yrs_P14_Win_Never','Yrs_EPCR_Win_Never','Derby_Derby','Days_Since_Lst_Game_Dummy_Over a Month','Lst_Game_in_Comp_Dummy_Over a Month','Day_of_Week_Non Trad Day','Month_of_Year_Fourth Q','Kick_off_Hour_Afternoon','Temp_Dummy_Cold','Wind_Dummy_Calm','Rain_Dummy_Damp','Stadium_Age_Dummy_Middle Age'])
  
savedfile=df.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Attendance Data.csv', index=False)

logattend=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/logAttendance DataA.csv', encoding='latin-1')
df2=pd.get_dummies(logattend)
df2=df2[['Win_Probability','Round','Win_Probability_Squared','Round_Significance','Table_Difference','No._P14_Wins','No._EPCR_Wins','HvsA_Winning_Percentage','Home_Table_Position',\
         'Away_Table_Position','Home_Lst_5_Win','Away_Lst_5_Win','Home_Lst_3_Win','Home_Lst_5_in_Comp','Away_Lst_5_in_Comp','Home_Winning_Percentage',\
             'Medium_Term_Uncertainty','Days_Since_Last_Game','Lst_Game_in_Comp','Sentiment_Under 105','Sentiment_Under 110','Sentiment_Under 115','Temperature','Rain','Wind','Stadium_Age','Tournament_Champions Cup',\
                 'Tournament_League','Home_Team_Benetton Treviso','Home_Team_Cardiff Blues','Home_Team_Connacht Rugby','Home_Team_Dragons','Home_Team_Ospreys',\
                     'Home_Team_Scarlets','Home_Team_Ulster Rugby','Home_Team_Zebre Rugby','Away_Team_Benetton Treviso','Away_Team_Cardiff Blues',\
                         'Away_Team_Connacht Rugby','Away_Team_Dragons','Away_Team_Edinburgh Rugby','Away_Team_Glasgow Warriors','Away_Team_Leinster Rugby',\
                             'Away_Team_Munster Rugby','Away_Team_Ospreys','Away_Team_Scarlets','Away_Team_Ulster Rugby','Away_Team_Zebre Rugby',\
                                 'Venue_BT Murrayfield','Venue_Irish Independent Park','Venue_Myreside','Venue_RDS Arena',\
                                     'Venue_Aviva Stadium','Venue_Thomond Park','Away_Country_Ireland','Away_Country_Italy','Away_Country_Scotland','Away_Country_Wales',\
                                         'Win_Probability_Dummy_Even','Game_Competitiveness_Cant Qualify','Game_Competitiveness_Has Qualified','Yrs_P14_Win_Four to Six',\
                                             'Yrs_P14_Win_Greater than Six','Yrs_P14_Win_Within Three','Yrs_EPCR_Win_Four to Six','Yrs_EPCR_Win_Greater than Six',\
                                                 'Yrs_EPCR_Win_Within Three','Derby_Extra Derby','Derby_Non Derby','Days_Since_Lst_Game_Dummy_Within Two Weeks','Days_Since_Lst_Game_Dummy_Within Month',\
                                                     'Lst_Game_in_Comp_Dummy_Within Month','Lst_Game_in_Comp_Dummy_Within Two Weeks','Day_of_Week_Friday','Day_of_Week_Saturday','Month_of_Year_First Q',\
                                                         'Month_of_Year_Second Q','Month_of_Year_Third Q','Kick_off_Hour_Early','Kick_off_Hour_Evening','Temp_Dummy_Mild',\
                                                             'Temp_Dummy_Warm','Wind_Dummy_Normal','Wind_Dummy_Wild','Rain_Dummy_Dry','Rain_Dummy_Wet',\
                                                                 'Stadium_Age_Dummy_New','Stadium_Age_Dummy_Old','Venue_Stadio Monigo','Venue_The Sportsground',\
                                                                     'Venue_Rodney Parade','Venue_Liberty Stadium','Venue_Parc y Scarlets','Venue_Kingspan Stadium',\
                                                                         'Venue_Stadio Sergio Lanfranchi','Venue_Cardiff Arms Park','Away_Team_NotPRO14',\
                                                                             'Tournament_Challenge Cup','Home_Team_Edinburgh Rugby','Home_Team_Leinster Rugby',\
                                                                                 'Home_Team_Munster Rugby','Away_Country_EngFra','Win_Probability_Dummy_Uneven',\
                                                                                     'Game_Competitiveness_Can Still Qualify','Yrs_P14_Win_Never','Yrs_EPCR_Win_Never',\
                                                                                         'Derby_Derby','Days_Since_Lst_Game_Dummy_Over a Month',\
                                                                                             'Lst_Game_in_Comp_Dummy_Over a Month','Day_of_Week_Non Trad Day',\
                                                                                                 'Month_of_Year_Fourth Q','Kick_off_Hour_Afternoon','Temp_Dummy_Cold',\
                                                                                                     'Wind_Dummy_Calm','Rain_Dummy_Damp','Stadium_Age_Dummy_Middle Age',\
                                                                                                         '(log)Attendance']]
df2=df2.drop(columns=['Sentiment_Under 105','Temperature','Rain','Wind','Days_Since_Last_Game','Lst_Game_in_Comp','Venue_Stadio Monigo','Venue_The Sportsground','Venue_Rodney Parade','Venue_Liberty Stadium','Venue_Parc y Scarlets','Venue_Kingspan Stadium',\
                      'Venue_Stadio Sergio Lanfranchi','Venue_Cardiff Arms Park','Away_Team_NotPRO14','Tournament_Challenge Cup','Home_Team_Edinburgh Rugby','Home_Team_Leinster Rugby','Home_Team_Munster Rugby','Away_Country_EngFra','Win_Probability_Dummy_Uneven','Game_Competitiveness_Can Still Qualify',\
                          'Yrs_P14_Win_Never','Yrs_EPCR_Win_Never','Derby_Derby','Days_Since_Lst_Game_Dummy_Over a Month','Lst_Game_in_Comp_Dummy_Over a Month','Day_of_Week_Non Trad Day','Month_of_Year_Fourth Q','Kick_off_Hour_Afternoon','Temp_Dummy_Cold','Wind_Dummy_Calm','Rain_Dummy_Damp','Stadium_Age_Dummy_Middle Age'])

  
savedfile=df2.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/(log)Attendance Data.csv', index=False)

spattend=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Stadium Percentage DataA.csv', encoding='latin-1')
df3=pd.get_dummies(spattend)
df3=df3[['Win_Probability','Round','Win_Probability_Squared','Round_Significance','Table_Difference','No._P14_Wins','No._EPCR_Wins','HvsA_Winning_Percentage','Home_Table_Position',\
         'Away_Table_Position','Home_Lst_5_Win','Away_Lst_5_Win','Home_Lst_3_Win','Home_Lst_5_in_Comp','Away_Lst_5_in_Comp','Home_Winning_Percentage',\
             'Medium_Term_Uncertainty','Days_Since_Last_Game','Lst_Game_in_Comp','Sentiment_Under 105','Sentiment_Under 110','Sentiment_Under 115','Temperature','Rain','Wind','Stadium_Age','Tournament_Champions Cup',\
                 'Tournament_League','Home_Team_Benetton Treviso','Home_Team_Cardiff Blues','Home_Team_Connacht Rugby','Home_Team_Dragons','Home_Team_Ospreys',\
                     'Home_Team_Scarlets','Home_Team_Ulster Rugby','Home_Team_Zebre Rugby','Away_Team_Benetton Treviso','Away_Team_Cardiff Blues',\
                         'Away_Team_Connacht Rugby','Away_Team_Dragons','Away_Team_Edinburgh Rugby','Away_Team_Glasgow Warriors','Away_Team_Leinster Rugby',\
                             'Away_Team_Munster Rugby','Away_Team_Ospreys','Away_Team_Scarlets','Away_Team_Ulster Rugby','Away_Team_Zebre Rugby',\
                                 'Venue_BT Murrayfield','Venue_Irish Independent Park','Venue_Myreside','Venue_RDS Arena',\
                                     'Venue_Aviva Stadium','Venue_Thomond Park','Away_Country_Ireland','Away_Country_Italy','Away_Country_Scotland','Away_Country_Wales',\
                                         'Win_Probability_Dummy_Even','Game_Competitiveness_Cant Qualify','Game_Competitiveness_Has Qualified','Yrs_P14_Win_Four to Six',\
                                             'Yrs_P14_Win_Greater than Six','Yrs_P14_Win_Within Three','Yrs_EPCR_Win_Four to Six','Yrs_EPCR_Win_Greater than Six',\
                                                 'Yrs_EPCR_Win_Within Three','Derby_Extra Derby','Derby_Non Derby','Days_Since_Lst_Game_Dummy_Within Two Weeks','Days_Since_Lst_Game_Dummy_Within Month',\
                                                     'Lst_Game_in_Comp_Dummy_Within Month','Lst_Game_in_Comp_Dummy_Within Two Weeks','Day_of_Week_Friday','Day_of_Week_Saturday','Month_of_Year_First Q',\
                                                         'Month_of_Year_Second Q','Month_of_Year_Third Q','Kick_off_Hour_Early','Kick_off_Hour_Evening','Temp_Dummy_Mild',\
                                                             'Temp_Dummy_Warm','Wind_Dummy_Normal','Wind_Dummy_Wild','Rain_Dummy_Dry','Rain_Dummy_Wet',\
                                                                 'Stadium_Age_Dummy_New','Stadium_Age_Dummy_Old','Venue_Stadio Monigo','Venue_The Sportsground',\
                                                                     'Venue_Rodney Parade','Venue_Liberty Stadium','Venue_Parc y Scarlets','Venue_Kingspan Stadium',\
                                                                         'Venue_Stadio Sergio Lanfranchi','Venue_Cardiff Arms Park','Away_Team_NotPRO14',\
                                                                             'Tournament_Challenge Cup','Home_Team_Edinburgh Rugby','Home_Team_Leinster Rugby',\
                                                                                 'Home_Team_Munster Rugby','Away_Country_EngFra','Win_Probability_Dummy_Uneven',\
                                                                                     'Game_Competitiveness_Can Still Qualify','Yrs_P14_Win_Never','Yrs_EPCR_Win_Never',\
                                                                                         'Derby_Derby','Days_Since_Lst_Game_Dummy_Over a Month',\
                                                                                             'Lst_Game_in_Comp_Dummy_Over a Month','Day_of_Week_Non Trad Day',\
                                                                                                 'Month_of_Year_Fourth Q','Kick_off_Hour_Afternoon','Temp_Dummy_Cold',\
                                                                                                     'Wind_Dummy_Calm','Rain_Dummy_Damp','Stadium_Age_Dummy_Middle Age',\
                                                                                                         'Stadium_Percentage']]
df3=df3.drop(columns=['Sentiment_Under 105','Temperature','Rain','Wind','Days_Since_Last_Game','Lst_Game_in_Comp','Venue_Stadio Monigo','Venue_The Sportsground','Venue_Rodney Parade','Venue_Liberty Stadium','Venue_Parc y Scarlets','Venue_Kingspan Stadium',\
                      'Venue_Stadio Sergio Lanfranchi','Venue_Cardiff Arms Park','Away_Team_NotPRO14','Tournament_Challenge Cup','Home_Team_Edinburgh Rugby','Home_Team_Leinster Rugby','Home_Team_Munster Rugby','Away_Country_EngFra','Win_Probability_Dummy_Uneven','Game_Competitiveness_Can Still Qualify',\
                          'Yrs_P14_Win_Never','Yrs_EPCR_Win_Never','Derby_Derby','Days_Since_Lst_Game_Dummy_Over a Month','Lst_Game_in_Comp_Dummy_Over a Month','Day_of_Week_Non Trad Day','Month_of_Year_Fourth Q','Kick_off_Hour_Afternoon','Temp_Dummy_Cold','Wind_Dummy_Calm','Rain_Dummy_Damp','Stadium_Age_Dummy_Middle Age'])
savedfile=df3.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Stadium Percentage Data.csv', index=False)

savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/'


explore=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/For Exploration.csv', encoding='latin-1')
explore=explore.drop(columns=['Temperature','Rain','Wind','Days_Since_Last_Game','Lst_Game_in_Comp'])


stats=explore.describe()
stats2=stats.T
stats2=stats2.round(decimals=2)
#savedfile=stats2.to_html(savepath+'Descriptive Stats.html') 

stats3=stats2.reset_index()
feat=list(stats3['index'])
dependent=feat[:18]
independent=feat[18:]


plt.style.use('seaborn') # pretty matplotlib plots
plt.rc('font', size=6)
plt.rc('figure', titlesize=6)
plt.rc('axes', labelsize=8)
plt.rc('axes', titlesize=8)
indcount=0
for i in independent:
    plt.figure(figsize=(12,24))
    plt.tight_layout()
    indcount=0
    for j in dependent:
        indcount+=1
        plt.subplot(6,3,indcount)
        plt.scatter(explore[i],  explore[j],
            c='steelblue', marker='o', edgecolor='white')
        plt.xlabel(i)
        plt.ylabel(j)
    plt.show()
        
        
        

explore2=explore.T
explore2=explore2.reset_index()
explore2=explore2.rename(columns={'index':'Features'})
explore2=explore2[['Features']]

explore2.loc[(explore2['Features'].str.contains('(log)Attendance|Attendance|Stadium_Percentage')),'Category']='Target Variable'
explore2.loc[(explore2['Features'].str.contains('Tournament|Home_Team|Away_Team|Venue|Munster_Euro|Away_Country|Round')),'Category']='Match Details'
explore2.loc[(explore2['Features'].str.contains('Win_Probability|Win_Probability_Squared|Win_Probability_Dummy|Round_Significance|Table_Difference')),'Category']='Match Level Uncertainty of Outcome'
explore2.loc[(explore2['Features'].str.contains('Game_Competitiveness|Yrs_P14_Win|Yrs_EPCR_Win')),'Category']='Season Level Uncertanty of Outcome'
explore2.loc[(explore2['Features'].str.contains('No._P14_Wins|No._EPCR_Wins|HvsA_Winning_Percentage')),'Category']='Long Run Uncertainty of Outcome'
explore2.loc[(explore2['Features'].str.contains('Home_Table_Position|Away_Table_Position|Home_Lst_5_Win|Away_Lst_5_Win|Home_Lst_3_Win|Home_Lst_5_in_Comp|Away_Lst_5_in_Comp')),'Category']='Team Quality'
explore2.loc[(explore2['Features'].str.contains('Derby|Home_Winning_Percentage|Medium_Term_Uncertainty')),'Category']='Contest Quality'
explore2.loc[(explore2['Features'].str.contains('Days_Since_Last_Game|Days_Since_Lst_Game_Dummy|Lst_Game_in_Comp|Lst_Game_in_Comp_Dummy|Day_of_Week|Month_of_Year|Kick_off_Hour|Sentiment')),'Category']='Economic Theory'
explore2.loc[(explore2['Features'].str.contains('Temperature|Rain|Wind|Temp_Dummy|Wind_Dummy|Rain_Dummy|Stadium_Age_Dummy|Stadium_Age')),'Category']='Quality of Viewing'
explore2=explore2.sort_values('Category')
df=explore2[['Category','Features']]

df.loc[(df['Features']=='Tournament'),'Description']='PRO14, Champions or Challenge Cup'
df.loc[(df['Features']=='Home_Team'),'Description']='Hosting team'
df.loc[(df['Features']=='Away_Team'),'Description']='Visiting team, PRO14 Team or dummy for other'
df.loc[(df['Features']=='Venue'),'Description']='Hosting stadium'
df.loc[(df['Features']=='Munster_Euro'),'Description']='Munster European dummy'
df.loc[(df['Features']=='Away_Country'),'Description']='Home Country of visiting team'
df.loc[(df['Features']=='Win_Probability'),'Description']='Based on probability of winning from betting odds'
df.loc[(df['Features']=='Win_Probability_Squared'),'Description']='Squared win probability'
df.loc[(df['Features']=='Win_Probability_Dummy'),'Description']='Even or uneven contest'
df.loc[(df['Features']=='Round'),'Description']='Round of the competition'
df.loc[(df['Features']=='Round_Significance'),'Description']='Round multiplied by winning percentage'
df.loc[(df['Features']=='Table_Difference'),'Description']='Table distance between both teams'
df.loc[(df['Features']=='Game_Competitiveness'),'Description']='Can / Can\'t / Has Qualified'
df.loc[(df['Features']=='Yrs_P14_Win'),'Description']='Dummy, within three, four to six, six plus, never'
df.loc[(df['Features']=='Yrs_EPCR_Win'),'Description']='Dummy, within three, four to six, six plus, never'
df.loc[(df['Features']=='No._P14_Wins'),'Description']='Number of League wins'
df.loc[(df['Features']=='No._EPCR_Wins'),'Description']='Number of Cup Wins'
df.loc[(df['Features']=='HvsA_Winning_Percentage'),'Description']='% of Home to Away wins'
df.loc[(df['Features']=='Home_Table_Position'),'Description']='Current position on the table at day of game'
df.loc[(df['Features']=='Away_Table_Position'),'Description']='Current position on the table at day of game'
df.loc[(df['Features']=='Home_Lst_5_Win'),'Description']='Number of games won in the last 5'
df.loc[(df['Features']=='Away_Lst_5_Win'),'Description']='Number of games won in the last 5'
df.loc[(df['Features']=='Home_Lst_3_Win'),'Description']='Number of games won in the last 3'
df.loc[(df['Features']=='Home_Lst_5_in_Comp'),'Description']='Number of games won in the last 5 of that competition'
df.loc[(df['Features']=='Away_Lst_5_in_Comp'),'Description']='Number of games won in the last 5 of that competition'
df.loc[(df['Features']=='Derby'),'Description']='Home Country = Away Country'
df.loc[(df['Features']=='Home_Winning_Percentage'),'Description']='Total points / toal points available'
df.loc[(df['Features']=='Medium_Term_Uncertainty'),'Description']='Winning percentage * home winning percentage'
df.loc[(df['Features']=='Days_Since_Lst_Game_Dummy'),'Description']='Budget Constraint: Within two weeks, a month or above'
df.loc[(df['Features']=='Lst_Game_in_Comp_Dummy'),'Description']='Budget Constraint: Within two weeks, a month or above'
df.loc[(df['Features']=='Day_of_Week'),'Description']='Substitutes: Sunday - Saturday'
df.loc[(df['Features']=='Month_of_Year'),'Description']='Substitutes: January - December'
df.loc[(df['Features']=='Kick_off_Hour'),'Description']='Substitutes: Early - Afternoon - Evening'
df.loc[(df['Features']=='Sentiment'),'Description']= 'Budget Constraint: Consumer sentiment in month of game in home Country'
df.loc[(df['Features']=='Temp_Dummy'),'Description']='3 level dummy'
df.loc[(df['Features']=='Wind_Dummy'),'Description']='3 level dummy'
df.loc[(df['Features']=='Rain_Dummy'),'Description']='3 level dummy'
df.loc[(df['Features']=='Stadium_Age_Dummy'),'Description']='3 level dummy'
df.loc[(df['Features']=='Stadium_Age'),'Description']='Years since stadium built'
df.loc[(df['Features']=='(log)Attendance'),'Description']='Log of Attendance'
df.loc[(df['Features']=='Attendance'),'Description']='Actual Attendance'
df.loc[(df['Features']=='Stadium_Percentage'),'Description']='Attendance / Stadium Capacity'

savepath='C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Exploratory Data Analysis/'
savedfile=df.to_html(savepath+'Feature Description.html',index=False) 

teamvenuepivot=pd.pivot_table(explore, index=['Home_Team','Venue'],values='Tournament',aggfunc='count').reset_index()
teamvenuepivot=teamvenuepivot.drop(columns=['Tournament']) 
savedfile=teamvenuepivot.to_html(savepath+'Team Venue Review.html',index=False)     
teamvenuepivot=pd.pivot_table(explore, index=['Venue','Home_Team'],values='Tournament',aggfunc='count').reset_index()
teamvenuepivot=teamvenuepivot.drop(columns=['Tournament']) 
savedfile=teamvenuepivot.to_html(savepath+'Venue Team Review.html',index=False)     
    
    
    
    
    
    
    
    
    