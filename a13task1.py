# -*- coding: utf-8 -*-
"""
Name:Yuchen Zhu
Email:yczhu@bu.edu
Assignment #13
This assignment is about creating and rebalancing a portfolio, analyzing 
portfolio returns. 
Task 1: Portfolio Construction and Rebalancing
"""
import pandas as pd

def create_equal_weight_portfolio(df_prices, initial_value = 1):
    """return a dataframe containing the values of investment in each of the 
    assets and the value of the total portfolio
    """
    no_columns = len(df_prices.columns)
    df = pd.DataFrame(index = df_prices.index,
                      data = df_prices.values, columns = df_prices.columns)
    #loop to change the price to weight
    for i in range(no_columns):
        init_price = df.iloc[0, i]
        df.iloc[:, i] = df.iloc[:, i]/ init_price / no_columns * initial_value
    df['portfolio'] = df.sum(axis = 1)
    return df


def plot_relative_weights_over_time(df_values):
    """create a plot showing the weights of each asset"""
    for i in range(len(df_values.columns)-1):
        df_values.iloc[:, i].plot()
        
def rebalance_portfolio(df_prices, target_weights, rebalance_freq, 
                        initial_value = 1):
    """return a dataframe with columns containing the values in each asset 
    according to the target weights with rebalancing frequency
    """
    df = df_prices/ df_prices.shift(1) - 1
    df2 = pd.DataFrame(index = df_prices.index, columns = df_prices.columns)
    no_columns = len(df_prices.columns)   
    #loop to change the price to weight
    df2['portfolio'] = df.sum(axis = 1)
    df2['portfolio'].iloc[0] = initial_value
    #loop to set the first row
    for i in range(no_columns):
        the_weight = target_weights[df2.columns[i]]
        df2.iloc[0, i] = initial_value * the_weight
    
    #loop to run the rest rows
    for j in range(1, len(df_prices)): 
        # calculate the weight using returns
        if j != j // rebalance_freq * rebalance_freq: 
            for i in range(no_columns):
                df2.iloc[j, i] = df2.iloc[j-1, i] * (1 + df.iloc[j, i])
            df2['portfolio'].iloc[j] = df2.iloc[j, :-1].sum()
        else: # the row that need rebalancing
            row_sum = 0
            for i in range(no_columns):
                row_sum += df2.iloc[j-1, i] * (1 + df.iloc[j, i])
            df2['portfolio'].iloc[j] = row_sum
            for i in range(no_columns):
                df2.iloc[j, i] = target_weights[df2.columns[i]] * \
                    df2['portfolio'].iloc[j]     
    return df2
