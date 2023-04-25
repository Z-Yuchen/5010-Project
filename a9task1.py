# -*- coding: utf-8 -*-
"""
Name:Yuchen Zhu
Email:yczhu@bu.edu
Assignment #9
This assignment is about simulating stock returns and price movement to prcie
path-dependent options.
Task 1: Simulating Stock Returns
"""
import numpy as np
import matplotlib.pyplot as plt

class MCStockSimulator:
    """This class simulates stock returns and values"""
    def __init__(self, s, t, mu, sigma, nper_per_year):
        """The constructor will initialize an object of type MCStockSimulator.
        s： the current stock price
        t: the option maturity time
        mu: the annualized rate of return
        sigma: the annualized standard deviation of returns
        nper_per_year: the number of discrete time periods per year
        """
        self.s = s
        self.t = t
        self.mu = mu
        self.sigma = sigma 
        self.nper = nper_per_year        
        
    def __repr__(self):
        """Return a well-formatted string representation of MCStockSimulator 
        object.
        """
        the_string = (f"MCStockSimulator (s=${self.s:.2f}, "
                      f"t={self.t:.2f}(years), "
                      f"mu={self.mu:.2f}, "
                      f"sigma={self.sigma:.2f}, "
                      f"nper_per_year={self.nper})")
        return the_string
    
    def generate_simulated_stock_returns(self):
        """return a np.array containing a sequence of stock 
        returns over the time period t
        """
        z = np.random.normal(size = int(self.nper * self.t))
        rate_of_return = (self.mu - self.sigma**2 / 2) * (1/self.nper) +\
        z * self.sigma * (1/self.nper)**(1/2)
        return rate_of_return
    
    def generate_simulated_stock_values(self):
        """return a np.array containing a sequence of stock values
        """
        prev_s = self.s
        rate_of_return = self.generate_simulated_stock_returns()
        stock_value = np.array([prev_s])
        #produce the stock value corresponding to the return
        for i in rate_of_return: 
            cur_value = prev_s * np.exp(i)
            stock_value = np.append(stock_value, cur_value)
            prev_s = cur_value
        return stock_value
        
        
    def plot_simulated_stock_values(self, num_trials = 1):
        """generate a plot of series of simulated stock returns"""    
        year_nper = np.array(range(self.nper * self.t + 1)) / self.nper
        # produce the plot with num_trials lines.
        for i in range(num_trials):
            stock_value = self.generate_simulated_stock_values()                
            plt.plot(year_nper, stock_value)
        plt.xlabel("years")
        plt.ylabel("$ value")
        plt.title(f"{num_trials} simulated trials")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
