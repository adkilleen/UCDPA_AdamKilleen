import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

qb = pd.read_csv('qb.csv')
qb1 = qb.dropna(axis=1)

qb_new = qb1["att"] >= 300
qb_filter = qb[qb_new]
#print(qb_filter)

sns.set(style="darkgrid")
sns.set_context("talk")
sns.set(font_scale=0.7)
b = sns.relplot(x="fantasyPts", y="rushCarries", style="player", size = "rushCarries", hue= "player", data=qb_filter, kind="scatter", sizes=(10,225))
b.fig.suptitle("Rush Carries To Fantasy Points")
plt.xlabel("Fantasy Points", fontsize=14)
plt.ylabel("Rushing Carries", fontsize=14)
plt.show()