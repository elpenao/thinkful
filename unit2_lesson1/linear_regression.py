import pandas as pd
import matplotlib.pyplot as plt

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

# print loansData['FICO.Score'][0:10]

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()


