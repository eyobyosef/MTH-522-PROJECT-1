Importing Libraries and Loading Data
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
from google.colab import files
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
import statsmodels.api as sm
from statsmodels.formula.api import ols
# Load the data from a file uploaded in Colab
uploaded = files.upload()
df = pd.read_excel(io.BytesIO(uploaded.get('cdc-diabetes-2018
(1).xlsx')))
# Separate data from different sheets in the Excel file
df_first_sheet = pd.read_excel(xlsx_file, 'Diabetes')
df_second_sheet = pd.read_excel(xlsx_file, 'Obesity')
df_third_sheet = pd.read_excel(xlsx_file, 'Inactivity')
# Extract specific columns from different sheets
diabetic = df_first_sheet['% DIABETIC']
obesity = df_second_sheet['% OBESE']
inactive = df_third_sheet['% INACTIVE']
# Merge the dataframes based on a common column 'FIPS'
merged_df = pd.merge(df_first_sheet, df_second_sheet, on="FIPS",
how="inner")
merged_df_final = pd.merge(merged_df, df_third_sheet_rename,
on="FIPS", how="inner")
# Display some basic information about the merged dataset
print(len(merged_df_final['% DIABETIC']), len(merged_df_final['%
OBESE']), len(merged_df_final['% INACTIVE']))
print(merged_df_final.head())
print(merged_df_final.isnull().sum())
print(merged_df_final.describe())
# Calculate statistics and create visualizations
print(merged_df_final['% DIABETIC'].corr(merged_df_final['%
INACTIVE']))
# ... (More code for histograms, scatter plots, and linear
regression)
# Fit a linear regression model and print coefficients
X = merged_df_final[['% OBESE', '% INACTIVE']]
y = merged_df_final['% DIABETIC']
regr = linear_model.LinearRegression()
regr.fit(X, y)
print(f"Intercept: {regr.intercept_}")
print(f"Slope: {regr.coef_}")
# Perform ANOVA analysis and display the results
mod = smf.ols(formula='y ~ X', data=merged_df_final)
res = mod.fit()
print(res.summary())
aov_table = sm.stats.anova_lm(model, typ=2)
print(aov_table)
# Calculate mean, median, and other statistics
mean_diabetes = merged_df_final['% DIABETIC'].mean()
median_inactive = merged_df_final['% INACTIVE'].median()
std_dev_diabetics = merged_df_final['% DIABETIC'].std()
kurtosis_diabetics = merged_df_final['% DIABETIC'].kurtosis()
print("mean of diabetes", mean_diabetes)
print("standard deviation of diabetics", std_dev_diabetics)
print("kurtosis of diabetics", kurtosis_diabetics)
# ... (More code for visualizations)
# Create a pair plot for the entire dataset
