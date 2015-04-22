import numpy as np
import pandas as pd
import statsmodels.api as sm
# import formula api as alias smf
import statsmodels.formula.api as smf

df = pd.read_csv('LoanStats3a.csv',header = 0, index_col=False)

cleanInterestRate = df['int_rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
df['int_rate'] = cleanInterestRate

df['home_own'] = 0
df.loc[('home_ownership' == "OWN"), 'home_own'] = 1

intrate = df['int_rate'].fillna(0)
annual_inc = df['annual_inc'].fillna(0)
home_own = df['home_own']

print home_own[:200]

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(annual_inc).transpose()
x2 = np.matrix(home_own).transpose()

X = sm.add_constant(x1,x2)
est = sm.OLS(y, X).fit()

print est.summary()



