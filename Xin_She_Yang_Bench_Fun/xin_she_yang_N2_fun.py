import numpy as np
lower_bound, upper_bound = -2 * np.pi, 2 * np.pi

def xinSheYangN2(x):

    dim = x.shape[1]

    fit = np.sum(np.abs(x)) * np.exp(- np.sum(np.sin(x **2)))

    return fit