#%% import pakages
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

#%% set parameters
path_FrictionState_ = '../particle_info/particle_info_friction_state.txt'
path_ParticleInfo_ = '../particle_info/particle_info_%d.txt' # note this path need to replace the number
path_HistoryData_ = '../particle_info/history_data.his'
threshold_ = 1 # the plate velocity threshold to select a slip event

#%% change current directory
os.chdir(os.path.dirname(sys.argv[0]))
# import function
from import_data import *

#%% read FrictionState and HistoryData
# table head: 0. Load pointer displacement, 1. Friction, 2. Top plate displacement, 
# 3. Bottom plate displacement, 4. Top plate velocity, 5. Bottom plate velocity
FrictionState_ = read_FrictionState(path_FrictionState_)
# table head: 0. step, 1. displacement, 2. gouge_thickness, 3. shear_strain,
# 4. shear_stress, 5. normal_stress, 6. friction,  7. plate_displacement,
# 8. plate_velocity, 9. plate_displacement_bottom, 10. plate_velocity_bottom,
# 11. shear_strain_rate
HistoryData_ = read_HistoryData(path_HistoryData_)

#%% plot the marked data and friction

# plt.rc('font', family = 'Arial')
# plt.rcParams['font.size'] = 15
# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'
plt.plot(HistoryData_[:, 1],  \
          HistoryData_[:, 6],\
          linewidth = 1, color = 'b')
# plt.scatter(FrictionState_[:, 0],  \
#             FrictionState_[:, 1]\
#               , c = 'r', marker = '*')

plt.axvline(x = FrictionState_[820, 0],  color='teal', ls='--', lw=1)
plt.axvline(x = FrictionState_[860, 0],  color='teal', ls='--', lw=1)
# plt.xlabel('Time (ms)', fontsize = 17)
# plt.ylabel('Polarization ($\\Phi$)', fontsize = 17)
plt.xlim([FrictionState_[0, 0], FrictionState_[40, 0]])
# plt.ylim([0, 0.9])
# y_tick_ = np.arange(0, 1, 0.1)
# plt.yticks(y_tick_)
# plt.savefig('polarization.svg', dpi=600, format='svg')
# plt.show()


# plt.plot(HistoryData_[:, 0],  \
#           HistoryData_[:, 1],\
#           linewidth = 1, color = 'b')

#%%

# plt.rc('font', family = 'Arial')
# plt.rcParams['font.size'] = 15
# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'
plt.plot(HistoryData_[:, 1],  \
          np.absolute(HistoryData_[:, 8] - HistoryData_[:, 10]) / 2,\
          linewidth = 1, color = 'b')
# plt.scatter(FrictionState_[:, 0],  \
#             FrictionState_[:, 1]\
#               , c = 'r', marker = '*')

plt.axvline(x = FrictionState_[108, 0],  color='teal', ls='--', lw=1)
plt.axvline(x = FrictionState_[109, 0],  color='teal', ls='--', lw=1)
# plt.xlabel('Time (ms)', fontsize = 17)
# plt.ylabel('Polarization ($\\Phi$)', fontsize = 17)
plt.xlim([FrictionState_[108, 0], FrictionState_[110, 0]])
# plt.ylim([0, 0.9])
# y_tick_ = np.arange(0, 1, 0.1)
# plt.yticks(y_tick_)
# plt.savefig('polarization.svg', dpi=600, format='svg')
# plt.show()


# plt.plot(HistoryData_[:, 0],  \
#           HistoryData_[:, 1],\
#           linewidth = 1, color = 'b')


#%% detect which area has a slip
index_marked_ = []  # store the index which contain a slip event
slip_velocities_ = []  # store the index velocity
index_historymax_ = [] # store the slip event in history
l_ = int(HistoryData_.shape[0] / FrictionState_.shape[0]) # the length between each index in the history data
for i_ in range(FrictionState_.shape[0]):
    # print(l_ * i_ + l_ - 1)
    t_ = (HistoryData_[(l_ * i_) : (l_ * i_ + l_), 8] -  \
        HistoryData_[(l_ * i_) : (l_ * i_ + l_), 10])/2
    t_ = np.absolute(t_)
    if np.max(t_) > threshold_:
        index_marked_.append(int(i_-1))
        slip_velocities_.append(np.max(t_))
        index_historymax_.append((np.where(t_ == t_.max())[0]) + int(l_ * i_) )
print('The saved variables are \'index_marked_\': save the index which contain a slip event; \n\
                              \'slip_velocities_\': store the index velocity;\n\
                              \'index_historymax_\': store the slip event in history')
print('The index which contain a slip event is:\n')
print(index_marked_)

#%% save some information

filename_ = open('plot_information/index_marked.pkl', 'wb')
pickle.dump(index_marked_, filename_)
filename_.close()

filename_ = open('plot_information/slip_velocities.pkl', 'wb')
pickle.dump(slip_velocities_, filename_)
filename_.close()

filename_ = open('plot_information/index_historymax.pkl', 'wb')
pickle.dump(index_historymax_, filename_)
filename_.close()

print('\nSaving data to directory: plot_information')
print('Done!')