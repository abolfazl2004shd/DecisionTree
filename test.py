import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

def antropy(y: np.ndarray) -> float:
    val,counts = np.unique(y, return_counts=True)
    
    all = counts.sum()
    probabilities = counts / all
    
    result = -np.sum(probabilities * np.log2(probabilities))
    return result

y = ['yes' , 'no', 'no' , 'yes', 'yes', 'no', 'no', 'yes']

print(antropy(y))