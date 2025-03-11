#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 14:26:46 2025

@author: georginagomes
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ctd_data_with_headers = pd.read_csv('../../Documents/AOS/P1_assignment/20081129_0652_CTD_output.csv')

ctd_dataframe = pd.DataFrame(ctd_data_with_headers)


fig, axes = plt.subplots(nrows=1,ncols=2, sharey=True)

depth_column = ctd_dataframe['Depth (m)']
reversed_temperature_column = ctd_dataframe['Temperature (celsius)'][::-1]
reversed_depth_column = depth_column[::-1]
reversed_salinity_column = ctd_dataframe['Salinity (psu)'][::-1]

axes[0].plot(reversed_temperature_column, reversed_depth_column, color='blue')

axes[1].plot(reversed_salinity_column, reversed_depth_column, color='red')

axes[0].invert_yaxis()
axes[1].invert_yaxis()
axes[0].set_ylim(max(depth_column), 0) 
axes[1].set_ylim(max(depth_column), 0) 


axes[0].set_xlabel("Temperature (degrees C)", color='blue')
axes[1].set_xlabel("Salinity (psu)", color='red')

axes[0].set_ylabel('Depth (m)')

fig.suptitle("Temperature and Salinity Depth Profiles for data collected from CTD on 29/11/2008 at 06:52")

plt.show()

fig.savefig('CTD_20081129_Temp_Salinity_graph', bbox_inches='tight')


