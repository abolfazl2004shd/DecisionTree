# import sys
# sys.path.append('..')
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
#from decision_tree import MultiNodeCategoricalDecisionTree


def load_dataset():
    df = pd.read_csv('corona_tested_006.csv')  # Use the cleaned DataFrame
    return df

data = load_dataset()

print(data)