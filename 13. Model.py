# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn import linear_model
# from	sklearn.linear_model	import	LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import r2_score
# from sklearn.ensemble import RandomForestRegressor
# import math
# import statsmodels.api as sm
# from scipy import stats
# from sklearn.feature_selection import RFE
# from statsmodels.graphics.gofplots import ProbPlot
# import seaborn as sns
# plt.style.use('seaborn') # pretty matplotlib plots
# plt.rc('font', size=14)
# plt.rc('figure', titlesize=18)
# plt.rc('axes', labelsize=15)
# plt.rc('axes', titlesize=18)

# """#########################
# IMPORT THE GAME DATA
# """
# dfAt=pd.read_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Final Data for Model2.csv', encoding='latin')



# """#########################
# PLOT THE DISTRIBUTION OF THE ATTENDANCE
# """
# plt.hist(dfAt['Attendance'],color='steelblue')
# plt.xlabel('Attendance')
# plt.ylabel('Quantity')
# plt.title('Distribution of Attendance')
# plt.hlines(y=0, xmin=0, xmax=70000, color='black', lw=2)
# plt.xlim([0, 70000])
# #plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Distribution of Attendance.jpeg')
# plt.show()


# """########################
# CHANGE THE ATTENDANCE TO THE LOG OF THE ATTENDANCE
# """
# dfAt['Attendance']=dfAt['Attendance'].apply(np.log)
# #dfAt['Attendance']=dfAt['Attendance'].apply(np.log10)
# #dfAt['Attendance']=dfAt['Attendance'].apply(np.log2)
# #dfAt['Attendance']=dfAt['Attendance'].apply(np.log1p)

# """#########################
# PLOT THE DISTRIBUTION OF THE ATTENDANCE WITH LOG ATTENDANCE
# """
# plt.hist(dfAt['Attendance'],color='steelblue')
# plt.xlabel('Attendance')
# plt.ylabel('Quantity')
# plt.title('Distribution of (log)Attendance')
# plt.hlines(y=0, xmin=6, xmax=12, color='black', lw=2) #xmax=5 for log10/ xmin=8 xmax=16 for log2/ xmin=6 xmax=16 for log1p
# plt.xlim([6, 12])
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Distribution of (log10)Attendance.jpeg')
# plt.show()

# # print(np.log10(15000))
# # log=np.log10(15000)
# # print(np.exp(log))

# """########################
# Set the Training, Validate and Test Data
# """
# X = dfAt.iloc[:, :-1]
# y = dfAt['Attendance']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=1)


# """#########################
# Also the average for the MAPE calculation
# """
# y_train_avg=np.mean(y_train)
# y_val_avg=np.mean(y_val)
# y_test_avg=np.mean(y_test)

# """##########################
# Model 1 Multiple Regression  on Attendance
# """
# mlr=linear_model.LinearRegression()
# mlr.fit(X_train,y_train)
# y_train_pred=mlr.predict(X_train)
# y_val_pred=mlr.predict(X_val)

# """########################
# Evaluate Regression on Train and Validate set
# """

# print('RMSE train: %.3f, Val: %.3f' % (mean_squared_error(y_train, y_train_pred, squared=False),mean_squared_error(y_val, y_val_pred, squared=False)))
# print('R^2 train: %.3f, Val: %.3f' % (r2_score(y_train, y_train_pred), r2_score(y_val, y_val_pred)))
# rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
# rmse_val=mean_squared_error(y_val, y_val_pred,squared=False)
# r2_train=r2_score(y_train, y_train_pred)
# r2_val=r2_score(y_val, y_val_pred)
# mapeTrain=rmse_train/y_train_avg
# mapeVal=rmse_val/y_val_avg
# print('Train MAPE = '+str(mapeTrain))
# print('Val MAPE = '+str(mapeVal))
#for i, prediction in enumerate(y_val_pred,start=1):
#    print('Predicted: %s. Target: %s' % (prediction, y_val[i])+'      '+str(round(prediction-y_val[i])))

# """########################
# Create a DataFrame of results for comparison later
# """
# mrresults=[rmse_train,rmse_val,r2_train,r2_val,mapeTrain,mapeVal]
# regResult1=pd.DataFrame(mrresults).T
# regResult1=regResult1.rename(columns={0:'RMSE Train',1:'RMSE Val',2:'R2 Train',3:'R2 Val',4:'Mape Train',5:'Mape Val'})
# regResult1['Overfit3']=regResult1['Mape Train']-regResult1['Mape Val']
# regResult1['Overfit2']=regResult1['Overfit3']**2
# regResult1['Overfit']=np.sqrt(regResult1['Overfit2'])
# regResult1=regResult1.drop(columns=['Overfit3','Overfit2'])

# """########################
# Plot the Model
# """
# #Scatter Plot of Residuals
# plt.scatter(y_train_pred,  y_train_pred - y_train,
#             c='steelblue', marker='o', edgecolor='white',
#             label='Training data')
# plt.scatter(y_val_pred,  y_val_pred - y_val,
#             c='limegreen', marker='s', edgecolor='white',
#             label='Validation data')
# plt.xlabel('Fitted values')
# plt.ylabel('Residuals')
# plt.title('Residuals vs Fitted')
# plt.legend(loc='upper left')
# plt.hlines(y=0, xmin=6, xmax=12, color='black', lw=2)
# plt.xlim([6, 12])
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Plot the Residuals.jpeg')
# plt.show()

# #QQ PLot of Residuals
# trainres=y_train_pred - y_train
# fig = sm.qqplot(trainres,fit=True, line='45',
#                 c='steelblue', marker='o', 
#                 label='Residuals')
# plt.ylabel('Residuals')
# plt.legend(loc='upper left')
# plt.title('Normal Q-Q')
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/QQPlot.jpeg')
# plt.show()


# """#########################
# Ordinary Least Squares of Model
# """
# X2=sm.add_constant(X_train)
# model = sm.OLS(y_train, X2)
# model_fit = model.fit()
# dataframe = pd.concat([X_train, y_train], axis=1)

# # model values
# model_fitted_y = model_fit.fittedvalues
# # model residuals
# model_residuals = model_fit.resid
# # absolute squared  residuals
# model_residuals_abs_sqrt = np.sqrt(np.abs(model_residuals))
# # normalized residuals
# model_norm_residuals = model_fit.get_influence().resid_studentized_internal
# # absolute squared normalized residuals
# model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))
# # absolute residuals
# model_abs_resid = np.abs(model_residuals)
# # leverage, from statsmodels internals
# model_leverage = model_fit.get_influence().hat_matrix_diag
# # cook's distance, from statsmodels internals
# model_cooks = model_fit.get_influence().cooks_distance[0]


# #Scale Loction
# plot_lm_3 = plt.figure()
# plt.scatter(model_fitted_y, model_residuals_abs_sqrt, alpha=0.5);
# sns.regplot(model_fitted_y, model_residuals_abs_sqrt,
#             scatter=False,
#             ci=False,
#             lowess=True,
#             line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
# plot_lm_3.axes[0].set_title('Scale-Location')
# plot_lm_3.axes[0].set_xlabel('Fitted values')
# plot_lm_3.axes[0].set_ylabel('Residuals');
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Scale Location.jpeg')

# #Scale Loction
# plot_lm_3 = plt.figure()
# plt.scatter(model_fitted_y, model_norm_residuals_abs_sqrt, alpha=0.5);
# sns.regplot(model_fitted_y, model_norm_residuals_abs_sqrt,
#             scatter=False,
#             ci=False,
#             lowess=True,
#             line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
# plot_lm_3.axes[0].set_title('Scale-Location')
# plot_lm_3.axes[0].set_xlabel('Fitted values')
# plot_lm_3.axes[0].set_ylabel('$\sqrt{|Standardized Residuals|}$');
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Normalised Scale Location.jpeg')

# plot_lm_4 = plt.figure();
# plt.scatter(model_leverage, model_residuals, alpha=0.5);
# sns.regplot(model_leverage, model_residuals,
#               scatter=False,
#               ci=False,
#               lowess=True,
#               line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
# plot_lm_4.axes[0].set_xlim(0, max(model_leverage)+0.01)
# plot_lm_4.axes[0].set_ylim(-.5, .5) #-.5 +.5 with log
# plot_lm_4.axes[0].set_title('Residuals vs Leverage')
# plot_lm_4.axes[0].set_xlabel('Leverage')
# plot_lm_4.axes[0].set_ylabel('Residuals'); 
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Residual Leverage.jpeg')               
                  
# plot_lm_4 = plt.figure();
# plt.scatter(model_leverage, model_norm_residuals, alpha=0.5);
# sns.regplot(model_leverage, model_norm_residuals,
#               scatter=False,
#               ci=False,
#               lowess=True,
#               line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
# plot_lm_4.axes[0].set_xlim(0, max(model_leverage)+0.01)
# plot_lm_4.axes[0].set_ylim(-3, 5)
# plot_lm_4.axes[0].set_title('Residuals vs Leverage')
# plot_lm_4.axes[0].set_xlabel('Leverage')
# plot_lm_4.axes[0].set_ylabel('Standardized Residuals');
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Standardised Leverage.jpeg')   

# """##############################
# Get the OLS Results
# """
# with open('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/OLS Summary.csv', 'w') as fh:
#     fh.write(model_fit.summary().as_csv())


# """##########################
# Feature Selection
# """

# mrresults=[]
# for i in range(1,73):
#     print(i)
#     result=[]
#     result.append(i)
#     rfe = RFE(mlr, i)
#     rfe = rfe.fit(X_train, y_train)
#     y_train_pred = rfe.predict(X_train)
#     dfy_train_pred=pd.DataFrame(y_train_pred)
#     y_val_pred = rfe.predict(X_val)
#     rmse_train=mean_squared_error(y_train, y_train_pred,squared=False)
#     result.append(rmse_train)
#     rmse_val=mean_squared_error(y_val, y_val_pred,squared=False)
#     result.append(rmse_val)
#     r2_train=r2_score(y_train, y_train_pred)
#     result.append(r2_train)
#     r2_val=r2_score(y_val, y_val_pred)
#     result.append(r2_val)
#     print('RMSE train: %.3f, val: %.3f' % (mean_squared_error(y_train, y_train_pred,squared=False),mean_squared_error(y_val, y_val_pred,squared=False)))
#     print('R^2 train: %.3f, val: %.3f' % (r2_score(y_train, y_train_pred),r2_score(y_val, y_val_pred)))
#     MeaTrain=rmse_train/y_train_avg
#     Meaval=rmse_val/y_val_avg
#     result.append(MeaTrain)
#     result.append(Meaval)
#     print('Train MAPE = '+str(MeaTrain))
#     print('Val MAPE = '+str(Meaval))
#     mrresults.append(result)
    
# regResult=pd.DataFrame(mrresults)
# regResult=regResult.rename(columns={0:'Features',1:'RMSE Train',2:'RMSE Val',3:'R2 Train',4:'R2 Val',5:'Mape Train',6:'Mape Val'})
# regResult['Overfit3']=regResult['Mape Train']-regResult['Mape Val']
# regResult['Overfit2']=regResult['Overfit3']**2
# regResult['Overfit']=np.sqrt(regResult['Overfit2'])
# regResult=regResult.drop(columns=['Overfit3','Overfit2'])
# regResult['Val Attendance']=10**regResult['Mape Val']
# y_val_join=y_val.reset_index(drop=True)
# regResult=regResult.join(y_val_join,how='outer')
# regResult['Y_Val Attendance']=
# savedfile=regResult.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Regression Feature Selection Results.csv',index=False)

# plt.plot(regResult['Mape Train'],color='steelblue',label='Train MAPE')
# plt.plot(regResult['Mape Val'],color='limegreen',label='Validate MAPE')
# plt.plot(regResult['Overfit'],color='red',label='Overfit')
# plt.xlabel('Features')
# plt.ylabel('MAPE & Overfit')
# plt.title('Features vs MAPE')
# plt.legend(loc='upper right')
# plt.hlines(y=0.0302461, xmin=0, xmax=73, color='red', lw=.5)
# plt.xlim([0, 73])
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/fEATURES VS mape.jpeg')
# plt.show()


# rfe = RFE(mlr, 1)
# rfe = rfe.fit(X_train, y_train)
# #Examine the Features
# ranking=rfe.ranking_
# ranks=pd.DataFrame(ranking)
# ranks=ranks.rename(columns={0:'Ranking'})
# features=pd.DataFrame(X_train.columns)
# features=features.rename(columns={0:'Features'})
# featureRanks=ranks.join(features,how='outer')
# savedfile=featureRanks.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Regression Feature Selection Rankings.csv',index=False)


# """########################
# Adjust the model
# ###(log)Attendance
# Venue_La Ghirada
# Venue_Principality Stadium
# Venue_Aviva Stadium
# Venue_Thomond Park
# Venue_Kingspan Stadium
# Venue_Stadio Sergio Lanfranchi
# Venue_Meggetland
# Venue_Stadio Tommaso Fattori
# Venue_Liberty Stadium
# Venue_The Sportsground
# Venue_Eugene Cross Park
# Venue_Morganstone Brewery Field
# Venue_Parc y Scarlets

# Home Team_Leinster Rugby
# Home Team_Benetton Treviso
# Home Team_Ulster Rugby
# Home Team_Cardiff Blues
# Home Team_Scarlets
# Home Team_Zebre Rugby

# Derby_Extra Derby
# Derby_Derby

# Tournament_Champions Cup
# Tournament_League

# Age of Stadium_Old
# Age of Stadium_Middle Age

# Kick Off Hour_Early

# Number ofP14 Wins

# Away Country_Ireland
# Away Country_Italy
# Away Country_Wales


# ###Attendance
# Venue_Principality Stadium
# Venue_Aviva Stadium
# Venue_Kingspan Stadium
# Venue_Thomond Park
# Venue_Stadio Sergio Lanfranchi
# Venue_Meggetland
# Venue_La Ghirada
# Venue_Venue_Stadio Monigo
# Venue_Stadio Tommaso Fattori
# Venue_Liberty Stadium
# Venue_Irish Independent Park
# Venue_Parc y Scarlets
# Venue_Myreside
# Venue_Morganstone Brewery Field
# Venue_Eugene Cross Park

# Home Team_Ulster Rugby
# Home Team_Leinster Rugby
# Home Team_Benetton Treviso
# Home Team_Connacht Rugby
# Home Team_Scarlets
# Home Team_Cardiff Blues

# Derby_Extra Derby
# Derby_Derby

# Tournament_Champions Cup
# Tournament_League

# Age of Stadium_Old

# Number ofP14 Wins

# Win Probability

# Away Country_Italy
# Away Country_Ireland
# Away Country_Wales
# Away Country_Scotland

# Wind_Normal
# Kick Off Hour_Afternoon
# Day Of Week
# Age of Stadium_Middle Age
# Temperature_Warm
# Home Last_5_W/L
# Win Probability Dummy_Even


# """

# """########################
# Set the Training, Validate and Test Data
# """
# X_train=X_train[['Venue_La Ghirada','Venue_Principality Stadium','Venue_Aviva Stadium','Venue_Thomond Park','Venue_Kingspan Stadium',\
#            'Venue_Stadio Sergio Lanfranchi','Venue_Meggetland','Venue_Stadio Tommaso Fattori','Venue_Liberty Stadium','Venue_The Sportsground',\
#            'Venue_Eugene Cross Park','Venue_Morganstone Brewery Field','Venue_Parc y Scarlets','Home Team_Leinster Rugby','Home Team_Benetton Treviso',\
#            'Home Team_Ulster Rugby','Home Team_Cardiff Blues','Home Team_Scarlets','Home Team_Zebre Rugby','Derby_Extra Derby','Derby_Derby',\
#            'Tournament_Champions Cup','Tournament_League','Age of Stadium_Old','Age of Stadium_Middle Age','Kick Off Hour_Early',\
#            'Number ofP14 Wins','Away Country_Ireland','Away Country_Italy','Away Country_Wales']]    
# X_val=X_val[['Venue_La Ghirada','Venue_Principality Stadium','Venue_Aviva Stadium','Venue_Thomond Park','Venue_Kingspan Stadium',\
#            'Venue_Stadio Sergio Lanfranchi','Venue_Meggetland','Venue_Stadio Tommaso Fattori','Venue_Liberty Stadium','Venue_The Sportsground',\
#            'Venue_Eugene Cross Park','Venue_Morganstone Brewery Field','Venue_Parc y Scarlets','Home Team_Leinster Rugby','Home Team_Benetton Treviso',\
#            'Home Team_Ulster Rugby','Home Team_Cardiff Blues','Home Team_Scarlets','Home Team_Zebre Rugby','Derby_Extra Derby','Derby_Derby',\
#            'Tournament_Champions Cup','Tournament_League','Age of Stadium_Old','Age of Stadium_Middle Age','Kick Off Hour_Early',\
#            'Number ofP14 Wins','Away Country_Ireland','Away Country_Italy','Away Country_Wales']]  
# X_test=X_test[['Venue_La Ghirada','Venue_Principality Stadium','Venue_Aviva Stadium','Venue_Thomond Park','Venue_Kingspan Stadium',\
#            'Venue_Stadio Sergio Lanfranchi','Venue_Meggetland','Venue_Stadio Tommaso Fattori','Venue_Liberty Stadium','Venue_The Sportsground',\
#            'Venue_Eugene Cross Park','Venue_Morganstone Brewery Field','Venue_Parc y Scarlets','Home Team_Leinster Rugby','Home Team_Benetton Treviso',\
#            'Home Team_Ulster Rugby','Home Team_Cardiff Blues','Home Team_Scarlets','Home Team_Zebre Rugby','Derby_Extra Derby','Derby_Derby',\
#            'Tournament_Champions Cup','Tournament_League','Age of Stadium_Old','Age of Stadium_Middle Age','Kick Off Hour_Early',\
#            'Number ofP14 Wins','Away Country_Ireland','Away Country_Italy','Away Country_Wales']]    

  
                 
# """##########################
# Model 1 Multiple Regression  on Attendance
# """
# mlr=LinearRegression()
# mlr.fit(X_train,y_train)
# y_train_pred=mlr.predict(X_train)
# y_val_pred=mlr.predict(X_val)

# """########################
# Evaluate Regression on Train and Validate set
# """
# print('MSE train: %.3f, Val: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_val, y_val_pred)))
# print('R^2 train: %.3f, Val: %.3f' % (r2_score(y_train, y_train_pred), r2_score(y_val, y_val_pred)))
# mse_train=mean_squared_error(y_train, y_train_pred)
# mse_val=mean_squared_error(y_val, y_val_pred)
# r2_train=r2_score(y_train, y_train_pred)
# r2_val=r2_score(y_val, y_val_pred)
# train_error=math.sqrt(mean_squared_error(y_train, y_train_pred))
# val_error=math.sqrt(mean_squared_error(y_val, y_val_pred))
# MeaTrain=train_error/y_train_avg
# Meaval=val_error/y_val_avg
# print('Train MAPE = '+str(MeaTrain))
# print('Val MAPE = '+str(Meaval))
# #for i, prediction in enumerate(y_val_pred,start=1):
# #    print('Predicted: %s. Target: %s' % (prediction, y_val[i])+'      '+str(round(prediction-y_val[i])))

# """########################
# Create a DataFrame of results for comparison later
# """
# mrresults=[mse_train,mse_val,r2_train,r2_val,MeaTrain,Meaval]
# regResult1=pd.DataFrame(mrresults).T
# regResult1=regResult1.rename(columns={0:'MSE Train',1:'MSE Val',2:'R2 Train',3:'R2 Val',4:'Mape Train',5:'Mape Val'})
# regResult1['Overfit3']=regResult1['Mape Train']-regResult1['Mape Val']
# regResult1['Overfit2']=regResult1['Overfit3']**2
# regResult1['Overfit']=np.sqrt(regResult1['Overfit2'])
# regResult1=regResult1.drop(columns=['Overfit3','Overfit2'])

# """########################
# Plot the Model
# """
# #Scatter Plot of Residuals
# plt.scatter(y_train_pred,  y_train_pred - y_train,
#             c='steelblue', marker='o', edgecolor='white',
#             label='Training data')
# plt.scatter(y_val_pred,  y_val_pred - y_val,
#             c='limegreen', marker='s', edgecolor='white',
#             label='val data')
# plt.xlabel('Fitted values')
# plt.ylabel('Residuals')
# plt.title('Residuals vs Fitted')
# plt.legend(loc='upper left')
# plt.hlines(y=0, xmin=2.5, xmax=5, color='black', lw=2)
# plt.xlim([2.5, 5])
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Plot the Residuals with FS.jpeg')
# plt.show()

# #QQ PLot of Residuals
# trainres=y_train_pred - y_train
# fig = sm.qqplot(trainres,fit=True, line='45',
#                 c='steelblue', marker='o', 
#                 label='Residuals')
# plt.ylabel('Residuals')
# plt.legend(loc='upper left')
# plt.title('Normal Q-Q')
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/QQPlot with FS.jpeg')
# plt.show()


# """#########################
# Ordinary Least Squares of Model
# """
# X2=sm.add_constant(X_train)
# model = sm.OLS(y_train, X2)
# model_fit = model.fit()
# dataframe = pd.concat([X_train, y_train], axis=1)

# # model values
# model_fitted_y = model_fit.fittedvalues
# # model residuals
# model_residuals = model_fit.resid
# # absolute squared  residuals
# model_residuals_abs_sqrt = np.sqrt(np.abs(model_residuals))
# # normalized residuals
# model_norm_residuals = model_fit.get_influence().resid_studentized_internal
# # absolute squared normalized residuals
# model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))
# # absolute residuals
# model_abs_resid = np.abs(model_residuals)
# # leverage, from statsmodels internals
# model_leverage = model_fit.get_influence().hat_matrix_diag
# # cook's distance, from statsmodels internals
# model_cooks = model_fit.get_influence().cooks_distance[0]


# #Scale Loction
# plot_lm_3 = plt.figure()
# plt.scatter(model_fitted_y, model_residuals_abs_sqrt, alpha=0.5);
# sns.regplot(model_fitted_y, model_residuals_abs_sqrt,
#             scatter=False,
#             ci=False,
#             lowess=True,
#             line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
# plot_lm_3.axes[0].set_title('Scale-Location')
# plot_lm_3.axes[0].set_xlabel('Fitted values')
# plot_lm_3.axes[0].set_ylabel('Residuals');
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Scale Location with FS.jpeg')

# #Scale Loction
# plot_lm_3 = plt.figure()
# plt.scatter(model_fitted_y, model_norm_residuals_abs_sqrt, alpha=0.5);
# sns.regplot(model_fitted_y, model_norm_residuals_abs_sqrt,
#             scatter=False,
#             ci=False,
#             lowess=True,
#             line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
# plot_lm_3.axes[0].set_title('Scale-Location')
# plot_lm_3.axes[0].set_xlabel('Fitted values')
# plot_lm_3.axes[0].set_ylabel('$\sqrt{|Standardized Residuals|}$');
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Normalised Scale Location with FS.jpeg')

# plot_lm_4 = plt.figure();
# plt.scatter(model_leverage, model_residuals, alpha=0.5);
# sns.regplot(model_leverage, model_residuals,
#               scatter=False,
#               ci=False,
#               lowess=True,
#               line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
# plot_lm_4.axes[0].set_xlim(0, max(model_leverage)+0.01)
# plot_lm_4.axes[0].set_ylim(-.5, .5)
# plot_lm_4.axes[0].set_title('Residuals vs Leverage')
# plot_lm_4.axes[0].set_xlabel('Leverage')
# plot_lm_4.axes[0].set_ylabel('Residuals'); 
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Residual Leverage with FS.jpeg')               
                  
# plot_lm_4 = plt.figure();
# plt.scatter(model_leverage, model_norm_residuals, alpha=0.5);
# sns.regplot(model_leverage, model_norm_residuals,
#               scatter=False,
#               ci=False,
#               lowess=True,
#               line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
# plot_lm_4.axes[0].set_xlim(0, max(model_leverage)+0.01)
# plot_lm_4.axes[0].set_ylim(-3, 5)
# plot_lm_4.axes[0].set_title('Residuals vs Leverage')
# plot_lm_4.axes[0].set_xlabel('Leverage')
# plot_lm_4.axes[0].set_ylabel('Standardized Residuals');
# plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Standardised Leverage with FS.jpeg')   

# """##############################
# Get the OLS Results
# """
# with open('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/OLS Summary with FS.csv', 'w') as fh:
#     fh.write(model_fit.summary().as_csv())

"""
Run Model on Test Data
"""
y_test_pred = mlr.predict(X_test)
mse_test=mean_squared_error(y_test, y_test_pred)
r2_val=r2_score(y_test, y_test_pred)
print('MSE test: %.3f' % (mean_squared_error(y_test, y_test_pred)))
print('R^2 test: %.3f' % (r2_score(y_test, y_test_pred)))
test_error=math.sqrt(mean_squared_error(y_test, y_test_pred))
Meatest=test_error/y_test_avg
print('Test MAPE = '+str(Meatest))



"""########################
Plot the Test Results
"""
#Scatter Plot of Residuals
plt.scatter(y_test_pred,  y_test_pred - y_test,
            c='steelblue', marker='o', edgecolor='white',
            label='Training data')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('Test Data: Residuals vs Fitted')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=2.5, xmax=5, color='black', lw=2)
plt.xlim([2.5, 5])
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Plot the Test Residuals.jpeg')
plt.show()

#QQ PLot of Residuals
testres=y_test_pred - y_test
fig = sm.qqplot(testres,fit=True, line='45',
                c='steelblue', marker='o', 
                label='Residuals')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.title('Test Data: Normal Q-Q')
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Test QQPlot.jpeg')
plt.show()


"""#########################
Ordinary Least Squares of Model
"""
X2=sm.add_constant(X_test)
model = sm.OLS(y_test, X2)
model_fit = model.fit()
dataframe = pd.concat([X_test, y_test], axis=1)

# model values
model_fitted_y = model_fit.fittedvalues
# model residuals
model_residuals = model_fit.resid
# absolute squared  residuals
model_residuals_abs_sqrt = np.sqrt(np.abs(model_residuals))
# normalized residuals
model_norm_residuals = model_fit.get_influence().resid_studentized_internal
# absolute squared normalized residuals
model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))
# absolute residuals
model_abs_resid = np.abs(model_residuals)
# leverage, from statsmodels internals
model_leverage = model_fit.get_influence().hat_matrix_diag
# cook's distance, from statsmodels internals
model_cooks = model_fit.get_influence().cooks_distance[0]


#Scale Loction
plot_lm_3 = plt.figure()
plt.scatter(model_fitted_y, model_residuals_abs_sqrt, alpha=0.5);
sns.regplot(model_fitted_y, model_residuals_abs_sqrt,
            scatter=False,
            ci=False,
            lowess=True,
            line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
plot_lm_3.axes[0].set_title('Test Data: Scale-Location')
plot_lm_3.axes[0].set_xlabel('Fitted values')
plot_lm_3.axes[0].set_ylabel('Residuals');
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Test Scale Location.jpeg')

#Scale Loction
plot_lm_3 = plt.figure()
plt.scatter(model_fitted_y, model_norm_residuals_abs_sqrt, alpha=0.5);
sns.regplot(model_fitted_y, model_norm_residuals_abs_sqrt,
            scatter=False,
            ci=False,
            lowess=True,
            line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
plot_lm_3.axes[0].set_title('Test Data: Scale-Location')
plot_lm_3.axes[0].set_xlabel('Fitted values')
plot_lm_3.axes[0].set_ylabel('$\sqrt{|Standardized Residuals|}$');
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Test Normalised Scale.jpeg')

plot_lm_4 = plt.figure();
plt.scatter(model_leverage, model_residuals, alpha=0.5);
sns.regplot(model_leverage, model_residuals,
              scatter=False,
              ci=False,
              lowess=True,
              line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
plot_lm_4.axes[0].set_xlim(0, max(model_leverage)+0.01)
plot_lm_4.axes[0].set_ylim(-.5, .5)
plot_lm_4.axes[0].set_title('Test Data: Residuals vs Leverage')
plot_lm_4.axes[0].set_xlabel('Leverage')
plot_lm_4.axes[0].set_ylabel('Residuals'); 
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Test Residual Leverage.jpeg')               
                  
plot_lm_4 = plt.figure();
plt.scatter(model_leverage, model_norm_residuals, alpha=0.5);
sns.regplot(model_leverage, model_norm_residuals,
              scatter=False,
              ci=False,
              lowess=True,
              line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8});
plot_lm_4.axes[0].set_xlim(0, max(model_leverage)+0.01)
plot_lm_4.axes[0].set_ylim(-3, 5)
plot_lm_4.axes[0].set_title('Test Data: Residuals vs Leverage')
plot_lm_4.axes[0].set_xlabel('Leverage')
plot_lm_4.axes[0].set_ylabel('Standardized Residuals');
plt.savefig('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Test Standardised Leverage.jpeg')   

"""##############################
Get the OLS Results
"""
with open('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Test OLS Summary.csv', 'w') as fh:
    fh.write(model_fit.summary().as_csv())

y_test2=pd.DataFrame(y_test.reset_index(drop=True))
prediction=pd.DataFrame(y_test_pred)
#for i, prediction in enumerate(y_test_pred):
#    print('Predicted: %s. Target: %s' % ((10**(prediction)), (10**(y_test2[i]))+'      '+str(round(prediction-y_test2[i])))
testResults=y_test2.join(prediction)
testResults=testResults.rename(columns={0:'Prediction'})
testResults['Attendance2']=10**testResults['Attendance']
testResults['Prediction2']=10**testResults['Prediction']
testResults['Error']=testResults['Prediction2']-testResults['Attendance2']
testResults['Squared Error']=testResults['Error']**2
mse=testResults['Squared Error'].mean()
test_error=math.sqrt(mse)
test_avg=testResults['Attendance2'].mean()
Meatest=test_error/test_avg
print('Test MAPE = '+str(Meatest))

print(10**4.12241)
""""""
""""""
""""""
""""""
""""""
# #Model 3 Random Forest on Attendance

# forest = RandomForestRegressor(n_estimators=500,criterion='mse',random_state=1,n_jobs=-1)
# forest.fit(X_train, y_train)
# y_train_pred = forest.predict(X_train)
# y_val_pred = forest.predict(X_val)

#Evaluate Forest
# print('MSE train: %.3f, val: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_val, y_val_pred)))
# print('R^2 train: %.3f, val: %.3f' % (r2_score(y_train, y_train_pred), r2_score(y_val, y_val_pred)))
# train_error=math.sqrt(mean_squared_error(y_train, y_train_pred))
# val_error=math.sqrt(mean_squared_error(y_val, y_val_pred))
# MeaTrain=train_error/y_train_avg
# Meaval=val_error/y_val_avg
# print('Train MAPE = '+str(MeaTrain))
# print('val MAPE = '+str(Meaval))

y_test_pred=forest.predict(X_test)
print('MSE Test: %.3f' % (mean_squared_error(y_test, y_test_pred)))
print('R^2 Test: %.3f' % (r2_score(y_test, y_test_pred)))
test_error=math.sqrt(mean_squared_error(y_test, y_test_pred))
MeaTest=test_error/y_test_avg
print('Test MAPE = '+str(MeaTest))

plt.scatter(y_train_pred,y_train_pred - y_train,c='steelblue',edgecolor='white',marker='o', s=35,alpha=0.9,label='Training data')
plt.scatter(y_val_pred,y_val_pred - y_val, c='limegreen', edgecolor='white',  marker='s', s=35, alpha=0.9, label='val data')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=2.5, xmax=5, lw=2, color='black')
plt.xlim([2.5, 5])
plt.show()


  
rfresults=[]
for i in range(1,60):
    result=[]
    rfe = RFE(forest, i)
    rfe = rfe.fit(X_train, y_train)
    y_train_pred = rfe.predict(X_train)
    y_val_pred = rfe.predict(X_val)
    mse_train=mean_squared_error(y_train, y_train_pred)
    result.append(mse_train)
    mse_val=mean_squared_error(y_val, y_val_pred)
    result.append(mse_val)
    r2_train=r2_score(y_train, y_train_pred)
    result.append(r2_train)
    r2_val=r2_score(y_val, y_val_pred)
    result.append(r2_val)
    print('MSE train: %.3f, val: %.3f' % (mean_squared_error(y_train, y_train_pred),mean_squared_error(y_val, y_val_pred)))
    print('R^2 train: %.3f, val: %.3f' % (r2_score(y_train, y_train_pred),r2_score(y_val, y_val_pred)))
    train_error=math.sqrt(mean_squared_error(y_train, y_train_pred))
    val_error=math.sqrt(mean_squared_error(y_val, y_val_pred))
    MeaTrain=train_error/y_train_avg
    Meaval=val_error/y_val_avg
    result.append(MeaTrain)
    result.append(Meaval)
    print('Train MAPE = '+str(MeaTrain))
    print('val MAPE = '+str(Meaval))
    rfresults.append(result)
    
dfResult=pd.DataFrame(rfresults)
dfResult=dfResult.rename(columns={0:'MSE Train',1:'MSE Val',2:'R2 Train',3:'R2 Val',4:'Mape Train',5:'Mape Val'})
dfResult['Overfit']=dfResult['Mape Train']-dfResult['Mape Val']
dfResult['Overfit2']=dfResult['Overfit']**2
dfResult['Overfit3']=np.sqrt(dfResult['Overfit2'])
savedfile=dfResult.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Random Forest Feature Selection Results.csv',index=False)

ranking=rfe.ranking_
ranks=pd.DataFrame(ranking)
ranks=ranks.rename(columns={0:'Ranking'})
features=pd.DataFrame(X_train.columns)
features=features.rename(columns={0:'Features'})
featureRanks=ranks.join(features,how='outer')
savedfile=featureRanks.to_csv('C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Model/Random Forest Feature Selection Rankings.csv',index=False)

#
#plt.scatter(y_train_pred,y_train_pred - y_train,c='steelblue',edgecolor='white',marker='o', s=35,alpha=0.9,label='Training data')
#plt.scatter(y_test_pred,y_test_pred - y_test, c='limegreen', edgecolor='white',  marker='s', s=35, alpha=0.9, label='Test data')
#plt.xlabel('Predicted values')
#plt.ylabel('Residuals')
#plt.legend(loc='upper left')
#plt.hlines(y=0, xmin=2.5, xmax=1, lw=2, color='black')
#plt.xlim([0, 1])
#plt.show()
# 
#from itertools import combinations
#x=[1,2,3,4,5,6,7]
#for i in combinations(x,r=7):
#    print(i)