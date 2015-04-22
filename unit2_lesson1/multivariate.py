import numpy as np
import pandas as pd
import statsmodels.api as sm
# import formula api as alias smf
import statsmodels.formula.api as smf

df = pd.read_csv('LoanStats3a.csv',header = 0, index_col=False)

cleanInterestRate = df['int_rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
df['int_rate'] = cleanInterestRate

df['home_own'] = 0
df.ix[df.home_ownership=="OWN", 'home_own'] = 1
df['rent'] = 0
df.ix[df.home_ownership=="RENT", 'rent'] = 1
df['mortgage'] = 0
df.ix[df.home_ownership=="MORTGAGE", 'mortgage'] = 1
df['none'] = 0
df.ix[df.home_ownership=="NONE", 'none'] = 1
df['other'] = 0
df.ix[df.home_ownership=="OTHER", 'other'] = 1


intrate = df['int_rate'].fillna(0)
annual_inc = df['annual_inc'].fillna(0)
home_own = df['home_own'].all()
rent = df['rent'].all()
mortgage = df['mortgage'].all()
none = df['none'].all()
other = df['other'].all()

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(annual_inc).transpose()
x2 = np.matrix(home_own).transpose()
x3 = np.matrix(rent).transpose()
x4 = np.matrix(mortgage).transpose()
x5 = np.matrix(none).transpose()
x6 = np.matrix(other).transpose()

# x = np.column_stack((x1,x2))
x = np.concatenate((x1,x2))

X = sm.add_constant(x)
est = sm.OLS(y, X).fit()

print est.summary()



