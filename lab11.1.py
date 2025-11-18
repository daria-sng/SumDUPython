import pandas as pd

df = pd.DataFrame({
    'Elizabeth Nelson': [10, 11, 8, 9, 7, 10, 12, 8, 9, 11],
    'Joe Allen': [11, 2, 10, 8, 9, 11, 12, 8, 9, 10],
    'Alice Rivera': [8, 9, 7, 6, 10, 11, 9, 10, 11, 9],
    'Jacob Martin': [2, 4, 9, 2, 7, 6, 4, 2, 6, 8],
    'Sarah Bailey': [10, 11, 11, 12, 10, 11, 9, 10, 11, 12],
    'Peter Johnson': [7, 9, 10, 4, 10, 11, 9, 10, 8, 9],
    'Helen Adams': [10, 11, 12, 8, 9, 11, 12, 7, 10, 11],
    'Steven White': [9, 8, 7, 10, 11, 12, 8, 9, 11, 11],
    'Michelle Baker': [9, 6, 2, 6, 7, 9, 10, 11, 8, 9],
    'Harry Williams': [10, 2, 8, 6, 4, 10, 9, 8, 10, 11]
},
index = range(1, 11))

print(f"{'DataFrame':^140}\n{df}")
# Базовий аналіз даних
print(f"\nBasic data analysis\n1. First tree rows of DataFrame:\n{df.head(3)}")
print(f"\n2. Data types:\n{df.dtypes}\n\n3. Numbers of rows and columns: {df.shape}\n\n4. Descriptive statistics:\n{df.describe()}")

# Додавання нового стовпця - загальна кількість оцінок (10-12) за один день 
df["High Scores 10-12"] = ((df >= 10) & (df <= 12)).sum(axis = 1)
print(f"\nDataFrame after adding new data:\n{'DataFrame':^140}\n{df}")

# Фільтрація даних - учні, які отримували 2 бали 
filtration = df.loc[:, df.min() == 2].iloc[:, :-1]
print(f"\nFiltered DataFrame:\n{"Students with score of 2":^56}\n{filtration}")

# Сортування даних - сортування по спаданню за стовпчиком "High Scores 10-12" 
sorting = df.sort_values(df.columns[-1], ascending=False) 
print(f"\nSorted DataFrame in descending order by \"High Scores 10-12\" values:\n{'DataFrame':^140}\n{sorting}")

# Групування даних + знаходження середнього значення по класах
DFtransposition = df.iloc[:, :-1].T
print(f"\nDataFrame grouping:\n{"Transposed DataFrame":^57}\n{DFtransposition}")

classes = ["11-A", "11-B", "10-A", "11-A", "11-B", "11-A", "11-B", "10-A", "11-B", "10-A"]
DFtransposition["Class"] = classes
print(f"\nTransposed DataFrame after adding a new column \"Class\":\n{"Transposed DataFrame":^62}\n{DFtransposition}")

grouping = DFtransposition.groupby("Class").mean().round(1)
print(f"\nGrouped DataFrame with average values found:\n{"Grouped DataFrame":^35}\n{grouping.T}")

# Додаткові операції агрегації 
# Визначення кількості учнів у кожному класі
print(f"\nAdditional aggregation operations:\nNumber of students in each class:\n{DFtransposition.groupby("Class").size()}")

# Знаходження класу з максимальним середнім балом 
class_mean = grouping.mean(axis=1)
topclass = class_mean.idxmax()
print(f"\nClass with the highest average score: {topclass} ( {class_mean.max():.1f} )")

# Виявлення стабільності учня 
print(f"\nStudent stability:\n{df.iloc[:,:-1].std().round(1)}\n*Explanation: smaller value - stability is observed (scores are close to each other)")
