s=sd(airbnb_normal$bathrooms)
x=mean(airbnb_normal$bathrooms)
airbnb_normal$beds=(airbnb_normal$bathrooms-x)/s
set.seed(3000)

k=10
km.out=kmeans(airbnb_normal[14:31],k,nstart=25)
km.clusters=km.out$cluster

tapply(airbnb$price,km.clusters,mean)
tapply(airbnb$bedrooms,km.clusters,mean)

rn=which(airbnb$bedrooms == 2)
airbnb[rn,]
test=km.clusters[rn]
table(test)