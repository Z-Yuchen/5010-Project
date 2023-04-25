# -*- coding: utf-8 -*-
"""
Name:Yuchen Zhu
Email:yczhu@bu.edu
Assignment #13
This assignment is about creating and rebalancing a portfolio, analyzing 
portfolio returns. 
Task 2: Efficient Portfolios, Value at Risk, and Drawdown
"""

from a10task2 import *
from a13task1 import *

def comparing_portfolios(symbols):
    """compare the risk and return of investing in an equal-weighted portfolio
    and a mean-variance efficient portfolio
    """
    the_price = get_stock_prices_from_csv_files(symbols)
    target_weight= {}
    for s in symbols:
        target_weight[s] = 1 / len(symbols)
     
    # without rebalancing, compare the equally-weighted and min variance 
    # efficient portfolio
    eq_wo_reb = create_equal_weight_portfolio(the_price)
    ret_eq_wo_reb = eq_wo_reb / eq_wo_reb.shift(1) - 1
    print(ret_eq_wo_reb.describe())
    
    the_variance = np.matrix(get_covariance_matrix(ret_eq_wo_reb))
    final_ret = np.matrix(ret_eq_wo_reb.mean())
    
    min_var_wo_reb = calc_global_min_variance_portfolio(the_variance)

    ret_min_var_wo_reb = calc_portfolio_return(final_ret, min_var_wo_reb)
    stdev_min_var_wo_reb = calc_portfolio_stdev(the_variance, min_var_wo_reb)
    print('The mean return for min variance portfolio: ', 
          f'{ret_min_var_wo_reb:.6f}')
    print('The standard deviation of the reutrn for min variance portfolio: '+\
          f'{stdev_min_var_wo_reb:.6f}')
    
        
    # without rebalancing in 20 days, compare the equally-weighted and min variance 
    # efficient portfolio
    eq_with_reb_20 = rebalance_portfolio(the_price, target_weight, 20)
    ret_eq_with_reb_20 = eq_with_reb_20 / eq_with_reb_20.shift(1) - 1
    print(ret_eq_with_reb_20.describe())
    
    the_variance_20 = np.matrix(get_covariance_matrix(ret_eq_with_reb_20))
    final_ret_20 = np.matrix(ret_eq_with_reb_20.mean())
   