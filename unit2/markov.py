
## Read: http://aix1.uottawa.ca/~jkhoury/markov.htm
## Read: http://stackoverflow.com/questions/29763108/understanding-markov-chains-in-terms-of-matrix-multiplication

import pandas as pd
import numpy as np

df = pd.DataFrame({'rainy': [.4, .7], 
                   'sunny': [.6, .3]
                  }, 
                  index=["rainy", "sunny"])
print "Original matrix"
print df
print "\n"

print "matrix dot product"
print df.dot(df)
print "\n"

print "matrix dot dot product"
print df.dot(df).dot(df)
print "\n"

# Elementwise multiplication of two dataframes
print df.mul(df)

# Elementwise multiplication of two dataframes
print df ** 2