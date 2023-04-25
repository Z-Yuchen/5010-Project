# -*- coding: utf-8 -*-
"""
Name:Yuchen Zhu
Email:yczhu@bu.edu
Assignment #10
This assignment is about using numpy, matplotlib, and pandas packages to 
perform operations on financial datasets.
Task 2: Efficient Portfolios and the Efficient Frontier
"""

import numpy as np
import pandas as pd
def calc_portfolio_return(e, w):
    """return the portfolio return for a portfolio of n>=2 assets.
    e: a matrix of expected returns for the assets
    w: a matrix of portfolio weights of the assets
    """
    return float(e * w.T)

def calc_portfolio_stdev(v, w):
    """return the portfolio standard deviation for a portfolio of n>= 2 assets.
    v: a matrix of covariances among the assets
    """
    return float(w * v * w.T)**0.5

def calc_global_min_variance_portfolio(v):
    """return the portfolio weights corresponding to the global minimum 
    variance portfolio."""
    ctemp = np.ones(len(v)) * v.I * np.matrix(np.ones(len(v))).T
    sigma_min = 1 / ctemp
    return sigma_min * np.ones(len(v)) * v.I

def calc_min_variance_portfolio(e, v, r):
    """return the portfolio weights corresponding to the min_variance_portfolio
    for rate r
    """
    ones = np.matrix(np.ones(len(v)))
    atemp = ones * v.I * e.T
    btemp = e * v.I * e.T
    ctemp = ones * v.I * ones.T
    det = np.matrix([[float(btemp),float(atemp)], [float(atemp),float(ctemp)]])
    determinant = np.linalg.det(det)
    g = 1 / determinant * (btemp * ones- atemp * e) * v.I
    h = 1 / determinant * (ctemp * e - atemp * ones) * v.I
    return g + h * r

def calc_efficient_portfolios_stdev(e, v, rs):
    """ returns the standard deviations of minimum variance portfolios.
        v: a matrix of covariances among the assets.
        rs: rates of return for which to calculate 
        the corresponding minimum variance portfolio’s standard deviation
    """
    the_sigmas = []
    # loop to devlop the efficient portfolios that correspond to the series of 
    # rates of return 
    for i in rs:
        w = calc_min_variance_portfolio(e, v, i) # the min_variance portfolio
        stdev = calc_portfolio_stdev(v, w)
        the_sigmas.append(stdev)
        the_list = str(w)
        print (f"r = {i:.4f}, sigma = {stdev:.4f} w = " + the_list)
    return np.array(the_sigmas)

def get_stock_prices_from_csv_files(symbols):
    """retrn pands.DataFrame object containing historical stock prices for 
    several stocks.
    """
    prices = pd.DataFrame()
    fn = './%s.csv' % symbols[0]
    df = pd.read_csv(fn)
    prices.index = df['Date']
    for symbol in symbols:
        fn = './%s.csv' % symbol
        df = pd.read_csv(fn)
        df.index = df['Date']
        prices[symbol] = df['Adj Close']    
    return prices
        
def get_stock_returns_from_csv_files(symbols):
    """return pandas.DataFrame object containing stock returns"""
    prices = get_stock_prices_from_csv_files(symbols)
    return prices/prices.shift(1) - 1
    
def get_covariance_matrix(returns):
    """get a covariance matrix for the stock returns"""
    return returns.cov()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        