
## Read: http://aix1.uottawa.ca/~jkhoury/markov.htm
## Read: http://stackoverflow.com/questions/29763108/understanding-markov-chains-in-terms-of-matrix-multiplication

import pandas as pd
import numpy as np

df = pd.DataFrame({'1':[ .90,.15,.25], 
                   '2':[ .075,.80,.25],
                   '3': [.025,.05,.500]
                  }, 
                  index=["1", "2", "3"])
print "Original matrix"
print df
print "\n"

#2 Transitions
print df.dot(np.linalg.matrix_power(df,2))


#Full converged matrix
print df.dot(np.linalg.matrix_power(df,100))




