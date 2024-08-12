#%% import pakages
import pandas as pd
import numpy as np


#%% define read in friction state mark
def read_FrictionState(path_):
    print('\nReading friction state...\n')
    t_ = pd.read_table(path_, delimiter = ',')
    print(t_.columns)
    print('\nRead friction state successful\n')
    return t_.to_numpy()




#%% define read in history data
def read_HistoryData(path_):
    print('\nReading history data...\n')
    with open(path_) as f_:
        print(f_.readline())
    t_ = pd.read_table(path_, skiprows= 2, header = None, delimiter = '\s+')
    
    print('\nRead history data successful\n')
    return t_.to_numpy()



#%% define read in particle info
def read_ParticleInfo(path_, number_):
    print('\nReading particle info %d...' % number_)
    t_ = pd.read_table(path_ % number_, delimiter = ',')
    print(t_.columns)
    print('\nRead particle info %d successful' % number_)
    return t_.to_numpy()

