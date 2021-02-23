def csv_export(alg_runs, name_of_file):

    from main import pso_iterations, particles_pop, dimensions, Algorithm , independent_runs
    import pandas as pd

    df = pd.DataFrame()

    for i in range(alg_runs):
        print(i)
        [Quality, Position , Exploration, Exploitation
         ] = Algorithm(pso_iterations, particles_pop, dimensions).results(i, independent_runs)
        # can add Slack depending the benchmark problem
        temp_df = pd.DataFrame(
            {
                'Solution_Quality': Quality,
                'Solution_Allocation': [Position],  # can also add slack columns
                'AVG_Exploration': Exploration,
                'AVG_Exploitation': Exploitation
            }
        )

        df = pd.concat([df, temp_df])

    "-------------------Change the name of the saved csv-------------------------"
    df.to_csv(name_of_file, sep = ',', header = True, index = False)