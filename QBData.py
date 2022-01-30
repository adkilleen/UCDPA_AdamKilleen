import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

qb = pd.read_csv('qb.csv')
qb1 = qb.dropna(axis=1)
#print(qb1.head())
#print(qb1.info())
#print(qb1.describe().T)
#print(qb1.isnull().sum())
#print(qb1.corr())