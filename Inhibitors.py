#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Algorithm for determining the temperature offset caused by inhibitors

The algorithmic framework presented here constitutes a temerature 
offset calculation algorithm, depending on experimentally determined
parameters and local pressure conditions. It follows the general procedure
outlined in https://pubs.acs.org/doi/full/10.1021/acs.jced.6b00146.

    Functions
    ----------
    temperature_offset :
        Calculation of the temperature offset
        
"""
import numpy as np
import time

"""Mapping of constants for salts"""

C_salt = {'NaCl':{1:0.3534,
                  2:1.375/1000,
                  3:2.433/10000,
                  4:4.056/100,
                  5:0.799,
                  6:2.25/10000,
                  'MaxConMol':26.5,
                  'MaxConMass':10,
                  'AAD':1.170},
    'CaCl2':{1:0.193,
                  2:7.580/1000,
                  3:1.953/10000,
                  4:4.253/100,
                  5:1.023,
                  6:2.80/10000,
                  'MaxConMol':40.6,
                  'MaxConMass':10,
                  'AAD':1.390},
    'KCl':{1:0.305,
                  2:6.770/10000,
                  3:8.060/100000,
                  4:3.858/100,
                  5:0.714,
                  6:2.20/100000,
                  'MaxConMol':31.5,
                  'MaxConMass':10,
                  'AAD':1.080},
    }
    
def temperature_offset(self)
