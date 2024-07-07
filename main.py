import pandas as pd

data = {
    "набор А": [85,90,95,100,105,],
    "набор Б": [70,80,95,110,120]
}

df = pd.DataFrame(data)

stdA = df["набор А"].std() # Вычисляем cтандартное отклонение, для набора А
stdB = df["набор Б"].std() # Вычисляем стандартное отклонение, для набора Б

print(f"Cтандартное отклонение для набора А: {stdA} \nCтандартное отклонение для набора Б: {stdB}")
