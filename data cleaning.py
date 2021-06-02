# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:53:26 2020

@author: Vin
"""


###
import pandas as pd
df=pd.read_csv('airbnb_raw.csv')


###clean unrelated letters for columns
df['price']=df.price.str.replace(r"[$]",'')
df['price']=df.price.str.replace(r"[,]",'')
df['price']=df['price'].astype(str).replace('\.00', '', regex=True)

df['host_response_rate']=df.host_response_rate.str.replace(r"[%]",'')

df['host_acceptance_rate']=df.host_acceptance_rate.str.replace(r"[%]",'')

df['bathrooms']=df.bathrooms.str.replace(r"[a-zA-Z]",'')
df['bathrooms']=df.bathrooms.str.replace(' ','')
df['bathrooms']=df.bathrooms.str.replace('-','')
df['bathrooms']=pd.to_numeric(df.bathrooms, errors='coerce')

df['bathroom_type']=df.bathroom_type.str.replace('\d+', '')
df['bathroom_type']=df.bathroom_type.str.replace(r"[.]",'')
df['bathroom_type']=df.bathroom_type.str.replace('private','')
df['bathroom_type']=df.bathroom_type.str.replace('baths','bath')
df['bathroom_type']=df.bathroom_type.str.replace(' ','')
df['bathroom_type']=df.bathroom_type.str.replace('Sharedhalf-bath','bath')
df['bathroom_type']=df.bathroom_type.str.replace('Half-bath','bath')
df['bathroom_type']=df.bathroom_type.str.replace('Privatehalf-bath','bath')
df['bathroom_type']=df.bathroom_type.str.replace('bath','private')
df['bathroom_type']=df.bathroom_type.str.replace('sharedbath','share')
df['bathroom_type']=df.bathroom_type.str.replace('sharedprivate','share')
df['bathroom_type']=df.bathroom_type.str.replace('private','Private bathroom')
df['bathroom_type']=df.bathroom_type.str.replace('share','Shared bathroom')
df.bathroom_type=df.bathroom_type.fillna('Private bathroom')


###convert variables to numeric
df['price']=pd.to_numeric(df.price, errors='coerce')
df['host_response_rate']=pd.to_numeric(df.host_response_rate, errors='coerce')
df['host_acceptance_rate']=pd.to_numeric(df.host_acceptance_rate, errors='coerce')
df['host_total_listings']=pd.to_numeric(df.host_total_listings, errors='coerce')
df['accommodates']=pd.to_numeric(df.accommodates, errors='coerce')
df['bedrooms']=pd.to_numeric(df.bedrooms, errors='coerce')
df['beds']=pd.to_numeric(df.beds, errors='coerce')
df['reviews']=pd.to_numeric(df.reviews, errors='coerce')
df['review_scores']=pd.to_numeric(df.review_scores, errors='coerce')



###change % to decimal
df['host_acceptance_rate']=df.host_acceptance_rate.div(100)
df['host_response_rate']=df.host_response_rate.div(100)

df.to_csv('airbnb with missing values with extreme values without strings.csv')



###
import pandas as pd
df=pd.read_csv('airbnb with extreme values with strings.csv')
df.isnull().any()


###clear unreasonable price value 
df=df[df.price >= 100]

###IQR plot for price
import seaborn as sns
sns.boxplot(x=df['price'])

###Scatter plot for price vs accomodates
import matplotlib.pyplot as plt
fig, ax=plt.subplots(figsize=(16,8))
ax.scatter(df['price'], df['accommodates'])
plt.show()


###clearing extreme price value using IQR
Q1=df.price.quantile(0.25)
Q3=df.price.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
df=df[~((df.price < (Q1 - 1.5 * IQR))|(df.price > (Q3 + 1.5 * IQR)))]

###clearing extreme values using z score
from scipy import stats
z=stats.zscore(df.price)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]

z=stats.zscore(df.accommodates)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]

z=stats.zscore(df.bathrooms)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]

z=stats.zscore(df.bedrooms)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]

z=stats.zscore(df.beds)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]

z=stats.zscore(df.host_total_listings)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]

z=stats.zscore(df.reviews)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]

z=stats.zscore(df.review_scores)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]

z=stats.zscore(df.host_response_rate)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]

z=stats.zscore(df.host_acceptance_rate)
abs_z=abs(z)
filtered_entries=(abs_z < 3)
df=df[filtered_entries]


###round off
df.host_total_listings=df['host_total_listings'].round(decimals=0)
df.accommodates=df['accommodates'].round(decimals=0)
df.bathrooms=df['bathrooms'].round(decimals=0)
df.bedrooms=df['bedrooms'].round(decimals=0)
df.beds=df['beds'].round(decimals=0)
df.reviews=df['reviews'].round(decimals=0)
df.review_scores=df['review_scores'].round(decimals=0)
df.host_response_rate=df['host_response_rate'].round(decimals=2)
df.host_acceptance_rate=df['host_acceptance_rate'].round(decimals=2)


###
df.to_csv('airbnb.csv')
