# -*- coding: utf-8 -*-
"""
Name:Yuchen Zhu
Email:yczhu@bu.edu
Assignment #9
This assignment is about simulating stock returns and price movement to prcie
path-dependent options.
Task 2: Pricing Path-Dependent Options
"""
from a9task1 import MCStockSimulator
import numpy as np
import math

class MCStockOption(MCStockSimulator):
    """This class inherits from MCStockSimulator and calculate the option’s 
    payoff.
    """
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        """The constructor will initialize an object of type MCStockSimulator.
        x: exercise price
        num_trials: the number of trials to run
        """
        super().__init__(s, t, r, sigma, nper_per_year)
        self.x = x
        self.num_trials = num_trials
        
    def __repr__(self):
        """return a well-formatted string representation of MCStockOption 
        object.
        """
        the_string = (f"MCStockOption (s=${self.s:.2f}, "
                      f"x=${self.x:.2f}, "
                      f"t={self.t:.2f}(years), "
                      f"r={self.mu:.2f}, "
                      f"sigma={self.sigma:.2f}, "
                      f"nper_per_year={self.nper}, "
                      f"num_trials={self.num_trials})")
        return the_string
    
    def value(self):
        """return the value of the option"""
        print("Base class MCStockOption has no concrete implementation of "
              ".value().")
        return 0
    
    def stderr(self):
        """return the standard error of the option's value."""
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0
        
class MCEuroCallOption(MCStockOption):
    """inherits from the base class MCStockOption"""
    def __repr__(self):
        """return a well-formatted string representation of MCEuroCallkOption 
        object.
        """
        the_string = (f"MCEuroCallOption (s=${self.s:.2f}, "
                      f"x=${self.x:.2f}, "
                      f"t={self.t:.2f}(years), "
                      f"r={self.mu:.2f}, "
                      f"sigma={self.sigma:.2f}, "
                      f"nper_per_year={self.nper}, "
                      f"num_trials={self.num_trials})")
        return the_string
        
    def value(self):
        """return the value of Euro Call Option"""
        the_trials = np.zeros(self.num_trials)
        for i in range(self.num_trials): #generate the number of trials needed
            st = self.generate_simulated_stock_values()[-1]
            the_trials[i] = max(st - self.x, 0) * np.exp(- self.mu * self.t)
        self.mean = np.mean(the_trials)
        self.stdev = np.std(the_trials)
        return self.mean
    
    def stderr(self):
        """return the degree of accuracy of this estimate"""
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0
        
class MCEuroPutOption(MCStockOption):
    """inherits from the base class MCStockOption"""
    def __repr__(self):
        """return a well-formatted string representation of MCEuroPutOption 
        object.
        """
        the_string = (f"MCEuroPutOption (s=${self.s:.2f}, "
                      f"x=${self.x:.2f}, "
                      f"t={self.t:.2f}(years), "
                      f"r={self.mu:.2f}, "
                      f"sigma={self.sigma:.2f}, "
                      f"nper_per_year={self.nper}, "
                      f"num_trials={self.num_trials})")
        return the_string
        
    def value(self):
        """return the value of Euro Put Option"""
        the_trials = np.zeros(self.num_trials)
        for i in range(self.num_trials): #generate the number of trials needed
            st = self.generate_simulated_stock_values()[-1]
            the_trials[i] = max(self.x - st, 0) * np.exp(- self.mu * self.t)
        self.mean = np.mean(the_trials)
        self.stdev = np.std(the_trials)
        return self.mean
    
    def stderr(self):
        """return the degree of accuracy of this estimate"""
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0

class MCAsianCallOption(MCStockOption):
    """inherits from the base class MCStockOption""" 
    def __repr__(self):
        """return a well-formatted string representation of MCAsianCallOption 
        object.
        """
        the_string = (f"MCAsianCallOption (s=${self.s:.2f}, "
                      f"x=${self.x:.2f}, "
                      f"t={self.t:.2f}(years), "
                      f"r={self.mu:.2f}, "
                      f"sigma={self.sigma:.2f}, "
                      f"nper_per_year={self.nper}, "
                      f"num_trials={self.num_trials})")
        return the_string
        
    def value(self):
        """return the value of Asian Call Option"""
        the_trials = np.zeros(self.num_trials)
        for i in range(self.num_trials): #generate the number of trials needed
            st = np.average(self.generate_simulated_stock_values())
            the_trials[i] = max(st - self.x, 0) * np.exp(- self.mu * self.t)
        self.mean = np.mean(the_trials)
        self.stdev = np.std(the_trials)
        return self.mean
    
    def stderr(self):
        """return the degree of accuracy of this estimate"""
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0
    
class MCAsianPutOption(MCStockOption):
    """inherits from the base class MCStockOption""" 
    def __repr__(self):
        """return a well-formatted string representation of MCAsianPutOption 
        object.
        """
        the_string = (f"MCAsianPutOption (s=${self.s:.2f}, "
                      f"x=${self.x:.2f}, "
                      f"t={self.t:.2f}(years), "
                      f"r={self.mu:.2f}, "
                      f"sigma={self.sigma:.2f}, "
                      f"nper_per_year={self.nper}, "
                      f"num_trials={self.num_trials})")
        return the_string
        
    def value(self):
        """return the value of Asian Put Option"""
        the_trials = np.zeros(self.num_trials)
        for i in range(self.num_trials): #generate the number of trials needed
            st = np.average(self.generate_simulated_stock_values())
            the_trials[i] = max(self.x - st, 0) * np.exp(- self.mu * self.t)
        self.mean = np.mean(the_trials)
        self.stdev = np.std(the_trials)
        return self.mean
    
    def stderr(self):
        """return the degree of accuracy of this estimate"""
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0   

class MCLookbackCallOption(MCStockOption):
    """inherits from the base class MCStockOPtion"""
    def __repr__(self):
        """return a well-formatted string representation of 
        MCLookbackCallOption object.
        """
        the_string = (f"MCLookbackCallOption (s=${self.s:.2f}, "
                      f"x=${self.x:.2f}, "
                      f"t={self.t:.2f}(years), "
                      f"r={self.mu:.2f}, "
                      f"sigma={self.sigma:.2f}, "
                      f"nper_per_year={self.nper}, "
                      f"num_trials={self.num_trials})")
        return the_string
        
    def value(self):
        """return the value of look-back call option"""
        the_trials = np.zeros(self.num_trials)
        for i in range(self.num_trials): #generate the number of trials needed
            st = np.max(self.generate_simulated_stock_values())
            the_trials[i] = max(st - self.x, 0) * np.exp(- self.mu * self.t)
        self.mean = np.mean(the_trials)
        self.stdev = np.std(the_trials)
        return self.mean
    
    def stderr(self):
        """return the degree of accuracy of this estimate"""
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0

class MCLookbackPutOption(MCStockOption):
    """inherits from the base class MCStockOPtion"""
    def __repr__(self):
        """return a well-formatted string representation of 
        MCLookbackPutOption object.
        """
        the_string = (f"MCLookbackPutOption (s=${self.s:.2f}, "
                      f"x=${self.x:.2f}, "
                      f"t={self.t:.2f}(years), "
                      f"r={self.mu:.2f}, "
                      f"sigma={self.sigma:.2f}, "
                      f"nper_per_year={self.nper}, "
                      f"num_trials={self.num_trials})")
        return the_string
        
    def value(self):
        """return the value of look-back put option"""
        the_trials = np.zeros(self.num_trials)
        for i in range(self.num_trials): #generate the number of trials needed
            st = np.min(self.generate_simulated_stock_values())
            the_trials[i] = max(self.x - st, 0) * np.exp(- self.mu * self.t)
        self.mean = np.mean(the_trials)
        self.stdev = np.std(the_trials)
        return self.mean
    
    def stderr(self):
        """return the degree of accuracy of this estimate"""
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0