lower_bound, upper_bound = -10, 10

def xinSheYangN4(x):
    import numpy as np

    fit = np.sum(np.sin(x) ** 2) - np.exp(-np.sum(x ** 2)) * np.exp(-np.sum(np.sin(np.sqrt(np.abs(x))) ** 2))

    return fit