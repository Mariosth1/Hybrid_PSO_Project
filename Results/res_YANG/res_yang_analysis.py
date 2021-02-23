

# Function Xin - She Yang N1 xsy1
import pandas as pd
"Opening the csv files"
xsy1_df1 = pd.read_csv('res_Yang_F1/PSO_YANG_F1_fun.csv')
xsy1_df2 = pd.read_csv('res_Yang_F1/PSO_MBA_YANG_F1_fun.csv')
xsy1_df3 = pd.read_csv('res_Yang_F1/PSO_BBBC_YANG_F1_fun.csv')
xsy1_df4 = pd.read_csv('res_Yang_F1/PSO_LEVY_YANG_F1_fun.csv')
xsy1_df5 = pd.read_csv('res_Yang_F1/PSO_FA_YANG_F1_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
xsy1_df = pd.DataFrame(
    {
     'PSO - Solution Quality': xsy1_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': xsy1_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': xsy1_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': xsy1_df4.iloc[:, 0],
     'PSO - FA Solution Quality': xsy1_df5.iloc[:, 0]
     }
    )

hist1 = xsy1_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])
hist1
"-------------------------Describe Statistics--------------------------------"
xsy1_describe_df1 = xsy1_df1.describe()
xsy1_describe_df2 = xsy1_df2.describe()
xsy1_describe_df3 = xsy1_df3.describe()
xsy1_describe_df4 = xsy1_df4.describe()
xsy1_describe_df5 = xsy1_df5.describe()

"------------------------------Skewness--------------------------------------"
xsy1_skrew_df1 = xsy1_df1.skew()
xsy1_skrew_df2 = xsy1_df2.skew()
xsy1_skrew_df3 = xsy1_df3.skew()
xsy1_skrew_df4 = xsy1_df4.skew()
xsy1_skrew_df5 = xsy1_df5.skew()


#######################################################################################################################
# Function Xin - She Yang N2 xsy2
import pandas as pd
"Opening the csv files"
xsy2_df1 = pd.read_csv('res_Yang_F2/PSO_YANG_F2_fun.csv')
xsy2_df2 = pd.read_csv('res_Yang_F2/PSO_MBA_YANG_F2_fun.csv')
xsy2_df3 = pd.read_csv('res_Yang_F2/PSO_BBBC_YANG_F2_fun.csv')
xsy2_df4 = pd.read_csv('res_Yang_F2/PSO_LEVY_YANG_F2_fun.csv')
xsy2_df5 = pd.read_csv('res_Yang_F2/PSO_FA_YANG_F2_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
xsy2_df = pd.DataFrame(
    {
     'PSO - Solution Quality': xsy2_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': xsy2_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': xsy2_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': xsy2_df4.iloc[:, 0],
     'PSO - FA Solution Quality': xsy2_df5.iloc[:, 0]
     }
    )

hist2 = xsy2_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])
"-------------------------Describe Statistics--------------------------------"
xsy2_describe_df1 = xsy2_df1.describe()
xsy2_describe_df2 = xsy2_df2.describe()
xsy2_describe_df3 = xsy2_df3.describe()
xsy2_describe_df4 = xsy2_df4.describe()
xsy2_describe_df5 = xsy2_df5.describe()

"------------------------------Skewness--------------------------------------"
xsy2_skrew_df1 = xsy2_df1.skew()
xsy2_skrew_df2 = xsy2_df2.skew()
xsy2_skrew_df3 = xsy2_df3.skew()
xsy2_skrew_df4 = xsy2_df4.skew()
xsy2_skrew_df5 = xsy2_df5.skew()

#######################################################################################################################
# Function Xin - She Yang N1 xsy1
import pandas as pd
"Opening the csv files"
xsy3_df1 = pd.read_csv('res_Yang_F3/PSO_YANG_F3_fun.csv')
xsy3_df2 = pd.read_csv('res_Yang_F3/PSO_MBA_YANG_F3_fun.csv')
xsy3_df3 = pd.read_csv('res_Yang_F3/PSO_BBBC_YANG_F3_fun.csv')
xsy3_df4 = pd.read_csv('res_Yang_F3/PSO_LEVY_YANG_F3_fun.csv')
xsy3_df5 = pd.read_csv('res_Yang_F3/PSO_FA_YANG_F3_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
xsy3_df = pd.DataFrame(
    {
     'PSO - Solution Quality': xsy3_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': xsy3_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': xsy3_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': xsy3_df4.iloc[:, 0],
     'PSO - FA Solution Quality': xsy3_df5.iloc[:, 0]
     }
    )

hist3 = xsy3_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])
"-------------------------Describe Statistics--------------------------------"
xsy3_describe_df1 = xsy3_df1.describe()
xsy3_describe_df2 = xsy3_df2.describe()
xsy3_describe_df3 = xsy3_df3.describe()
xsy3_describe_df4 = xsy3_df4.describe()
xsy3_describe_df5 = xsy3_df5.describe()

"------------------------------Skewness--------------------------------------"
xsy3_skrew_df1 = xsy3_df1.skew()
xsy3_skrew_df2 = xsy3_df2.skew()
xsy3_skrew_df3 = xsy3_df3.skew()
xsy3_skrew_df4 = xsy3_df4.skew()
xsy3_skrew_df5 = xsy3_df5.skew()

#######################################################################################################################
# Function Xin - She Yang N4 xsy4
import pandas as pd
"Opening the csv files"
xsy4_df1 = pd.read_csv('res_Yang_F4/PSO_YANG_F4_fun.csv')
xsy4_df2 = pd.read_csv('res_Yang_F4/PSO_MBA_YANG_F4_fun.csv')
xsy4_df3 = pd.read_csv('res_Yang_F4/PSO_BBBC_YANG_F4_fun.csv')
xsy4_df4 = pd.read_csv('res_Yang_F4/PSO_LEVY_YANG_F4_fun.csv')
xsy4_df5 = pd.read_csv('res_Yang_F4/PSO_FA_YANG_F4_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
xsy4_df = pd.DataFrame(
    {
     'PSO - Solution Quality': xsy4_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': xsy4_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': xsy4_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': xsy4_df4.iloc[:, 0],
     'PSO - FA Solution Quality': xsy4_df5.iloc[:, 0]
     }
    )

hist4 = xsy4_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])
"-------------------------Describe Statistics--------------------------------"
xsy4_describe_df1 = xsy4_df1.describe()
xsy4_describe_df2 = xsy4_df2.describe()
xsy4_describe_df3 = xsy4_df3.describe()
xsy4_describe_df4 = xsy4_df4.describe()
xsy4_describe_df5 = xsy4_df5.describe()

"------------------------------Skewness--------------------------------------"
xsy4_skrew_df1 = xsy4_df1.skew()
xsy4_skrew_df2 = xsy4_df2.skew()
xsy4_skrew_df3 = xsy4_df3.skew()
xsy4_skrew_df4 = xsy4_df4.skew()
xsy4_skrew_df5 = xsy4_df5.skew()

