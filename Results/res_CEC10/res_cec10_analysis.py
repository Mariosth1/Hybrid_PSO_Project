

# Function CEC10 F5
import pandas as pd
"Opening the csv files"
f5_df1 = pd.read_csv('res_F5/PSO_CEC10_F5_fun.csv')
f5_df2 = pd.read_csv('res_F5/PSO_MBA_CEC10_F5_fun.csv')
f5_df3 = pd.read_csv('res_F5/PSO_BBBC_CEC10_F5_fun.csv')
f5_df4 = pd.read_csv('res_F5/PSO_LEVY_CEC10_F5_fun.csv')
f5_df5 = pd.read_csv('res_F5/PSO_FA_CEC10_F5_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
f5_df = pd.DataFrame(
    {
     'PSO - Solution Quality': f5_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': f5_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': f5_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': f5_df4.iloc[:, 0],
     'PSO - FA Solution Quality': f5_df5.iloc[:, 0]
     }
    )

hist1 = f5_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])
hist1
"-------------------------Describe Statistics--------------------------------"
f5_describe_df1 = f5_df1.describe()
f5_describe_df2 = f5_df2.describe()
f5_describe_df3 = f5_df3.describe()
f5_describe_df4 = f5_df4.describe()
f5_describe_df5 = f5_df5.describe()

"------------------------------Skewness--------------------------------------"
f5_skrew_df1 = f5_df1.skew()
f5_skrew_df2 = f5_df2.skew()
f5_skrew_df3 = f5_df3.skew()
f5_skrew_df4 = f5_df4.skew()
f5_skrew_df5 = f5_df5.skew()


#######################################################################################################################
# Function CEC10 F11
import pandas as pd
"Opening the csv files"
f11_df1 = pd.read_csv('res_F11/PSO_CEC10_F11_fun.csv')
f11_df2 = pd.read_csv('res_F11/PSO_MBA_CEC10_F11_fun.csv')
f11_df3 = pd.read_csv('res_F11/PSO_BBBC_CEC10_F11_fun.csv')
f11_df4 = pd.read_csv('res_F11/PSO_LEVY_CEC10_F11_fun.csv')
f11_df5 = pd.read_csv('res_F11/PSO_FA_CEC10_F11_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
f11_df = pd.DataFrame(
    {
     'PSO - Solution Quality': f11_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': f11_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': f11_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': f11_df4.iloc[:, 0],
     'PSO - FA Solution Quality': f11_df5.iloc[:, 0]
     }
    )

hist2 = f11_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])

"-------------------------Describe Statistics--------------------------------"
f11_describe_df1 = f11_df1.describe()
f11_describe_df2 = f11_df2.describe()
f11_describe_df3 = f11_df3.describe()
f11_describe_df4 = f11_df4.describe()
f11_describe_df5 = f11_df5.describe()

"------------------------------Skewness--------------------------------------"
f11_skrew_df1 = f11_df1.skew()
f11_skrew_df2 = f11_df2.skew()
f11_skrew_df3 = f11_df3.skew()
f11_skrew_df4 = f11_df4.skew()
f11_skrew_df5 = f11_df5.skew()


#######################################################################################################################
# Function CEC10 F17
import pandas as pd
"Opening the csv files"
f17_df1 = pd.read_csv('res_F17/PSO_CEC10_F17_fun.csv')
f17_df2 = pd.read_csv('res_F17/PSO_MBA_CEC10_F17_fun.csv')
f17_df3 = pd.read_csv('res_F17/PSO_BBBC_CEC10_F17_fun.csv')
f17_df4 = pd.read_csv('res_F17/PSO_LEVY_CEC10_F17_fun.csv')
f17_df5 = pd.read_csv('res_F17/PSO_FA_CEC10_F17_fun.csv')

"--------------------Plot all of them together-------------------------------"
# Solution Quality
f17_df = pd.DataFrame(
    {
     'PSO - Solution Quality': f17_df1.iloc[:, 0],
     'PSO - MBA Solution Quality': f17_df2.iloc[:, 0],
     'PSO - BBBC Solution Quality': f17_df3.iloc[:, 0],
     'PSO - LEVY Solution Quality': f17_df4.iloc[:, 0],
     'PSO - FA Solution Quality': f17_df5.iloc[:, 0]
     }
    )

hist3 = f17_df.hist(sharey = True, figsize = [8,8], xrot = -30, range = [0.0,1])

"-------------------------Describe Statistics--------------------------------"
f17_describe_df1 = f17_df1.describe()
f17_describe_df2 = f17_df2.describe()
f17_describe_df3 = f17_df3.describe()
f17_describe_df4 = f17_df4.describe()
f17_describe_df5 = f17_df5.describe()

"------------------------------Skewness--------------------------------------"
f17_skrew_df1 = f17_df1.skew()
f17_skrew_df2 = f17_df2.skew()
f17_skrew_df3 = f17_df3.skew()
f17_skrew_df4 = f17_df4.skew()
f17_skrew_df5 = f17_df5.skew()

#######################################################################################################################

print(1, f17_describe_df1)
print(2, f17_describe_df2)
print(3, f17_describe_df3)
print(4, f17_describe_df4)
print(5, f17_describe_df5)
