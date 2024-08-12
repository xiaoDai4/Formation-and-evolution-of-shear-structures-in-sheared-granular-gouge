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
index_former_ = [1420]
index_later_ = [1500]
if len(index_former_) != len(index_later_):
    print('The program terminated!!!\nThe size of \'index_former\' and \'index_later\' is not the same')
    sys.exit()
# each cloumn of particle information are:
# 0 ID, 1 cx, 2, cy, 3 dx, 4 dy, 5 vx, 6 vy, 7 Cxx, 8 Cxy, 9 Cyy


#%% change current directory
os.chdir(os.path.dirname(sys.argv[0]))
# import function
from import_data import *
from calculate_distance import *
from assign_neighbor import *
from calculate_nonaffine_displacement import *

#%% start the calculation
steps_ = len(index_former_)
print('Start NonAffine!')
for i_ in range(steps_):
    # read data
    print('\n-----------------------------------------------------\n')
    ParticleInfo_former_ = read_ParticleInfo(path_ParticleInfo_, index_former_[i_])
    ParticleInfo_later_ = read_ParticleInfo(path_ParticleInfo_, index_later_[i_])
    n_particles_ = ParticleInfo_former_.shape[0]
    # calculate distance
    print('\n-----------------------------------------------------\n')
    c_former_ = ParticleInfo_former_[:,[1,2]] # the coordinate of former particles
    distance_ = calculate_distance(c_former_) 
    # assign neighbor
    print('\n-----------------------------------------------------\n')
    neighbor_ = assign_neighbor(distance_, threshold_)
    # calculate non-affine displacement
    print('\n-----------------------------------------------------\n')
    c_later_ = ParticleInfo_later_[:,[1,2]] # the coordinate of later particles
    nonaffine_ = calculate_nonaffine(c_former_, c_later_, neighbor_) # a vector that store the nonaffine displacement
    # save data
    print('\n-----------------------------------------------------\n')
    np.save('nonaffine_displacement_data/nonaffine_from_%d_to_%d' % \
            (index_former_[i_], index_later_[i_]), nonaffine_)
    print('Save data done')
print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
print('NonAffine saved. ALL DONE.')
    
    