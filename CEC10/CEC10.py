import numpy as np
import numpy.matlib
import scipy.io as scipy

class benchFunctions:
    def __init__(self):
        self.f5_lower_bound, self.f5_upper_bound = -5, 5
        self.f11_lower_bound, self.f11_upper_bound = -32, 32
        self.f17_lower_bound, self.f17_upper_bound = -100, 100

    def function5(self, x):

        temp = scipy.loadmat('CEC10/f05_opm.mat')
        o = temp['o']
        p = temp['p']
        M = temp['M']

        [ps, D] = x.shape
        m = 50

        if D != 1000:
            print('Error only 1000 dimensions')
        else:
            a = 1e+6

            y = x - np.matlib.repmat(o, ps, 1)

            p = p - 1
            fit = a * np.sum((M * y[0][p[0][:m]]) ** 2 - 10 * np.cos(2 * np.pi * (M * y[0][p[0][:m]]))+10
                             ) + np.sum(y[0][p[0][(m + 1):]] ** 2 - 10 * np.cos(2 * np.pi * y[0][p[0][(m + 1):]])+10)
            print(a * np.sum((M * y[0][p[0][:m]]) ** 2 - 10 * np.cos(2 * np.pi * (M * y[0][p[0][:m]]))+10))
        return fit

    def function11(self, x):

        temp = scipy.loadmat('CEC10/f11_opm.mat')
        o = temp['o']
        p = temp['p']
        M = temp['M']
        p = p - 1
        [ps, D] = x.shape
        m = 50
        G = D/m/2
        if D != 1000:
            print('Error only 1000 dimensions')
        else:
            fit = 0
            y = x - np.matlib.repmat(o, ps, 1)

            for k in range(int(G)):
                index = np.arange(((k - 1) * m + 1), (k * m + 1))

                fit += 20 - 20 * np.exp(-0.2 * np.sqrt(fit / D)) - np.exp(np.sum(np.cos(2 * np.pi * y[0][p[0][index]] * M)) / D) + np.exp(1)

            fit += 20 - 20 * np.exp(-0.2 * np.sqrt(fit / D)) - np.exp(np.sum(np.cos(2 * np.pi * y[0][p[0][(int(G)*m+10):]])) / D) + np.exp(1)

        return fit

    def function17(self, x):
        temp = scipy.loadmat('CEC10/f17_op.mat')
        o = temp['o']
        p = temp['p']

        p = p - 1
        [ps, D] = x.shape
        m = 50
        G = D / m
        if D != 1000:
            print('Error only 1000 dimensions')
        else:
            fit = 0
            y = x - np.matlib.repmat(o, ps, 1)
            for k in range(int(G)):
                index = np.arange(((k - 1) * m + 1), (k * m + 1))

                fit += self.schwefelProb12(y[0][p[0][index]])

        return fit

    def schwefelProb12(self, x):

        D = x.shape[0]
        fit = 0
        for i in range(D):
            fit += np.sum(x[:][:i]) ** 2

        return fit
