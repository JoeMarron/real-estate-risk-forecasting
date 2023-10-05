# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:53:20 2023

@author: joema
"""

import pandas as pd
from datetime import datetime

# load HPI data

class HPI_data:
    
    def __init__(self, hpi_filename, region_lkp_filename):
        
        self.hpi = pd.read_csv(hpi_filename)
        self.region_lkp = pd.read_csv(region_lkp_filename)
    
    def get_data(self):
     
        self.hpi = self.hpi[['Date', 'RegionName',
                'AveragePrice','DetachedPrice', 'SemiDetachedPrice', 'TerracedPrice', 'FlatPrice']]
    
    
        # adjust data types
        self.hpi['Date'] = pd.to_datetime(self.hpi['Date'])
        self.hpi['Date'] = self.hpi['Date'].apply(lambda x: datetime.strftime(x, '%Y-%d-%m'))
        self.hpi['Date'] = pd.to_datetime(self.hpi['Date'])
        
        self.hpi['AveragePrice'] = pd.to_numeric(self.hpi['AveragePrice'])
        self.hpi = self.hpi.astype({'AveragePrice': 'float64',
                          'DetachedPrice': 'float64',
                          'SemiDetachedPrice': 'float64',
                          'TerracedPrice': 'float64',
                          'FlatPrice': 'float64'})
    
    
        # filter for 1995-2022
        self.hpi = self.hpi[(self.hpi['Date'] >= '1995-01-01') & (self.hpi['Date'] <= '2022-12-31')]
    
        # filter for given regions
        county_lkp = list(self.region_lkp["GOR10NM"].unique())[:-1]
        county_lkp += ['England']
        self.hpi = self.hpi[self.hpi['RegionName'].isin(county_lkp)]
        
        return self
    
    def get_property_dfs(self):
        
        average_price_df = self.hpi[['Date', 'RegionName', 'AveragePrice']]
        average_price_df = average_price_df.pivot_table(values='AveragePrice',
                                                        index='Date', columns='RegionName', aggfunc='first')
        
        
        detached_price_df = self.hpi[['Date', 'RegionName', 'DetachedPrice']]
        detached_price_df = detached_price_df.pivot_table(values='DetachedPrice',
                                                          index='Date', columns='RegionName', aggfunc='first')
        
        semidet_price_df = self.hpi[['Date', 'RegionName', 'SemiDetachedPrice']]
        semidet_price_df = semidet_price_df.pivot_table(values='SemiDetachedPrice',
                                                        index='Date', columns='RegionName', aggfunc='first')
        
        terraced_price_df = self.hpi[['Date', 'RegionName', 'TerracedPrice']]
        terraced_price_df = terraced_price_df.pivot_table(values='TerracedPrice',
                                                          index='Date', columns='RegionName', aggfunc='first')
        
        flat_price_df = self.hpi[['Date', 'RegionName', 'FlatPrice']]
        flat_price_df = flat_price_df.pivot_table(values='FlatPrice',
                                                  index='Date', columns='RegionName', aggfunc='first')
        
        return average_price_df, detached_price_df, semidet_price_df, terraced_price_df, flat_price_df
    
    
    def get_hpi_returns(dfs:list):
        
        if isinstance(dfs, list):
            
            output_dfs = []
            for df in dfs:
                output_dfs.append(df.pct_change().dropna())
                
        else:
            raise TypeError('Incorrect input formats: Expected list, Recieved %s.' % dfs.type)
            
        return output_dfs
    

if __name__ == "__main__":
    
    filename = 'UK-HPI-full-file-2023-03.csv'
    region_lkp = 'Ward_to_Local_Authority_District_to_County_to_Region_to_Country_Lookup_in_United_Kingdom.csv'
    hpi = HPI_data(filename, region_lkp)
    print(hpi.get_data().get_property_dfs())