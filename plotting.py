import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Users\\larsg\\Desktop\\Data\\Data17_31_14.csv', index_col='Time', parse_dates=True)
print(df.head())
sns.lineplot(data=df)
plt.show()