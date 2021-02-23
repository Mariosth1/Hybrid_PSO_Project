# from Xin_She_Yang_Bench_Fun.xin_she_yang_N4_fun import xinSheYangN4 as fitness
# from Xin_She_Yang_Bench_Fun.xin_she_yang_N4_fun import lower_bound, upper_bound

from CEC10_Con.CEC10_Con import benchFunctions
fitness = benchFunctions().function1
lower_bound = benchFunctions().f1_lower_bound
upper_bound = benchFunctions().f1_upper_bound

# from CEC10.CEC10 import benchFunctions
# fitness = benchFunctions().function5
# lower_bound = benchFunctions().f5_lower_bound
# upper_bound = benchFunctions().f5_upper_bound

# from CEC17.CEC17 import benchFunctions
# fitness = benchFunctions().function17
# lower_bound = benchFunctions().lower_bound
# upper_bound = benchFunctions().upper_bound

# from CEC05.CEC05 import benchFunctions
# fitness = benchFunctions().function7
# lower_bound = benchFunctions().f7_lower_bound
# upper_bound = benchFunctions().f7_upper_bound


import numpy as np
from copy import deepcopy

class Space():
    def __init__(self):

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        self.particles = []

        self.global_best_eval = float('inf')
        self.global_best_position = np.array([0.])

        # Firefly Algorithm
        self.alpha = 0.2

        # Diversification
        self.diver_array = np.array([])  # Maybe there is no need to save this, did it for later use
        self.diver_per = None

        # Find out if trapped in local optima
        self.local_optima_counter = 0  # Will be set to zero each time it find a new global best

    def particleEvaluation(self):

        # Now I Save the best position and the global best
        for particle in self.particles:

            fitness_eval = fitness(particle.position)

            # Saving the best position of each particle
            if fitness_eval <= particle.best_position_eval:  # Minimization
                particle.best_position_eval = fitness_eval
                particle.best_position = particle.position

            # Saving global best position
            if fitness_eval < self.global_best_eval:

                self.global_best_eval = fitness_eval
                self.global_best_position = particle.position
                self.local_optima_counter = 0

            # Find out if trapped in a local optima
            else: self.local_optima_counter += 1

    def moveParticles(self):
        W, c1, c2 = 0.5, 0.5, 0.5  # Parameters, change them to your desire

        self.prev_particles = deepcopy(self.particles)  # copy::deepcopy is from copying the array

        for particle in self.particles: # (W * particle.velocity) + , if Weighted
            new_velocity = (
                    c1 * np.random.uniform()) * (particle.best_position - particle.position) + (
                                   c2 * np.random.uniform()) * (self.global_best_position - particle.position)

            particle.velocity = new_velocity
            particle.movement()

    def mineBlastExploration(self, shrapnel_pieces, max_iterations, dimensions):
        if self.local_optima_counter < max_iterations * 0.2:

            i = 0  # Population Counter
            for particle in self.particles:

                mine_distance = self.upper_bound - self.lower_bound

                for _ in range(shrapnel_pieces):
                    # Calculation of the distance of the shrapnel pieces
                    mine_distance = mine_distance * abs(np.random.normal(size=(1, dimensions)))**2

                    # Calculation of the direction of the shrapnel pieces
                    mine_direction = (fitness(particle.position) - fitness(self.prev_particles[i].position)) / (
                            particle.position - self.prev_particles[i].position + 10**(-8))  # division by zero fix it
                                                                                            #added 10**(-8) temporarily
                    # Location of the exploding Mine Bomb Particles
                    explode_particle = np.multiply(mine_distance,
                                                   np.cos(2 * np.pi / shrapnel_pieces))

                    # New Mine Particles affected by shrapnels (The new positions)
                    new_position = explode_particle + np.exp(
                        -np.sqrt(abs(mine_direction), abs(mine_distance))) * self.prev_particles[i].position

                    if fitness(particle.position) > fitness(new_position):  # Minimization
                        particle.position = new_position

                i += 1  # counting the population
            else:
                pass

    def bigBangBigCrunch(self, max_iterations, iteration, dimensions):

        if self.local_optima_counter > max_iterations * 0.2:

            sum_fit = 0.  # Sum(1 / fitness)
            sum_fit_pos = np.zeros([1, dimensions])  # Sum((1 / fitness) * Xi)

            for particle in self.particles:
                sum_fit += 1/fitness(particle.position)
                sum_fit_pos += sum_fit * particle.position

            center_of_mass = sum_fit_pos / sum_fit

            # Find the n (= pop_size / 2) worst particles in the population
            pop_size = 0
            particle_quality = []
            for particle in self.particles:
                particle_quality.append(fitness(particle.position))
                pop_size += 1  # i can pass it in the function, but counting it in here in case i want to increase it

            # Finding the population_size best indexes, so that the pop size is the same
            temp = deepcopy(particle_quality)  # Temporarily find the population_size best qualities
            temp.sort(reverse=True)  # Minimization so biggest number is worse
            temp = temp[:int(np.floor(pop_size/2))]
            worst_indexes = [particle_quality.index(k) for k in temp]

            # Replace them with the Big Bang Method
            i = 0
            for particle in self.particles:

                if i in worst_indexes:
                    particle.position = center_of_mass + self.upper_bound * np.random.uniform() / (iteration + 1)
                    # i am not sure here if its upper_bound there
                i += 1
        else:
            pass

    def cuckooSearch(self, iteration, max_iterations):
        # Implementation of cuckoo search global exploration walk

        sigma = 0.5  # step_size
        lev_lambda = 3 / 2
        levy = (lev_lambda * np.random.gamma(lev_lambda) * np.sin(np.pi * lev_lambda / 2)) / (
                    np.pi * sigma ** (1 + lev_lambda))

        scaling_factor = 0.01  # O(L/100) or O(L/10)

        pop_size = 0
        particle_quality = []
        for particle in self.particles:
            particle_quality.append(fitness(particle.position))
            pop_size += 1  # i can pass it in the function, but counting it in here in case i want to increase it

        # Finding the population_size best indexes, so that the pop size is the same
        temp = deepcopy(particle_quality)  # Temporarily find the population_size best qualities
        temp.sort(reverse=True)  # Minimization so biggest number is worse
        temp = temp[:int(np.floor(pop_size / 2))]
        worst_indexes = [particle_quality.index(k) for k in temp]

        # Replace them with the Big Bang Method
        i = 0
        for particle in self.particles:

            if i in worst_indexes:
                particle.position = particle.position + scaling_factor * levy

            i += 1

    def fireflyMovement(self, dimensions, particles_pop):

        # Parameters
        self.alpha += 0.98  # delta
        gamma = 1.
        beta0 = 1.

        for i in range(particles_pop - 1):

            if fitness(self.particles[i].position) < fitness(self.particles[i + 1].position):
                r_dist = self.particles[i + 1].position - self.particles[i].position

                new_light_attract = beta0 * np.exp(
                    -gamma * r_dist ** 2) * r_dist + self.alpha * np.random.uniform(0, 1, [1, dimensions])

                self.particles[i].velocity = new_light_attract
                self.particles[i].movement()

    def diversification(self, dimensions, particles_pop):
        # Finding the % of exploration
        i = 0  # This loop can be done easier, fix it later
        for particle in self.particles:

            if i == 0: particles_matrix = particle.position

            else: particles_matrix = np.concatenate((particles_matrix, particle.position))

            i = 1

        dim_median = np.median(particles_matrix, axis=0)  # The median of each column(dimension) of the particle matrix

        div_in_iter = np.sum(dim_median - particles_matrix) / (particles_pop * dimensions) # Average of Diversity of all dimensions

        self.diver_array = np.append(self.diver_array, div_in_iter)

        max_diver = np.max((abs(self.diver_array)))
        self.diver_per = abs(div_in_iter) / max_diver

    def relocation(self, dimensions):

        # Relocate the position if it goes out of bounds
        for particle in self.particles:

            for i in range(dimensions):

                # Relocation in space
                if particle.position[0][i] > self.upper_bound or particle.position[0][i] < self.lower_bound:

                    particle.position[0][i] = self.lower_bound + (
                            self.upper_bound - self.lower_bound) * np.cos(particle.position[0][i]) ** 2

                # Relocation at bounds
                # if particle.position[0][i] > self.upper_bound: particle.position[0][i] = self.upper_bound
                #
                # elif particle.position[0][i] < self.lower_bound: particle.position[0][i] = self.lower_bound


    # def modifiedCuckooSearch(self):
    #
    #     # If the exploration percentage is less than 50% or we are trapped in a local optima, global walk will occur
    #     if self.local_optima_counter > max_iterations * 0.1:
    #         # Global exploration - Levy Flight
    #         # Levy exponent and coefficient - This is a simple way of implementing Levy flights
    #         # For details, see equation(2.21), Page 16 (chapter2) of the book
    #         # X.S.Yang, Nature - Inspired Metaheuristic Algorithms, 2ndEdition, Luniver Press, (2010).
    #
    #         beta = 3 / 2
    #         sigma = (np.random.gamma(1 + beta) * np.sin(np.pi * beta / 2) / (
    #                     np.random.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
    #
    #         for particle in self.particles:
    #
    #             u = np.random.randn(*particle.position.shape) * sigma
    #             v = np.random.randn(*particle.position.shape)
    #             step = u / abs(v) ** (1 / beta)
    #
    #             # if the particle is the best then the particle remains unchanged
    #             stepsize = 0.01 * step * (particle.position - self.global_best_position)
    #
    #             particle.position = particle.position + stepsize * np.random.randn(*particle.position.shape)
    #
    #     else:
    #         pass
