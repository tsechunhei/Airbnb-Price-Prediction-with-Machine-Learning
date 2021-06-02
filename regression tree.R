df=read.csv('airbnb.csv')
summary(df$district)
library(caTools)
set.seed(123)
split=sample.split(df$price,SplitRatio=0.7)
qTrain=subset(df,split==TRUE)
qTest=subset(df,split==FALSE)

library(rpart)
library(rpart.plot)
Tree1=rpart(price~.,data=qTrain,method='anova', minbucket=250)
rpart.plot(Tree1, type=1)
prp(Tree1)


Prediction1 = predict(Tree1, newdata=qTest, type='matrix')
library(forecast)
accuracy(Prediction1, qTest$price)



##########
library(caret)
library(e1071)
set.seed(123)
numFolds = trainControl(method = "cv", number = 10)
cpGrid = expand.grid(cp = seq(0,0.3,0.01))
result = train(price~., qTrain, method = "rpart",
               trControl = numFolds, tuneGrid = cpGrid)
result
plot(result)


set.seed(123)
Tree2=rpart(price ~., data = qTrain,method="anova", cp = 0.01)
rpart.plot(Tree2,type=1)
prp(Tree2)

Prediction2 = predict(Tree2,newdata=qTest, type='matrix')
accuracy(Prediction2,qTest$price)

Tree1$variable.importance
Tree2$variable.importance


mean(df$price)
sd(df$price)
