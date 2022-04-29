# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:51:11 2020

@author: Mahsa
Homework 5
"""

import numpy as np
import pandas as pd

df=pd.read_csv("D:/Old_Data/math/Data science toseeh/Files/digi2.csv",encoding='UTF-8')

#1
df.columns
#df["ID_Order"].head()
#df.iloc[:0].head()
df.describe(include="all")

#2
np.sum(df.isna())

#3
df.drop(labels="Amount_Gross_Order",axis=1,inplace=True)
df.columns

#4
df.drop_duplicates(inplace=True)
len(df.index)

#5
df["DateTime_CartFinalize"]=df["DateTime_CartFinalize"].agg(pd.Timestamp)
df.loc[1,"DateTime_CartFinalize"].day_name()
df.loc[1,"DateTime_CartFinalize"].dayofweek

#JalaliDate
from persiantools.jdatetime import JalaliDate
JalaliDate(pd.Timestamp("1/17/2020"))
JalaliDate(pd.Timestamp('1/6/2020')).year
JalaliDate(pd.Timestamp('1/6/2020')).month
JalaliDate(pd.Timestamp('1/6/2020')).day
df["DateTime_CartFinalize"].agg(JalaliDate)
#be jaye taghir tarikh be shmsi yek sotoone shamsi gozashtam ke dade taghir nakone.
 
#6
def ghadim_jadid(x):
    x=pd.Timestamp(x)
    baze=(x.now()-x).days
    return(baze)
fasele=df["DateTime_CartFinalize"].agg(ghadim_jadid)    
df["DateTime_CartFinalize"][fasele==fasele.max()]
df["DateTime_CartFinalize"][fasele==fasele.min()]

#7
np.unique(df["ID_Item"])
len(np.unique(df["ID_Item"]))
#95232
len(np.unique(df["ID_Customer"]))
#151634

#8
len(np.unique(df["city_name_fa"]))
#906

#9

city=df.groupby("city_name_fa").agg({"ID_Order":["count"]})
sort=city.sort_values(("ID_Order","count"),ascending=False)
sort.head(20)

#10
def yearfunction(x):
    y=pd.Timestamp(x).year
    return(y)

df["Year"]=df["DateTime_CartFinalize"].agg(yearfunction)

yeargroup=df.groupby("Year").agg({"ID_Order":["count"]})
sortyear=yeargroup.sort_values(("ID_Order","count"),ascending=False)
sortyear.head(20)

#11
year_city=df.groupby(["city_name_fa","Year"]).count()["ID_Order"]
year_city.get("تهران")
year_city.get("اصفهان")

#12
np.unique(df.iloc[:,5])
df.iloc[:,5].value_counts().head(20).index


#13
#???????????????????????????????????????????????????????
s=df.groupby("city_name_fa")["Quantity_item"]
np.unique(s.get_group("مشهد"))
np.unique(s.get_group("رشت"))



#14
syear=df.groupby("Year")["Quantity_item"]
np.unique(syear.get_group(2018))
#15
customer_order=df.groupby("ID_Customer").agg({"ID_Order":["count"]})
customer_order.get_value(466132,("ID_Order","count"))
#16
df["ID_Item"].value_counts(ascending=False).head(20).index

#17
Top=df.groupby('city_name_fa')["ID_Item"].value_counts(ascending=False).head()
#in dastoor moshkeli ke dare ine ke aval baraye har shahr va har id item tedade an ra mishomarad.
#pas agar tehran faghat daraye 2 id item a va b ba tedade 3 va 4 bashad,
#darim   tehran-a:3 va tehran-b:4. be hamin sorat baraye shahrhaye digar. 
#hal agar head# begirim az roye satr ha pish mire va momkene maslan beshe tehran_a:3, tehran_b:4, abadan:c:1....
#pas ebteda bayad begim masalan hame tehran(ya ye shahr dige) ha ra jam kon va hala head anha ra bede.
#baraye inke farakhani konim bayad ye data frame besazim. ama chon nazire bazi shahrha chand meghdar darim beja data frame mishe dictionary.

b=dict()

for i in np.unique(df['city_name_fa']):
    b[i]=df.groupby('city_name_fa').get_group(i)["ID_Item"].value_counts(ascending=False).index[:5]
    

b["تهران"]
b["محمود آباد"]

