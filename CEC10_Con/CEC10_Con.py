import scipy.io as scipy
import numpy as np
import numpy.matlib

class benchFunctions:
    def __init__(self):
        self.f1_lower_bound, self.f1_upper_bound = 0, 10
        self.f7_lower_bound, self.f7_upper_bound = -140, 140

    def function1(self, x):
        temp = scipy.loadmat('CEC10_Con/Function1.mat')
        o = temp['o']

        [ps, D] = x.shape

        o = o[:D]

        y = x - np.matlib.repmat(o, ps, 1)

        f1 = np.sum(np.cos(y) ** 4) - 2 * np.product(np.cos(y) ** 2)
        f2 = np.zeros([ps, 1])

        for i in range(D):
            f2 += i * y[0][i]

        fit = - np.abs(f1 / np.sqrt(f2))
        g1 = 0.75 - np.product(y)
        g2 = np.sum(y) - 7.5 * D

        if g1 > 0 or g2 > 0:
            fit += np.max(g1, 0) + np.max(g2, 0)

        return fit[0][0]

    def function7(self, x):
        temp = scipy.loadmat('CEC10_Con/Function7.mat')
        o = temp['o']

        [ps, D] = x.shape

        o = o[:D]

        y = x - np.matlib.repmat(o, ps, 1)

        z = y + 1

        fit = np.sum(100 * (z[0][:(D - 1)] ** 2 - z[0][1:D]) ** 2 + (z[0][:(D - 1)] - 1) ** 2)
        g = 0.5 - np.exp(-0.1 * np.sqrt(np.sum(y ** 2) / D)) - 3 * np.exp(np.sum(np.cos(0.1 * y)) / D) + np.exp(1)

        if g > 0:
            fit += max(g, 0)

        return fit