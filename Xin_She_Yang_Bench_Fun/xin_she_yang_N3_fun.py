lower_bound, upper_bound = -5, 10

def xinSheYangN3(x):

    dim = x.shape[1]

    comp1, comp2 = 0, 0

    for i in range(dim):

        comp1 += x[0][i]**2
        comp2 += 0.5 * i * x[0][i]

    fit = comp1 + comp2 ** 2 + comp2 ** 4

    return fit