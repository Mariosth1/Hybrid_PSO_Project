
lower_bound, upper_bound = -5, 5

def xinSheYangFun(x):
    import numpy as np

    dim = x.shape[1]
    fit = 0

    for i in range(dim):

        fit +=  np.random.uniform() * np.abs(x[:, i])**i

    return fit