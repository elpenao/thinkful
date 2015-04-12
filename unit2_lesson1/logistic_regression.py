import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate

cleanLoanLength = loansData['Loan.Length'].map(lambda y: int(y.rstrip(' months')))
loansData['Loan.Length'] = cleanLoanLength

cleanFico = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFico = cleanFico.map(lambda z:[int(n) for n in z])
simpleFico = [score[0] for score in cleanFico]
loansData['FICO.Score'] = simpleFico

loansData['lessthan12'] = loansData['Interest.Rate'].map(lambda x: True if x < 0.12 else False)
#print loansData['lessthan12'][1:10]
loansData['constant'] = [1 for i in simpleFico]

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']
lessthan12 = loansData['lessthan12']
loanLength = loansData['Loan.Length']
constant = loansData['constant']

ind_vars = ['Interest.Rate','Amount.Requested','FICO.Score','Loan.Length','constant']

logit = sm.Logit(loansData['lessthan12'], loansData[ind_vars])

result = logit.fit()

coeff = result.params
print coeff

