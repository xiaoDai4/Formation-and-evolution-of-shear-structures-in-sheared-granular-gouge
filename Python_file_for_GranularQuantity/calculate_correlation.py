import numpy as np
import math
def calculate_correlation(distance_, values_, r_, a_):
    '''
    Relevant theory is in airticle 'Microscopic origin of shape-dependent shear strength of granular
    materials: a granular dynamics perspective'

    Parameters
    ----------
    distance_ : matrix
        distance between particles.
    values_ : vector
        the values to calculate the correlation.
    r_ : vector
        the prescribed mutual distance.
    a_: float
        the sigma of smooth delta
    Returns
    -------
    correlation_ : vector
        correlation.

    '''
    
    n_particles_ = len(values_)
    correlation_ = np.zeros(len(r_))
    mean_ = np.average(values_)
    mean_sq_ =  np.average(values_ ** 2)                # mean of  square
    for i_ in range(len(r_)):
        print(i_)
        n_ = 0 # accumulation of delta
        pairs_ = 0 # accumulation of pairs mutiply
        for j_ in range(n_particles_):
            for k_ in range(n_particles_):
                n_ += smooth_delta(distance_[j_, k_] - r_[i_],a_)
                pairs_ += smooth_delta(distance_[j_, k_] - r_[i_],a_) * values_[j_] * values_[k_]
        correlation_[i_] = (pairs_/n_ - mean_**2) / (mean_sq_ - mean_**2)
    print('Calculate correlation done.')
    return correlation_
    

# smooth delta
def smooth_delta(r_,a_):
    return 1/(a_ * math.sqrt(math.pi)) * math.exp(-r_**2 / a_**2)

# a_ = 10e-5
# correlation_ = calculate_correlation(distance_, values_, r_, a_)