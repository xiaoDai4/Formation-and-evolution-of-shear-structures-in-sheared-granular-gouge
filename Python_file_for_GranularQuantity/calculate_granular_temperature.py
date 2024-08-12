import numpy as np
import math
def calculate_temperature(v_, neighbor_):
    '''
    The theory of this function refer to airticle
        'Microscopic origin of shape-dependent shear strength of granular materials: a granular dynamics perspective'

    Parameters
    ----------
    v_:
        Particle's velocity.
    neighbor_ : 
        Particle's neighbors.

    Returns
    -------
    granular_temperature_:
         A vector that store the granular temperature.

    '''
    n_particles_ = v_.shape[0]
    granular_temperature_ = np.zeros(n_particles_)
    for i_ in range(n_particles_):
        # calculate v_bar_
        v_bar_ = np.zeros(2)
        sum_v_abs_ = 0
        for j_ in neighbor_[i_]:
            v_bar_[0] += v_[j_][0] * np.linalg.norm(v_[j_])
            v_bar_[1] += v_[j_][1] * np.linalg.norm(v_[j_])
            sum_v_abs_ += np.linalg.norm(v_[j_])
        v_bar_ /= sum_v_abs_
       
        for j_ in neighbor_[i_]:
            granular_temperature_[i_] += (v_[j_][0] - v_bar_[0])**2 + (v_[j_][1] - v_bar_[1])**2
        granular_temperature_ /= 2 * len(neighbor_[i_])

    print('Calculate granular temperature done')
    return granular_temperature_



# granular_temperature_ = calculate_temperature(v_, neighbor_)