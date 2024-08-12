# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:34:57 2023

@author: daizh
"""
import numpy as np
#%% Screen particles according to x to avoid effects caused by BC
def filter_particles(l_xlim_, u_xlim_, l_ylim_, u_ylim_, c_, v_):
    '''
    l_xlim_ - lower x limit
    u_xlim_ - upper x limit
    l_ylim_ - lower y limit
    u_ylim_ - upper y limit
    c_ - c coodinate
    v_ - corresponding variables
    
    returns:
        cnew_ - the  coodinate in a centain range
        vnew_ - the correspnding coodinate in a certain range
    
    '''
    cnew_, vnew_ = [], [] # initialize
    for i_ in range(c_.shape[0]):
        
        if c_[i_][0] > l_xlim_ and c_[i_][0]  < u_xlim_:
            if c_[i_][1] > l_ylim_ and c_[i_][1]  < u_ylim_:
                cnew_.append(c_[i_][:])
                vnew_.append(v_[i_])

    return np.array(cnew_), np.array(vnew_)  # return handled coodinate and variables.

# cnew_, ynew_ = filter_particles(0.5, 3.5, 0, 2,  x_, y_)
# cnew_, vnew_ = filter_particles(0.5, 3.5, 0, 2, x_, vx_)
