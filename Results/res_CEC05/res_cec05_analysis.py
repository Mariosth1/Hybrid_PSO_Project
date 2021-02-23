

# Function CEC05 F3
import pandas as pd
"Opening the csv files"
f3_df1 = pd.read_csv('res_F3/PSO_CEC05_F3_fun.csv')
f3_df2 = pd.read_csv('res_F3/PSO_MBA_CEC05_F3_fun.csv')
f3_df3 = pd.read_csv('res_F3/PSO_BBBC_CEC05_F3_fun.csv')
f3_df4 = pd.read_csv('res_F3/PSO_LEVY_CEC05_F3_fun.csv')
f3_df5 = pd.read_csv('res_F3/PSO_FA_CEC05_F3_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
f3_df = pd.DataFrame(
    {
     'PSO - Solution Quality': f3_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': f3_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': f3_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': f3_df4.iloc[:, 0],
     'PSO - FA Solution Quality': f3_df5.iloc[:, 0]
     }
    )

hist1 = f3_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])
hist1
"-------------------------Describe Statistics--------------------------------"
f3_describe_df1 = f3_df1.describe()
f3_describe_df2 = f3_df2.describe()
f3_describe_df3 = f3_df3.describe()
f3_describe_df4 = f3_df4.describe()
f3_describe_df5 = f3_df5.describe()

"------------------------------Skewness--------------------------------------"
f3_skrew_df1 = f3_df1.skew()
f3_skrew_df2 = f3_df2.skew()
f3_skrew_df3 = f3_df3.skew()
f3_skrew_df4 = f3_df4.skew()
f3_skrew_df5 = f3_df5.skew()


#######################################################################################################################
# Function CEC05 F6
import pandas as pd
"Opening the csv files"
f6_df1 = pd.read_csv('res_F6/PSO_CEC05_F6_fun.csv')
f6_df2 = pd.read_csv('res_F6/PSO_MBA_CEC05_F6_fun.csv')
f6_df3 = pd.read_csv('res_F6/PSO_BBBC_CEC05_F6_fun.csv')
f6_df4 = pd.read_csv('res_F6/PSO_LEVY_CEC05_F6_fun.csv')
f6_df5 = pd.read_csv('res_F6/PSO_FA_CEC05_F6_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
f6_df = pd.DataFrame(
    {
     'PSO - Solution Quality': f6_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': f6_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': f6_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': f6_df4.iloc[:, 0],
     'PSO - FA Solution Quality': f6_df5.iloc[:, 0]
     }
    )

hist2 = f6_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])

"-------------------------Describe Statistics--------------------------------"
f6_describe_df1 = f6_df1.describe()
f6_describe_df2 = f6_df2.describe()
f6_describe_df3 = f6_df3.describe()
f6_describe_df4 = f6_df4.describe()
f6_describe_df5 = f6_df5.describe()

"------------------------------Skewness--------------------------------------"
f6_skrew_df1 = f6_df1.skew()
f6_skrew_df2 = f6_df2.skew()
f6_skrew_df3 = f6_df3.skew()
f6_skrew_df4 = f6_df4.skew()
f6_skrew_df5 = f6_df5.skew()


#######################################################################################################################
# Function CEC05 F3
import pandas as pd
"Opening the csv files"
f7_df1 = pd.read_csv('res_F7/PSO_CEC05_F7_fun.csv')
f7_df2 = pd.read_csv('res_F7/PSO_MBA_CEC05_F7_fun.csv')
f7_df3 = pd.read_csv('res_F7/PSO_BBBC_CEC05_F7_fun.csv')
f7_df4 = pd.read_csv('res_F7/PSO_LEVY_CEC05_F7_fun.csv')
f7_df5 = pd.read_csv('res_F7/PSO_FA_CEC05_F7_fun.csv')

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

hist3 = f7_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])

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

