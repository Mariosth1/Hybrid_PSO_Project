import numpy as np
import random as r

class Particle():
    def __init__(self, dimensions, lower_bound, upper_bound):

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.dimensions = dimensions
        self.position = np.array([[(lower_bound + (upper_bound - lower_bound)*r.random()) for _ in range(self.dimensions)]])
        self.best_position = self.position
        self.best_position_eval = float('inf') #np.array([0.]) #float('-inf')
        self.velocity = np.array([0 for _ in range(self.dimensions)])

    def movement(self):
        self.position = self.position + self.velocity