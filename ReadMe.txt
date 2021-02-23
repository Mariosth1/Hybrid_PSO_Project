This is a hybrid PSO Algorithm running benchmark functions:
Mechanisms fetched from other nature inspired Algorithms are applied to solve PSO's well-known problems (i.e. premature
convergence) and also make it more robust, efficient, etc.

Specifically the mechanisms used to create schemes are:
1) The Exploration mechanism from Mine Blast Algorithm
2) The Big Bang - Big Crunch Method
3) The Levy Flight from Cuckoo Search
4) The Firefly Algorithm movement

=======================================================================================================================
a) Inside _main_ you can set:
    1. pso_iterations = The iterations of PSO in the Search Space.
    2. particles_pop = The population of the particles.
    3. independent_runs = The number of independent test runs of PSO Algorithm.

    As preset _main_ prints the results in the console. The results are the fitness evaluation (Quality) and the
    allocation of the decision variables (Best Particle Position).
    You can also choose if you want a csv file exported:
        Erase the comment with the csv function inside _main_ and change the "name_of_file" in a string ("name.csv") of
        your desire.

If you wish to change the PSO velocity parameters open the "PSO_Algorithm.search_space.py":
    Inside the moveParticles function ("def moveParticles"):
        c1 = acceleration coefficient affecting the importance of personal best value
        c2 = acceleration coefficient affecting the importance of social best value

=======================================================================================================================
b) If you wish to change the fitness open the "PSO_Algorithm.search_space.py":
    import your fitness function as fitness
    i.e.:
    "from Folder.yourFile import yourFitnessFunction as fitness"

The data are imported inside the objective function

The data and other parameters are imported in the "PSO_Algorithm.search_space.py":
    1. lower_bound = the lower bound of the decision variable, can be imported from data.
    2. upper_bound = the upper bound of the decision variable, can be imported from data.

    import from your data the 2 parameters
    i.e.:
    "from Folder.yourDataFile import lower_bound, upper_bound"

=======================================================================================================================
c) 3 Schemes created:
    1. PSO - MBA (Particle Swarm Optimization with Mine Blast Algorithm, Exploration Mechanism)
    2. PSO - BBBC (Particle Swarm Optimization with Big Bang - Big Crunch Method)
    3. PSO - CS (Particle Swarm Optimization with Cuckoo Search, Levy Flight Mechanism)
    4. PSO - FA (Particle Swarm Optimization with Firefly Algorithm, Movement Mechanism)

    If you wish to change the scheme or run the simple PSO, you can toggle them by changing the parameters to 'True':

    MINE_BLAST_EPLOR = False
    BIG_BANG_BIG_CRUNCH = False
    CUCKOO_SEARCH = False
    FIREFLY_MOVEMENT = False

    Which are located in the "PSO_Algorithm.search_space.py" file.

=======================================================================================================================
d) Exploration - Exploitation:

    Its independent also returns the Average Xpl% and Xpt% of the Scheme.

    If you wish to plot a the Xpl and Xpt of the last Run, you can toggle them by changing the parameter to 'True':

    PLOTTING = False