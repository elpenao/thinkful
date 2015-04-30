import pandas as pd
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('LoanStats3b.csv', header=0, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

print loan_count_summary

loan_count_summary.plot(figsize=(12,8));
plt.show()

fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(loan_count_summary)
plt.show()
fig = sm.graphics.tsa.plot_pacf(loan_count_summary)
plt.show()