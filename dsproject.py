import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

df = pd.read_csv("911.csv")
#print(df.info())
#print(df.head())
#print(df.tail())
#top five zip codes
#print(df['zip'].value_counts().head(5))
#top five township
#print(df["twp"].value_counts().head(5))
#take a look "title" coulmn .how many unique codes are there
#print(df['title'].nunique())
#we create a reason column to separate new column that contains string value not departments
df["Reason"]=df["title"].apply(lambda title : title.split(':')[0])
#print(df["Reason"])
#top 3 reasons for 911 calls
#print(df["Reason"].value_counts())
#Data visulasize
# countplot for reason
#sns.countplot(x = "Reason",data = df)
#plt.show()
#datatype of timestamp
#print(np.dtype(df["timeStamp"]))
#print(df["timeStamp"].head())
#To create 3 columns in timestamp date,time,hour
#dummy = df["timeStamp"].iloc[0]
#print(dummy.hour)
#countplot for title  with
#sns.countplot(x ="title",data = df)
#plt.show()
#groupby the month.group the month column and use count(),use head return
#print(df["timeStamp"])
#Month = df["Month"] = df["timeStamp"].apply(lambda timeStamp: timeStamp.split("-")[1])
#print(df["Month"])
#bymonth = df.groupby("Month").count()
#print(bymonth.head())
#sns.lmplot(x='Month',y='twp',data = df )
#plt.show()
