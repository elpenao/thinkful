import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()

data = [i.split(', ') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

mean = df['Alcohol'].mean()
mean = str(mean)
print "alcohol mean: " + mean
median = df['Alcohol'].median() 
median = str(median)
print "alcohol median " + median

# If all numbers occur equally often, stats.mode() will return the smallest number
mode = stats.mode(df['Alcohol'])[0][0]
print "alcohol mode: ", mode

tmean = df['Tobacco'].mean()[0][0]
print "tobacco mean: ", tmean

tmedian = df['Tobacco'].median()[0][0]
print "tobacco median: ", tmedian

tmode = stats.mode(df['Tobacco'])[0][0]
tmode = str(tmode)
print "tobacco mode: ", tmode

arange = max(df['Alcohol']) - min(df['Alcohol'])
print "alcohol range: " + str(arange)

astd = df['Alcohol'].std() 
print "alcohol std: " + str(astd)

avar = df['Alcohol'].var() 
print "alcohol var: " + str(avar)

trange = max(df['Tobacco']) - min(df['Tobacco'])
print "tobacco range: " + str(trange)

tstd = df['Tobacco'].std() 
print "tobacco std: " + str(tstd)

tvar = df['Tobacco'].var() 
print "tobacco var: " + str(tvar)



