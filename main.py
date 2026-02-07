import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import sklearn as sk
import seaborn as sb

from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler



data = datasets.load_iris()

print(data)