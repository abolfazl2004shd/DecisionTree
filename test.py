import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

# def gini(y: np.ndarray) -> float:
#     val,counts = np.unique(y ,return_counts=True)
#     all = counts.sum()
#     probabilities = counts / all
    
#     result = 1 - np.sum(np.pow(probabilities , 2))
#     return result

# y = ['yes' , 'no', 'no' , 'yes', 'yes', 'no', 'no', 'no']
# X = 
# print(gini(y))



X = np.array([
    [0, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, 0]
])

y = np.array([0, 0, 1, 1, 0])

feature = X[:,1]
vals,counts = np.unique(feature , return_counts=True)

all = counts.sum()
result = 0.0

for v,c in (vals, counts):
cur_y = y[v]

            
# print(vals ,counts)
# print(all)