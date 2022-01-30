import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

qb = pd.read_csv('qb.csv')
qb1 = qb.dropna(axis=1)

qb_new = qb1["att"] >= 300
qb_filter = qb[qb_new]

sns.set(style="darkgrid")
sns.set_context("talk")
sns.set(font_scale=0.7)
b = sns.relplot(x="fantasyPts", y="passYds300Games", style="player", hue= "player", size= "fantasyPts", data=qb_filter, kind="scatter", sizes=(10,225))
b.fig.suptitle("300 Yard Passing Games To Fantasy Points", fontsize=18)
plt.xlabel("Fantasy Points", fontsize=14)
plt.ylabel("300 Yard Passing Games", fontsize=14)
plt.show()