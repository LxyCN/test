from bisect import bisect_left as find
import numpy as np

def resample_f(dimension, sample, p, size):
    '''
    return an array of values of a variable with the PDF of p
    
    sample: array of original values

    p: the probability density array at each point

    size: Number of resamples
    '''
    orignal_N_sample = len(sample)
    interval = np.zeros(orignal_N_sample)
    interval[0] = p[0]

    #generate array of the sum of probability 
    for i in range(1,orignal_N_sample):
        interval[i] = interval[i-1] + p[i]

    random_resample = np.random.uniform(high=interval[orignal_N_sample-1], size = size)
    resample = np.zeros([size, dimension])

    for i in range(size):
        resample[i] = sample[find(interval, random_resample[i])]
    
    return resample