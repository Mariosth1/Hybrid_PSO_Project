

# Function CEC10 Constrain F1
import pandas as pd
"Opening the csv files"
f1_df1 = pd.read_csv('res_F1/PSO_CEC10_Con_F1_fun.csv')
f1_df2 = pd.read_csv('res_F1/PSO_MBA_CEC10_Con_F1_fun.csv')
f1_df3 = pd.read_csv('res_F1/PSO_BBBC_CEC10_Con_F1_fun.csv')
f1_df4 = pd.read_csv('res_F1/PSO_LEVY_CEC10_Con_F1_fun.csv')
f1_df5 = pd.read_csv('res_F1/PSO_FA_CEC10_Con_F1_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
f1_df = pd.DataFrame(
    {
     'PSO - Solution Quality': f1_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': f1_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': f1_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': f1_df4.iloc[:, 0],
     'PSO - FA Solution Quality': f1_df5.iloc[:, 0]
     }
    )

hist1 = f1_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])

"-------------------------Describe Statistics--------------------------------"
f1_describe_df1 = f1_df1.describe()
f1_describe_df2 = f1_df2.describe()
f1_describe_df3 = f1_df3.describe()
f1_describe_df4 = f1_df4.describe()
f1_describe_df5 = f1_df5.describe()

"------------------------------Skewness--------------------------------------"
f1_skrew_df1 = f1_df1.skew()
f1_skrew_df2 = f1_df2.skew()
f1_skrew_df3 = f1_df3.skew()
f1_skrew_df4 = f1_df4.skew()
f1_skrew_df5 = f1_df5.skew()


#######################################################################################################################
# Function CEC10 Constrained F7
import pandas as pd
"Opening the csv files"
f7_df1 = pd.read_csv('res_F7/PSO_CEC10_Con_F7_fun.csv')
f7_df2 = pd.read_csv('res_F7/PSO_MBA_CEC10_Con_F7_fun.csv')
f7_df3 = pd.read_csv('res_F7/PSO_BBBC_CEC10_Con_F7_fun.csv')
f7_df4 = pd.read_csv('res_F7/PSO_LEVY_CEC10_Con_F7_fun.csv')
f7_df5 = pd.read_csv('res_F7/PSO_FA_CEC10_Con_F7_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
f7_df = pd.DataFrame(
    {
     'PSO - Solution Quality': f7_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': f7_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': f7_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': f7_df4.iloc[:, 0],
     'PSO - FA Solution Quality': f7_df5.iloc[:, 0]
     }
    )

hist2 = f7_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])

"-------------------------Describe Statistics--------------------------------"
f7_describe_df1 = f7_df1.describe()
f7_describe_df2 = f7_df2.describe()
f7_describe_df3 = f7_df3.describe()
f7_describe_df4 = f7_df4.describe()
f7_describe_df5 = f7_df5.describe()

"------------------------------Skewness--------------------------------------"
f7_skrew_df1 = f7_df1.skew()
f7_skrew_df2 = f7_df2.skew()
f7_skrew_df3 = f7_df3.skew()
f7_skrew_df4 = f7_df4.skew()
f7_skrew_df5 = f7_df5.skew()

