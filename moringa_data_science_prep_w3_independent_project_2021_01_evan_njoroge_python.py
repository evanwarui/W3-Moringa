

#importing numpy library
import numpy as np

# importing pandas library
import pandas as pd

#Creating a Dataframe from cells geo csv and displaying first 5 items

ds1 = pd.read_csv('cells_geo.csv', delimiter =";")
ds1.head()

#Creating a Dataframe from cells geo description excel file and displaying first 5 items

ds2 = pd.read_excel('cells_geo_description.xlsx')
ds2.head()

#Creating  Dataset3 from CDR description excel file and displaying last 5 items

ds3 = pd.read_excel('CDR_description.xlsx')
ds3.tail()

#Creating  Dataset4 from Telcom_Dataset1 csv file and displaying first 5 items

d_perse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
ds4 = pd.read_csv('Telcom_dataset1.csv', parse_dates=['DATETIME'], date_parser=d_perse)
ds4.head()

#Creating  Dataset5 from Telcom_Dataset2 csv file and displaying last 5 items

d_perse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
ds5 = pd.read_csv('Telcom_dataset2.csv', parse_dates=['DATE_TIME'], date_parser=d_perse)
ds5.head()

#Creating  Dataset6 from Telcom_Dataset3 csv file and displaying first 5 items

d_perse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
ds6 = pd.read_csv('Telcom_dataset2.csv', parse_dates=['DATE_TIME'], date_parser=d_perse)
ds6.head()

#Preaparing to merge Dataset 4,5 and 6 (Meging the three Telkom Datasets)
#Making all the column names uniform - lowercase

ds4.columns = map(str.lower, ds4.columns)
columns = ['product', 'value', 'date_time', 'cell_on_site', 'dw_a_number_int',
'dw_b_number_int', 'country_a', 'country_b', 'cell_id', 'site_id']
ds4.columns = columns

ds5.columns = map(str.lower, ds5.columns)
columns = ['product', 'value', 'date_time', 'cell_on_site', 'dw_a_number_int',
'dw_b_number_int', 'country_a', 'country_b', 'cell_id', 'site_id']
ds5.columns = columns

ds6.columns = map(str.lower, ds6.columns)
columns = ['product', 'value', 'date_time', 'cell_on_site', 'dw_a_number_int',
'dw_b_number_int', 'country_a', 'country_b', 'cell_id', 'site_id']

ds_merged = pd.concat([ds4,ds5,ds6], ignore_index = 1)
ds_merged.tail()

#Cleaning unwanted data on merged dataset: Remoniving country_a , country_b and cell_on_site.

ds_new = ds_merged.drop(columns = ['country_a' , 'country_b' ,'cell_on_site'])
ds_new.tail(11)

ds_new.loc[0, 'date_time'].day_name()

##ds_new

##Cleaning  Dataset1: cells geo csv by removing unwamted column: Unnamed, sites not in service

ds1.loc[ds1['STATUS'] == '', 'STATUS'] = 0
ds1.drop(ds1.index[ds1['STATUS'] == '0'], inplace = True)

ds1

#combining the the 6th dataset with the already merged Telecom datasets
ds_fin= pd.merge(ds_new,ds1,how='inner', left_on="site_id", right_on="SITE_CODE")
ds_fin

#calculating the most used city for the three days?

ds_fin['VILLES'].value_counts().head(20)

val= ds_fin.groupby(['VILLES', 'product'])['value'].sum()
val.head(10)

#calculating Which cities were the most used during business and home hours?
#Asupmtion - Buisness Hours are 8am to 5pm
#assuption  - Home hours are 7am to 8am and also 5pm to 9pm
#date / time Filtering from 7am to 9pm

filt = (ds_fin['date_time'] >= pd.to_datetime('07:00.00') and (ds_fin['date_time']) < pd.to_datetime('21:00.00')
ds_fin.loc[filt]
ds_fin

