airbnb = read.csv("airbnb.csv")
set.seed(88)
RF500 = randomForest (price~., data = airbnb , ntree = 500)
RF1000 = randomForest (price~., data = airbnb , ntree = 1000)
RF2000 = randomForest (price~., data = airbnb , ntree = 2000)


print(mtry)

actualRF = randomForest(price ~. , data = airbnb, ntree = 1000, mtry = 6)
print(actualRF)