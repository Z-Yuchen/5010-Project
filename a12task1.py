# -*- coding: utf-8 -*-
"""
Name:Yuchen Zhu
Email:yczhu@bu.edu
Assignment #12
This assignment is about using some functions to help quantify the risk of an 
investment strategy.
Task 1:Value at Risk
"""
from scipy.stats import norm
import pandas as pd
def compute_model_var_pct(mu, sigma, x, n):
    """return the value at risk
    mu: daily rate of return
    sigma: daily standard deviation of returns
    x: percentage confident of our maximum loss
    n: number of days
    """
    z = norm.ppf(1 - x)
    var = mu * n + z * sigma * n**0.5
    return var

def compute_historical_var_pct(returns, x, n):
    """using historial simulation approach to return the value at risk"""
    returns.sort_values(ascending = True)
    var = returns.iloc[int((1- x) * len(returns)) - 1]
    day_var = var * n**0.5
    return day_var
    
    
    
    
    
    
    