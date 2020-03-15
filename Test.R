library(dplyr)
library(ggplot2)
install.packages("psych")
library(psych)
library(tidyverse)
install.packages('kableExtra')
games <-  read.csv("C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Data for Model.csv",sep=",")
train <- games[1:550,]
test <- games[551:596,]
model1 <- lm(Attendance ~ ., data=train)
summary(model1)
sigma(model1)/mean(train$Attendance)

predict(model1,test,se.fit = TRUE)
pred.w.plim <- predict(model1, test, interval = "prediction")
pred.w.clim <- predict(model1, test, interval = "confidence")
matplot(test$Attendance, cbind(pred.w.clim, pred.w.plim[,-1]))

step(model1, direction = "back", scope = formula(model1))
model2 <- lm(formula = Attendance ~ Tournament + Home.Team + Venue + Away.Table.Position + 
               Away.Last_5_W.L + Rain.Level + Home.Win.Loss.in.Comp + Day.Of.Week + 
               Kick.Off.Hour + Derby + Number.ofEPCR.Wins + Years.sinceP14.Win + 
               Stadium.Age + Wind, data = games)
summary(model2)
sigma(model2)
sigma(model2)/mean(games$Attendance)




