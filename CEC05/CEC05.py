import scipy.io as scipy
import numpy as np
import numpy.matlib


class benchFunctions:
    def __init__(self):

        self.f3_lower_bound, self.f3_upper_bound = -100, 100
        self.f6_lower_bound, self.f6_upper_bound = -100, 100
        self.f7_lower_bound, self.f7_upper_bound = 0, 600

        f_bias = scipy.loadmat('CEC05/fbias_data.mat')
        self.f_bias = f_bias['f_bias']

    # 3. Shifted Rotated High Conditioned Elliptic Function
    def function3(self, x):

        o = scipy.loadmat('CEC05/high_cond_elliptic_rot_data.mat')
        o = o['o']

        [ps, D] = x.shape

        if o.shape[1] > D:
            o = o[0][:D]

        else:
            o = -100 + 200 * np.random.random([1, D])

        c = 1
        if D == 2:
            M = scipy.loadmat('CEC05/elliptic_M_D2.mat')
            M = M['M']

        elif D == 10:
            M = scipy.loadmat('CEC05/elliptic_M_D10.mat')
            M = M['M']

        elif D == 30:
            M = scipy.loadmat('CEC05/elliptic_M_D30.mat')
            M = M['M']

        elif D == 50:
            M = scipy.loadmat('CEC05/elliptic_M_D50.mat')
            M = M['M']

        y = x - np.matlib.repmat(o, ps, 1)

        y *= M[0][:]
        a = 1e+6
        fit = 0
        for i in range(D):

            fit += a ** ((i - 1) / (D - 1)) * y[0][i] ** 2

        return fit + self.f_bias[0][2]

    # 6. Shifted Rosenbrock's Function
    def function6(self, x):

        o = scipy.loadmat('CEC05/rosenbrock_func_data.mat')
        o = o['o']

        [ps, D] = x.shape

        if o.shape[1] > D:
            o = o[0][:D]

        else:
            o = -90 + 180 * np.random.random([1, D])

        y = x - np.matlib.repmat(o, ps, 1) + 1

        fit = np.sum(100 * (y[:][:(D - 1)] ** 2 - y[:][:D]) ** 2 + (y[:][:(D - 1)] - 1) ** 2)

        return fit + self.f_bias[0][5]

    # 7. Shifted Rotated Griewank's Function
    def function7(self, x):

        o = scipy.loadmat('CEC05/griewank_func_data.mat')
        o = o['o']

        [ps, D] = x.shape

        if o.shape[1] > D:
            o = o[0][:D]

        else:
            o = -600 + 0 * np.random.random([1, D])


        if D == 2:
            M = scipy.loadmat('CEC05/griewank_M_D2.mat')
            M = M['M']

        elif D == 10:
            M = scipy.loadmat('CEC05/griewank_M_D10.mat')
            M = M['M']

        elif D == 30:
            M = scipy.loadmat('CEC05/griewank_M_D30.mat')
            M = M['M']

        elif D == 50:
            M = scipy.loadmat('CEC05/griewank_M_D50.mat')
            M = M['M']

        y = x - np.matlib.repmat(o, ps, 1)
        y *= M[0][:]

        fit = 1
        for i in range(D):

            fit *= np.cos(y[0][i] / np.sqrt(i + 1))

        fit = np.sum(y**2) / 4000 - fit + 1
        return fit + self.f_bias[0][6]
