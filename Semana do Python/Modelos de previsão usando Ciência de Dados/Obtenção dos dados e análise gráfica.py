import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(os.path.join(os.path.dirname(__file__), "advertising.csv"))
print(df)

print(df.info())

sns.pairplot(df)
plt.show()

sns.heatmap(df.corr(), cmap='Wistia', annot=True)
plt.show()