#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:29:25 2025

@author: georginagomes
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sa_agulhas_ship_log_data = pd.read_csv('../../Downloads/SAA2_WC_2017_metocean_10min_avg.csv')
sa_agulhas_ship_log_dataframe = pd.DataFrame(sa_agulhas_ship_log_data)

#index data frame using 'TIME_SERVER' date time column
sa_agulhas_ship_log_dataframe['TIME_SERVER'] = pd.to_datetime(sa_agulhas_ship_log_dataframe['TIME_SERVER'], format="%Y/%m/%d %H:%M")
print(sa_agulhas_ship_log_dataframe.dtypes)
sa_agulhas_ship_log_dataframe.set_index('TIME_SERVER', inplace=True)
sa_agulhas_ship_log_dataframe = sa_agulhas_ship_log_dataframe.sort_index()

#check values
print(sa_agulhas_ship_log_dataframe)
print(sa_agulhas_ship_log_dataframe.isna())
print(sa_agulhas_ship_log_dataframe[sa_agulhas_ship_log_dataframe.isna().any(axis=1)])


departure_date_time = pd.to_datetime("2017/06/28 17:10")
#could have been any time on day of 4th, we don't know
arrival_date_time = pd.to_datetime("2017/07/04 23:59")
departure_to_arrival_data = sa_agulhas_ship_log_dataframe[(sa_agulhas_ship_log_dataframe.index>=departure_date_time) & (sa_agulhas_ship_log_dataframe.index<=arrival_date_time)]
 
print(departure_to_arrival_data)

#temperature time series 
fig = plt.figure(figsize=(8,6))
plt.plot(departure_to_arrival_data.index, departure_to_arrival_data['TSG_TEMP'])
plt.title("Time series of Sea Surface Temperature recorded between 2017/06/28-2017/07/14 on SA Agulhas II cruise of Southern Ocean")
plt.xlabel("Time")
plt.ylabel("Sea Surface Temperature (degrees C)")
plt.style.use('grayscale')
plt.xticks([pd.to_datetime("2017/06/28 17:10"), pd.to_datetime("2017/07/04 23:50")], ["2017/06/28", "2017/07/04"])
plt.show()
fig.savefig("temperature_time_series.png", bbox_inches='tight')
 

#histogram of salinity 
fig = plt.figure(figsize=(8,6))
plt.hist(departure_to_arrival_data['TSG_SALINITY'], bins=10, range=(30,35))
plt.title("Salinity distribution recorded between 2017/06/28-2017/07/14 on SA Agulhas II cruise of Southern Ocean")
plt.xlabel('Salinity (psu)')
plt.ylabel("Frequency")
plt.show()
fig.savefig("salinity_distribution.png", bbox_inches='tight')

#mean & standard deviation of temperature and salinity presented in table
temperature_column = departure_to_arrival_data['TSG_TEMP']
temperature_mean = temperature_column.mean()
temperature_standard_deviation = temperature_column.std()
temperature_first_quartile = temperature_column.quantile(0.25)
temperature_third_quartile = temperature_column.quantile(0.75)
temperature_interquartile_range = temperature_third_quartile - temperature_first_quartile

salinity_column = departure_to_arrival_data['TSG_SALINITY']
salinity_mean = salinity_column.mean()
salinity_standard_deviation = salinity_column.std()
salinity_first_quartile = salinity_column.quantile(0.25)
salinity_third_quartile = salinity_column.quantile(0.75)
salinity_interquartile_range = salinity_third_quartile - salinity_first_quartile

temperature_salinity_stats = {'Variable':['Sea Surface Temperature (degrees C)', 'Salinity (psu)'],
                              'Mean':[temperature_mean, salinity_mean],
                              'Standard Deviation': [temperature_standard_deviation, salinity_standard_deviation],
                              'Interquartile Range': [temperature_interquartile_range, salinity_interquartile_range]
                               }
temperature_salinity_stats_dataframe = pd.DataFrame(temperature_salinity_stats)
 
fig = plt.figure()
table = plt.table(cellText=temperature_salinity_stats_dataframe.values, colLabels=temperature_salinity_stats_dataframe.columns, cellLoc="center", loc="center")
table.scale(3, 4)
table.set_fontsize(14)
plt.axis('off')
fig.suptitle("Temperature and Salinity statistics for data recorded between 2017/06/28-2017/07/14 on SA Agulhas II cruise of Southern Ocean")
plt.show()
fig.savefig('temperature_salinity_stats_table.png', dpi=300, bbox_inches='tight')
 
 
#decimal degrees conversion function 
def ddmm2dd(ddmm):   
     """     
     Converts a position input from degrees and minutes to degrees and decimals     
     Input is ddmm.cccc and output is dd.cccc     
     Note, it does not check if positive or negative (but all points are in southern ocean
                                                      so all are negative)    
     """     
     thedeg = np.floor(ddmm/100.)     
     themin = (ddmm-thedeg*100.)/60.     
     return thedeg+themin
 
#scatter plot of wind data 
fig = plt.figure(figsize=(8,6))
plt.scatter(departure_to_arrival_data['AIR_TEMPERATURE'], departure_to_arrival_data['WIND_SPEED_REL'], c=departure_to_arrival_data['LATITUDE'].apply(ddmm2dd), cmap="coolwarm_r")
plt.title('Air Temperature vs Relative Wind Speed recorded between 2017/06/28-2017/07/14 on SA Agulhas II cruise of Southern Ocean')
plt.xlabel('Air Temperature (degrees C)')
plt.ylabel('Relative Wind speed (m/s)')
plt.show()
fig.savefig('air_temperature_vs_relative_wind_speed_scatterplot.png', dpi=300, bbox_inches='tight')





