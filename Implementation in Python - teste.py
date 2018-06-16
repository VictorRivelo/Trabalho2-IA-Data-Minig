Implementation in Python from scratch


# Importing libraries
import pandas as pd
import numpy as np
import math
import operator
#### Start of STEP 1
# Importing data 
data = pd.read_csv("train.csv")
#### End of STEP 1

#coleta as primeiras N linhas do arquivo de entrada 
data.head() 