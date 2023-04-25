# -*- coding: utf-8 -*-
"""
Name:Yuchen Zhu
Email:yczhu@bu.edu
Assignment #11
This assignment is about backtesting an investment strategy. 
Task 2: Backtesting your own Trading Strategy
"""
import pandas as pd
def mystrategy(symbol):
    """return the strategy to earn the return and backtest."""
    fn = './%s.csv' % symbol
    df = pd.read_csv(fn) 
    df.index = df['Date']
    position = pd.Series(index = df.index, data = 0)
    # Buy 10% if the stock price goes down, sell 10% if the stock price goes up
    for i in range(len(df) - 1):
        if float(df['Change %'].iloc[i][:-1]) > 0:
            position[i+1] = 0.1
        else:
            position[i+1] = -0.1
    df['Signal'] = position
    # 0.25% trading fees on each time buy and sell
    df['Market Return'] = df['Price']/ df['Price'].shift(1) - 1  
    df['Action Return']  = df['Signal'] * df['Market Return'] -0.0025
    df['Abnormal Return'] = df['Action Return'] - df['Market Return']
    df[['Market Return', 'Action Return', 'Abnormal Return']].cumsum().plot(
        title = 'Cumulative Returns')
    mean_rate_return = df['Action Return'].mean()
    stdev_return = df['Action Return'].std()
    acu_return = df['Abnormal Return'].sum()
    the_string = f'Rate of return is {mean_rate_return:.4f}\n'
    the_string += f'standard deviation of returns {stdev_return:.4f}\n'
    the_string += f'cumulative abnormal returns is {acu_return:.2f}'
    print(the_string)
    return df