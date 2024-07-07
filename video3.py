import pandas as pd

data = {
    'name': ["John", "Jane", "Bob", "Alice", "Tom"],
    'gender': ["M", "F", "M", "F", "M"],
    'departament': ["HR", "Engineering", "Marketing", "Engineering", "HR"],
}

df = pd.DataFrame(data)#создаем датафрейм
df['gender'] = df['gender'].astype('category')#конвертируем в категорию
df['departament'] = df['departament'].astype('category')#конвертируем в категорию

df["departament"].cat.add_categories("Finance")#добавляем категорию

df["departament"] = df["departament"].cat.add_categories("Finance")#добавляем категорию
df["departament"] = df["departament"].cat.remove_categories("HR")#удаляем категорию
print(df["departament"].cat.categories)
print(df)