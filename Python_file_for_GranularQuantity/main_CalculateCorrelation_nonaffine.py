#%% import pakages
import pandas as pd
import numpy as np
import os
import sys
import math

#%% set parameter
file_names_ = ['nonaffine_displacement_data/nonaffine_from_0_to_40.npy',
               'nonaffine_displacement_data/nonaffine_from_60_to_100.npy',
               'nonaffine_displacement_data/nonaffine_from_100_to_140.npy',
               'nonaffine_displacement_data/nonaffine_from_820_to_860.npy']  # file name to imported
# the coordinate of particles to import
index_ = [0, 60, 100, 820]

a_ = 2.5e-5

r_ = np.linspace(0, 25e-5, 30)  # mutual distance to be calculated

# define the range of particles we concerned
l_xlim_ = 0.5e-3
u_xlim_ = 3.5e-3
l_ylim_ = 1e-3
u_ylim_ = 3e-3

path_FrictionState_ = '../particle_info/particle_info_friction_state.txt'
path_ParticleInfo_ = '../particle_info/particle_info_%d.txt' # note this path need to replace the number
path_HistoryData_ = '../particle_info/history_data.his'

#%% change work directory
os.chdir(os.path.dirname(sys.argv[0]))
# import function
from import_data import *
from calculate_distance import *
from calculate_correlation import *
from filter_particles import *


#%% correlation
steps_ = len(file_names_)
print('Start Correlation!')
for i_ in range(steps_):
    # import data 
    print('\n-----------------------------------------------------\n')
    ParticleInfo_ = read_ParticleInfo(path_ParticleInfo_, index_[i_])
    n_particles_ = ParticleInfo_.shape[0]
    values_ = np.load(file_names_[i_])
    print('\nRead %s\n' % file_names_[i_])
    
    # filter particles
    c_ = ParticleInfo_[:,[1,2]] # the coordinate of particles
    c_filtered_, v_filtered_ = filter_particles(l_xlim_, u_xlim_, l_ylim_, u_ylim_, c_, values_)
    
    # distance
    print('\n-----------------------------------------------------\n')
    
    distance_ = calculate_distance(c_filtered_) 
    
    # calculate correlation
    print('\n-----------------------------------------------------\n')
    correlation_ = calculate_correlation(distance_, v_filtered_, r_, a_)
    
    # save data
    print('\n-----------------------------------------------------\n')
    correlation_ = np.vstack([r_, correlation_])
    # correlation_: row 0, i.e. correlation_[0, :] is the prescribed mutual distance
    # correlation_: row 1, i.e. correlation_[1, :] is the prescribed mutual distance
    np.save('correlation_data/correlation_of_%s' % os.path.basename(file_names_[i_]), correlation_)
    
    print('Save data done')
print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
print('Correlation saved. ALL DONE.')