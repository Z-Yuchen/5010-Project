# -*- coding: utf-8 -*-
"""
Name:Yuchen Zhu
Email:yczhu@bu.edu
Assignment #12
This assignment is about using some functions to help quantify the risk of an 
investment strategy.
Task 2: Quantifying Investment Risk: Drawdown
"""
import pandas as pd
from a9task1 import MCStockSimulator
import numpy as np
def compute_drawdown(prices):
    """return dataframe that shows price, prev_max: peak price,
    dd_dollars: drawdown, dd_pct: percentage decline since peak price
    """
    df = pd.DataFrame(index = prices.index)
    prev_max = pd.Series(index = prices.index)
    df['price'] = prices
    #loop to find the previous maximum price
    max_price = df['price'].iloc[0]
    for i in range(len(df)):
        if df['price'].iloc[i] > max_price:
            max_price = df['price'].iloc[i]
        prev_max[i] = max_price
    df['prev_max'] = prev_max
    df['dd_dollars'] = df['prev_max'] - df['price']
    df['dd_pct'] = df['dd_dollars'] / df['prev_max']
    return df

def plot_drawdown(df):
    """draw two charts that contains the historical and maximum prices, and 
    the drawdown since previous maximum price
    """
    df[['price', 'prev_max']].plot(title = 'Price and Previous Maximum')
    df[['dd_pct']].plot(title = 'Drawdown Percentage')
    
def run_mc_drawdown_trials(init_price, years, r,sigma, trial_size, num_trials):
    """run num_trials on the MCstocksimulator to calculate the maximum 
    drawdown on each trial
    """
    max_dd = []
    #loop to create number of trials of stock simulation
    for i in range(num_trials):
        the_trial = MCStockSimulator(init_price, years, r, sigma, trial_size).\
            generate_simulated_stock_values()
        max_price = the_trial[0]
        drawdown = 0
        for j in the_trial: #loop to find maximum drawdown for each trial
            if j > max_price:
                max_price = j
            if (max_price - j)/max_price > drawdown:
                drawdown = (max_price - j)/max_price
        max_dd.append(drawdown)
    return pd.Series(max_dd)