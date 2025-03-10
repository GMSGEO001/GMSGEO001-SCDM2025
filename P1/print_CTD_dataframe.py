#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 14:26:46 2025

@author: georginagomes
"""

import pandas as pd

ctd_data_with_headers = pd.read_csv('./P1_assignment/20081129_0652_CTD_data.dat', names=['Date', 'Time', 'Depth (m)', 'Temperature (celsius)', 'Salinity (psu)'], delimiter='\t')

ctd_dataframe = pd.DataFrame(ctd_data_with_headers)

print(ctd_dataframe)