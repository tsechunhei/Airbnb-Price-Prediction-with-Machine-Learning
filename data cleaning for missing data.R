df=read.csv('airbnb with missing values with extreme values without strings.csv')
str(df)

###mice
install.packages("mice")
library(mice)
md.pattern(df)

###visualize missing values
install.packages("VIM")
library(VIM)
mice_plot = aggr(df, col=c('navyblue','yellow'),
                    numbers=TRUE, sortVars=TRUE,
                    labels=names(df), cex.axis=.7,
                    gap=3, ylab=c("Missing data","Pattern"))

###impute missing values
imputed_Data = mice(df, m=5, maxit = 50, method = 'pmm', seed = 100)
summary(imputed_Data)
imputed_Data$imp$review_scores

completeData = complete(imputed_Data,2)
str(completeData)

sd(df$host_total_listings)
sd(completeData$host_total_listings)

densityplot(imputed_Data)

write.csv(completeData, 'airbnb with extreme values without strings.csv')
