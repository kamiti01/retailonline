import pandas as pd 
import seaborn as sns
dataf= pd.read_csv('onlineretail.csv', encoding= 'ISO-8859-1')
 #understanding the data 
print (dataf.head(10))
print(dataf.shape)
print(dataf.info())
print(dataf.columns)
print(dataf.describe)
print(dataf.isnull().sum())

# calculating the missing values % contribution in DF
df_null = round(100*(dataf.isnull().sum())/len(dataf),2)
print(df_null)

#dropping rows having missing values

dataf = dataf.dropna()
print(dataf.shape)
print(dataf.isnull().sum())

# changing the datatype of customer Id as per business understanding
dataf['CustomerId'] = dataf['CustomerID'].astype(str)

#data preparation
dataf['Amount'] = dataf['Quantity']*dataf['UnitPrice']
data_monitoring = dataf.groupby('CustomerID')['Amount'].sum()
data_monitoring = data_monitoring.reset_index()
print(data_monitoring.head())
# calculate the sales volume and product
data_monitoring = dataf.groupby('Description')['Quantity'].sum().sort_values(ascending= False)
data_monitoring = data_monitoring.reset_index()
print(data_monitoring.head())

# calculate the sales volume and per region

data_monitoring = dataf.groupby('Country')['Quantity'].sum().sort_values(ascending= False)
data_monitoring = data_monitoring.reset_index()
print(data_monitoring.head())

# calculate frequently sold product

data_monitoring = dataf.groupby('Description')['InvoiceNo'].count().sort_values(ascending= False)
data_monitoring = data_monitoring.reset_index()
print(data_monitoring.head())

data_monitoring = dataf.groupby('InvoiceDate')['Quantity'].count().sort_values(ascending= False)
data_monitoring = data_monitoring.reset_index()
print(data_monitoring.head())

#converting the date and time as a value.

dataf['InvoiceDate']= pd.to_datetime(dataf['InvoiceDate'], format = '%m/%d/%Y %H:%M')
print(dataf.head())

#compute the maximum and minimum date to know the last transcation date
max_date = max(dataf['InvoiceDate'])
print(max_date)

min_date = min(dataf['InvoiceDate'])
print(min_date)

# calculate the number of days 
days=max(dataf["InvoiceDate"]) - min(dataf["InvoiceDate"])
print(days)

# changing the min date to 30 days from the max date
date =max_date - pd.Timedelta(days=30)
print(date)

# define start and ending date 
days = max_date-date
print(days)
start_date = '2011-11-09'
end_date = '2011-12-09'
dates_range = pd.date_range(start=start_date, end=end_date)
print(dates_range)

import numpy as np

# calculate the total sales from the data set

total_sales= dataf.groupby(dataf['InvoiceDate'].dt.day)['Amount'].sum().sort_values(ascending= False)
total_sales = total_sales.reset_index()
print(total_sales)
#from sklearn.cluster import KMeans 
#KMeans = KMeans(n_clusters = 4 , max_iter=50)
#KMeans.fit(dataf_df_scale)
