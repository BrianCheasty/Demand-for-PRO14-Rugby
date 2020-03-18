library(dplyr)
library(ggplot2)
install.packages("psych")
library(psych)
library(tidyverse)
install.packages('kableExtra')
#data is Munster Model or Data for Model
games <-  read.csv("C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Data for Model.csv",sep=",")
set.seed(100)
train <- sample(nrow(games),0.8*nrow(games),
                replace=FALSE)
TrainSet <-  games[train,]
ValidSet <- games[-train,]
model1 <- lm(Attendance ~ ., data=TrainSet)
summary(model1)
sigma(model1)
sigma(model1)/mean(games$Attendance)

predict(model1,ValidSet,se.fit = TRUE)
pred.w.plim <- predict(model1, test, interval = "prediction")
pred.w.clim <- predict(model1, test, interval = "confidence")
matplot(test$Attendance, cbind(pred.w.clim, pred.w.plim[,-1]))

step(model1, direction = "back", scope = formula(model1))
model2 <- lm(formula = Attendance ~ Tournament + Home.Team + Venue + Home.Table.Position + 
               Away.Table.Position + Max.Temperature + Rain.Level + Home.Win.Loss.in.Comp + 
               Home.Total.P + Day.Of.Week + Month.of.Year + Kick.Off.Hour + 
               Home.Winning.Percentage + Derby + Years.sinceP14.Win + Years.sinceEPCR.Win + 
               Table.Difference + Uncertainty, data = games)
summary(model2)
sigma(model2)
sigma(model2)/mean(games$Attendance)



#Regression Tree
install.packages(rpart)
library("rpart")
games <-  read.csv("C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Data for Model.csv",sep=",")
train <- games[1:480,]
test <- games[481:560,]
modeltree	<-	rpart(Attendance	~	.,	data	=	train)
library(rpart.plot)
rpart.plot(modeltree,	digits	=	3)
p.rpart	<-	predict(modeltree,	test)
summary(modeltree)
cor(p.rpart,test$Attendance)
MAE	<-	function(actual,predicted){
  mean(abs(actual	-	predicted))
  }
MAE(p.rpart,test$Attendance)
average <-mean(train$Attendance)
MAE(average,test$Attendance)

#Model Tree
install.packages(rWeka)
library(RWeka)
m.m5p	<-	M5P(Attendance	~	.,	data	=	train)
summary(m.m5p)



#Nueral Network
install.packages('neuralnet')
library(neuralnet)
games2 <-  read.csv("C:/Users/bcheasty/OneDrive - Athlone Institute Of Technology/Research Project/Data Set Creation/Data/Feature Creation/Munster2 Model.csv",sep=",")
view(games2)
newdf <- t(na.omit(t(games2)))

normalize	<-	function(x)	{
  return((x	-	min(x))	/	(max(x)	-	min(x)))
}

games_norm	<-	as.data.frame(lapply(games2,	normalize))
new<-games_norm[ , colSums(is.na(games_norm)) == 0]
view(games_norm)
train <- new[1:40,]
test <- new[41:50,]
view(train)
games_model	<-	neuralnet(Attendance	~	.,data	=	train)
plot(games_model)
model_results <- compute(games_model, test)
view(model_results)
predicted_attendance <- model_results$net.result
view(predicted_attendance)
cor(predicted_attendance, test$attendance)
view(predicted_attendance,test$Attendance)

