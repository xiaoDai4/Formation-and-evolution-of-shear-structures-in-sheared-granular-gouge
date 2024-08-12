#%% import pakages
import pandas as pd
import numpy as np
import os
import sys
import math

#%% set parameters
path_FrictionState_ = '../particle_info/particle_info_friction_state.txt'
path_ParticleInfo_ = '../particle_info/particle_info_%d.txt' # note this path need to replace the number
path_HistoryData_ = '../particle_info/history_data.his'
threshold_ = 3e-5

#%% define index to be calculated
index_ = [0,500]
# each cloumn of particle information are:
# 0 ID, 1 cx, 2, cy, 3 dx, 4 dy, 5 vx, 6 vy, 7 Cxx, 8 Cxy, 9 Cyy

#%% change current directory
os.chdir(os.path.dirname(sys.argv[0]))
# import function
from import_data import *
from calculate_distance import *
from assign_neighbor import *
from calculate_granular_temperature import *

#%% start the calculation
steps_ = len(index_)
print('Start GranularTemperature!')
for i_ in range(steps_):
    # read data
    print('\n-----------------------------------------------------\n')
    ParticleInfo_ = read_ParticleInfo(path_ParticleInfo_, index_[i_])
    n_particles_ = ParticleInfo_.shape[0]
    # calculate distance
    print('\n-----------------------------------------------------\n')
    c_ = ParticleInfo_[:,[1,2]] # the coordinate of particles
    distance_ = calculate_distance(c_) 
    # assign neighbor
    print('\n-----------------------------------------------------\n')
    neighbor_ = assign_neighbor(distance_, threshold_)
    # calculate granular temperature
    print('\n-----------------------------------------------------\n')
    v_ = ParticleInfo_[:,[5,6]] # the velocity of particles
    granular_temperature_ = calculate_temperature(v_, neighbor_) # a vector that store the nonaffine displacement
    # save data
    print('\n-----------------------------------------------------\n')
    np.save('granular_temperature_data/temperature_at_%d' % \
            (index_[i_]), granular_temperature_)
    print('Save data done')
print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
print('GranularTemperature saved. ALL DONE.')