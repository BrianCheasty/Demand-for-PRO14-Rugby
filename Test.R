library(dplyr)
library(ggplot2)
install.packages("psych")
library(psych)
library(tidyverse)
install.packages('kableExtra')
games <-  read.csv("C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Data for Model.csv",sep=",")

str(games)
summary(games)
plot(games$Home.Team,games$Attendance)
plot(games$Away.Team,games$Attendance)
plot(games$Derby,games$Attendance)
plot(games$Attendance)
hist(games$Attendance)
shapiro.test(games$Attendance)
#W = 0.63416, p-value < 2.2e-16
#The data does not pass the Shapiro-Wilk test with a result much less than 0.05
qqnorm(games$Attendance)
qqline(games$Attendance)
hist(summary(games$Home.Team))
#There is no obvious reason for the outliers and is likely down to the content which is not captured in this dataset
#It is accepted that content plays a huge role in Engagement, the categories applied by the company do not account for this variation
#More work is required to create an accurate model
#Type has the greatest distribution difference so is chosen to remove outliers by factor
#remove_outliers <- function(x, na.rm = TRUE, ...) {
#  qnt <- quantile(x, probs=c(.25, .75), na.rm = na.rm, ...)
#  H <- 1 * IQR(x, na.rm = na.rm)
#  y <- x
#  y[x < (qnt[1] - H)] <- NA
#  y[x > (qnt[2] + H)] <- NA
#  y
#}
#
#games <- games %>%
#  group_by(Type) %>%
#  mutate(Engaged = remove_outliers(Engaged))
#
#summary(games)
#
#From the summary we can see that we have outliers in the original dataset and introduced as a result of outliers
#The NA's are dealt with first
#Confirm that the dataframe has and na's
#sum(is.na(games))
#We have 6 not outlier NA's,check the columns 
#colswithNA <- sapply(games, function(x) sum(is.na(x)))
#namesofcollsWithNA <- names(which(colswithNA>0))
#print(namesofcollsWithNA)
##Paid, Like,Share
#sum(is.na(games$Paid))
##1 NA
#sum(is.na(games$like))
##1 NA
#sum(is.na(games$share))
##4 NA
#sum(is.na(games$Engaged))
#4 NA
#Looking at the results of a post, like and share are found in other metrics and unlikely to be used, 
#I will fill with the mean
#games$like[is.na(games$like)] <- mean(games$like,na.rm=TRUE)
#games$share[is.na(games$share)] <- mean(games$share,na.rm=TRUE)
#There is no statistic to replace Paid so this is to be removed,Engaged was introduced when dealing with outliers so will be removed
#games<- na.omit(games)

#summary(games)
#It can be seen from the summary that Engaged still has outliers
#Plotting the Variables after removal of Outliers
#plot(games$Category,games$Engaged)
#Outliers in all 3 Categories
#plot(games$Type,games$Engaged)
##Outliers in all 4 Types, distribution is different and removal of outliers best done by factor
#plot(games$Post.Month,games$Engaged)
#plot(games$Post.Weekday,games$Engaged)
#plot(games$Post.Hour,games$Engaged)
#plot(games$Engaged)
#hist(games$Engaged)
#The distribution still appears to have outliers which are not explained by the data
#It's important to note that the content is not included in the data set
#shapiro.test(games$Engaged)
#The data does not pass the Shapiro-Wilk test with a result much less than 0.05
#qqnorm(games$Engaged)
#qqline(games$Engaged)
#qqplot(games$Type,games$Engaged)

#plot(games$Category,games$Engaged)
#games <- games %>%
#  group_by(Category) %>%
#  mutate(Engaged = remove_outliers(Engaged))
#games<- na.omit(games)
#shapiro.test(games$Engaged)
#qqnorm(games$Engaged)
#qqline(games$Engaged)
#plot(games$Category,games$Engaged)

#plot(games$Post.Month,games$Engaged)
#games <- games %>%
#  group_by(Post.Month) %>%
#  mutate(Engaged = remove_outliers(Engaged))
#games<- na.omit(games)
#plot(games$Post.Month,games$Engaged)
#shapiro.test(games$Engaged)
#qqnorm(games$Engaged)
#qqline(games$Engaged)

#plot(games$Post.Weekday,games$Engaged)
#games <- games %>%
#  group_by(Post.Weekday) %>%
#  mutate(Engaged = remove_outliers(Engaged))
#games<- na.omit(games)
#plot(games$Post.Weekday,games$Engaged)
#shapiro.test(games$Engaged)
#qqnorm(games$Engaged)
#qqline(games$Engaged)

#plot(games$Post.Hour,games$Engaged)
#games <- games %>%
#  group_by(Post.Hour) %>%
#  mutate(Engaged = remove_outliers(Engaged))
#games<- na.omit(games)
#plot(games$Post.Hour,games$Engaged)
#shapiro.test(games$Engaged)
#qqnorm(games$Engaged)
#qqline(games$Engaged)

#plot(games$Post.Month,games$Engaged)
#games <- games %>%
#  group_by(Post.Month) %>%
#  mutate(Engaged = remove_outliers(Engaged))
#games<- na.omit(games)
#plot(games$Post.Month,games$Engaged)
#shapiro.test(games$Engaged)
#qqnorm(games$Engaged)
#qqline(games$Engaged)
#
#
#hist(games$Engaged)


model1 <- lm(Attendance ~ ., data=games)
summary(model1)
sigma(model1)/mean(games$Attendance)

step(model1, direction = "back", scope = formula(model1))
model2 <- lm(formula = Attendance ~ Tournament + Home.Team + Away.Table.Position + 
               Kick.Off.Hour + Derby + homeVSaway.Winning.Percentage + Stadium.Age + 
               Table.Difference, data = games)
summary(model2)
sigma(model2)
sigma(model2)/mean(games$Attendance)


step(fbmodel1, direction = "both", scope = formula(fbmodel1))
fbmodel2 <- lm(Engaged ~ Type+Post.Month+Paid, data=games)
#Mean Absolute Percent Error 28.7% vs 28.8% in study
summary(fbmodel2)
sigma(fbmodel2)/mean(games$Engaged)

#Exploring the relationships between the dependent variables
pairs.panels(games[c('PageLikes','Category','Type','Post.Month','Post.Weekday','Post.Hour','Paid')])
#Post Month and page likes have a correlation of .94, this is understandable given that the values would move in the same direction
#It could be argued that page likes are also a result of post results,
#the accumulation of results might correlate with the page likes
#It would make sense that a combination of the factors will influence the outcome. For example paid may have an influence but
#combined with month you would expect to see a greater impact from seasonality. Paid in December may have a greater
#impact than paid in June.
games$CatType <- as.factor(paste(games$Category,games$Type))
games$CatPaid <- as.factor(paste(games$Category,games$Paid))
games$TypePaid <- as.factor(paste(games$Type,games$Paid))
games$WeekHour <- as.factor(paste(games$Post.Weekday,games$Post.Hour))
games$MonthHour <- as.factor(paste(games$Post.Hour,games$Post.Month))
games$WeekMonth <- as.factor(paste(games$Post.Weekday,games$Post.Month))
games$MonthPaid <- as.factor(paste(games$Post.Month,games$Paid))
games$CatMonth <- as.factor(paste(games$Category,games$Post.Month))
games$TypeMonth <- as.factor(paste(games$Type,games$Post.Month))


pairs.panels(games[c('CatType','CatPaid','TypePaid','WeekHour','MonthHour','WeekMonth',
                        'MonthPaid','CatMonth','TypeMonth', 'Engaged')])

#We can see that there is strong correlation between some of the new variables and the target variable
#There is also correlation between them that needs to be handled
#Looking at the ones over 90%

pairs.panels(games[c('CatType','CatPaid','CatMonth','Engaged')])
#CatMonth has the highest correlation with the other variables and Engaged so is preferred

pairs.panels(games[c('WeekHour','MonthHour','WeekMonth','Engaged')])
#These variables have low correlation with the target variable, weekhour and weekmonth have a high correlation together so
#WeekHour is preferred

#These variables do not have high correlations with other variables
pairs.panels(games[c('MonthPaid','TypeMonth','Engaged')])
#Type Month is the most promising of these variables and is kept

#Reviewing the Independent Variables
pairs.panels(games[c('PageLikes','Category','Type','Post.Month','Post.Weekday','Post.Hour',
                        'Paid','CatMonth','TypeMonth','WeekHour','MonthPaid','Engaged')])

#Based on this and eliminating and remaining variables that correlate we choose the following for initial model creation
pairs.panels(games[c('Type','Post.Month','Post.Weekday','Post.Hour',
                        'Paid','TypeMonth','MonthHour','MonthPaid','Engaged')])

#Page Likes is removed due to the correlation with Post.Month and the lower correlation to Consumer
#Category is removed due to the high correlation to CatTypePaidMonth and the lower correlation to Consumer
#Cat Month is removed due to the high correlation to CatTypePaidMonth and lower correlation to Consumer

#First we run the model with all added variables
fbmodela <- lm(Engaged ~PageLikes+Category+Type+Post.Month+Post.Weekday+Post.Hour+Paid+
                 CatMonth+TypeMonth+WeekHour+MonthPaid, data=games)
summary(fbmodela)
sigma(fbmodela)/mean(games$Engaged)
step(fbmodela, direction = "back", scope = formula(fbmodela))
step(fbmodela, direction = "both", scope = formula(fbmodela))
fbmodela2 <- lm(Engaged ~MonthPaid+TypeMonth, data=games)
fbmodela2 <- lm(Engaged ~Paid+TypeMonth, data=games)
summary(fbmodela2)
sigma(fbmodela2)/mean(games$Engaged)

vbremove <- lm(Engaged ~CatMonth+TypeMonth+WeekHour+MonthPaid, data=games)
summary(vbremove)
sigma(vbremove)/mean(games$Engaged)
#############################################
vbremove2 <- lm(Engaged ~CatMonth+TypeMonth+MonthHour+MonthPaid, data=games)
summary(vbremove2)
sigma(vbremove2)/mean(games$Engaged)
#The change from week hour to monthhour has produced a better model.

#############
#Assessing the model

install.packages('lmtest')
library(lmtest)
bptest(vbremove2)
bptest(vbremove)
bptest(fbmodela2)
plot(vbremove2)
install.packages('ggfortify')
library(ggfortify)

mod <- fortify(vbremove2)
ggplot(mod, aes(x=.fitted, y=.resid))+
  geom_point()
