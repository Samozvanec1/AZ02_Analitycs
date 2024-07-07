import pandas as pd

data = {
    "Возраст": [23, 22, 21, 27, 23, 20, 29, 28, 22, 25,],
    "Зарплата": [42500, 23600, 24700, 27800, 82900, 53000, 73100, 33200, 63300, 23400,]
}

df = pd.DataFrame(data)


#rint(df.describe())

print(f"Средний возраст:{df['Возраст'].mean()}")

print(f"Медианный возраст:{df['Возраст'].median()}")

print(f"Стандартный отклонение Возраста:{df['Возраст'].std()}", end="\n\n")

print(f"Средняя зарплата:{df['Зарплата'].mean()}")

print(f"Медианная зарплата:{df['Зарплата'].median()}")

print(f"Стандартное отклонение Зарплаты:{df['Зарплата'].std()}")


