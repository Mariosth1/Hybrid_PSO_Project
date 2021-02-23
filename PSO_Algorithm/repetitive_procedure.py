from PSO_Algorithm.particle_info import Particle
from PSO_Algorithm.search_space import Space

import numpy as np


MINE_BLAST_EPLOR = False        # If True apply the Exploration Process of the Mine Blast Algorithm
BIG_BANG_BIG_CRUNCH = False   # If True apply the Big Bang - Big Crunch method and replace the worst particles
CUCKOO_SEARCH = False         # If True apply the Cuckoo Search global exploration method
FIREFLY_MOVEMENT = True      # If True apply the Firefly Algorithm Movement

PLOTTING = False  # Plot the exploration of the last independent run

class RepetitiveProcedure():
    def __init__(self, max_iterations, particles_pop, dimensions):

        self.max_iterations = max_iterations
        self.particles_pop = particles_pop
        self.dimensions = dimensions

        self.s_space = Space()
        self.lower_bound = Space().lower_bound
        self.upper_bound = Space().upper_bound

        # Simple PSO initialization
        self.particles_vector = [Particle(self.dimensions, self.lower_bound, self.upper_bound) for _ in range(self.particles_pop)]

        self.s_space.particles = self.particles_vector

        # Initialization of new fractals per particle
        self.new_fractals_per = np.random.randint(3, 10)  # The number of fractals produced per diffusion

        # Initialization of the the new mine bomb particles / pass the particles attributes init
        self.shrapnel_pieces = np.random.randint(3, 10)  # The number of sharpnels per explosion

    def results(self, plot_iter, independent_runs):
        exploration = []
        for iteration in range(self.max_iterations):

            self.s_space.particleEvaluation()
            self.s_space.diversification(self.dimensions, self.particles_pop)  # Finding the % of Exploration
            self.s_space.moveParticles()  # Move the Particles in space with the PSO velocity mechanism

            if MINE_BLAST_EPLOR:
                self.s_space.mineBlastExploration(self.shrapnel_pieces, self.max_iterations,
                                                  self.dimensions)  # Exploration of Mine Blast Algorithm
            if CUCKOO_SEARCH:
                self.s_space.cuckooSearch(iteration, self.max_iterations)

            if BIG_BANG_BIG_CRUNCH:
                self.s_space.bigBangBigCrunch(self.max_iterations, iteration, self.dimensions)

            if FIREFLY_MOVEMENT:
                self.s_space.fireflyMovement(self.dimensions, self.particles_pop)

            # Relocate the position in space, if it goes out of bound
            self.s_space.relocation(self.dimensions)

            # Check if relocation Works
            # for particle in self.s_space.particles:
            #     for i in range(self.dimensions):
            #         # Relocation in space
            #         if particle.position[0][i] > 100 or particle.position[0][i] < -100: print('condition True')

            # Plotting
            exploration.append(self.s_space.diver_per)
        exploitation = [1 - exploration[_] for _ in range(len(exploration))]

        if plot_iter == independent_runs - 1:

            if PLOTTING:
                from matplotlib import pyplot as plt
                plt.plot(exploration, label='Xpl %')
                plt.plot(exploitation, label='Xpt %')

                plt.ylabel("Exploration - Exploitation %")
                plt.xlabel("Iterations")
                plt.title("CEC10 F17 - PSO - FA")
                plt.legend()
                plt.show()

        return self.s_space.global_best_eval, self.s_space.global_best_position,\
               np.average(exploration), np.average(exploitation)

