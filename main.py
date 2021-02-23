from PSO_Algorithm.repetitive_procedure import RepetitiveProcedure as Algorithm
import time
"""
main needs to contain the:
    1. dimensions = the dimensions of the decision variable, can be imported from data. 
    2. pso_iterations = The iterations of PSO in the Search Space.
    3. particles_pop = The population of the particles.
    4. independent_runs = The number of independent test runs of PSO Algorithm.
 """
independent_runs = 40  #40
pso_iterations = 50  #100
particles_pop = 50  #100
dimensions = 30  #50

if __name__ == '__main__':

    start_time = time.time()
    # This is for testing in console
    for i in range(independent_runs):
        print(Algorithm(pso_iterations, particles_pop, dimensions).results(i, independent_runs))
    end_time = time.time()
    time_lapsed = end_time - start_time
    print('Time lapsed = ', time_lapsed, ' sec')
    """
    # This is for exporting the results in a csv file
    from csv_export_fun import csv_export
    name_of_file = "PSO_FA_CEC10_Con_F1_fun.csv"  # needs to be in a string from ("name.csv")
    csv_export(independent_runs, name_of_file)
    """