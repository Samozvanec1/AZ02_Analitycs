import pandas as pd
import numpy as np

data = pd.date_range(start="2022-07-26", periods=10,freq="D")

value = np.random.randn(10)

df = pd.DataFrame({'Date': data, 'value': value})
df.set_index('Date', inplace=True)
print(df)

month = df.resample('ME').mean() # рассчитываем среднее значение по месяцам
print(month)