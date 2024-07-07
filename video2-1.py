import pandas as pd
import matplotlib.pyplot as plt

data = {"value": [1,2,2,3,3,3,4,4,4,4,5,6,7,8,9,10,55]}

df = pd.DataFrame(data)

# df['value'].plot.hist(bins=10)
df.boxplot(column='value')
plt.show()

q1 = df['value'].quantile(0.25)
q3 = df['value'].quantile(0.75)
iqr = q3 - q1

downside = q1 - 1.5 * iqr
upside = q3 + 1.5 * iqr
print(f"Нижняя граница: {downside}")
print(f"Верхняя граница: {upside}")

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]
df_new.boxplot(column='value')
plt.show()