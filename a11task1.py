# -*- coding: utf-8 -*-
"""
Name:Yuchen Zhu
Email:yczhu@bu.edu
Assignment #11
This assignment is about backtesting an investment strategy. 
Task 1: Bollinger Bands and Backtesting a Trading Strategy
"""
import pandas as pd
def create_bollinger_bands(df, window = 21, no_of_std = 1, column_name = ''):
    """Create Bollinger Bands"""
    df2 = pd.DataFrame(index = df['Date'])
    if column_name == '':
        df2['Observation'] = df.iloc[:, 1]         
    else:
        df2['Observation'] =  df[column_name]
    df2['RollingMean'] = df2['Observation'].rolling(window).mean()
    df2['UpperBound'] = df2['RollingMean'] + no_of_std*\
            df2['Observation'].rolling(window).std()
    df2['LowerBound'] = df2['RollingMean'] - no_of_std*\
        df2['Observation'].rolling(window).std()
    return df2

def create_long_short_position(df):
    """evaluate the data elements in the Observation column against 
    the columns UpperBound and LowerBound
    """
    position = pd.Series(index = df.index, data = 0)
    df2 = pd.DataFrame(index = df.index)
    for i in range(len(df)):
        if pd.isna(df['UpperBound'].iloc[i]) == False:
            if df['UpperBound'].iloc[i] < df['Observation'].iloc[i]:
                position[i] = 1
            if df['Observation'].iloc[i] < df['LowerBound'].iloc[i]:
                position[i] = -1
    df2['Position'] = position
    return df2

def calculate_long_short_returns(df, position, column_name = ''):
    """returns an object containing the columns
    ['Market Return', 'Strategy Return', and 'Abnormal Return']"""
    df2 = pd.DataFrame(index = df.index)
    if column_name == '':
        df2['Market Return'] = df.iloc[:, 1]/ df.iloc[:, 1].shift(1) - 1        
    else:
        df2['Market Return'] = df[column_name]/ df[column_name].shift(1) - 1
    pd.to_datetime(df2.index)
    df2['Strategy Return']  = position['Position'] * df2['Market Return'] 
    df2['Abnormal Return'] = df2['Strategy Return'] - df2['Market Return']
    return df2
 
def plot_cumulative_returns(df):
    """create a plot of the cumulative return for each column"""
    df[['Market Return', 'Strategy Return', 'Abnormal Return']].cumsum().plot()
