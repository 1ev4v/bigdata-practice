# p68 1번
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a+5)


# p68 2번
import numpy as np

a = np.array([12, 21, 35, 48, 5])
print(a[::2])


# p68 3번
import numpy as np

a = np.array([1, 22, 93, 64, 54])
print(a.max())


# p68 4번
import numpy as np

a = np.array([1, 2, 3, 2, 4, 5, 4, 6])
a = np.unique(a)
print(a)


# p68 5번
import numpy as np

a = np.array([21, 31, 58])
b = np.array([24, 44, 67])
c = []

min_len = min(len(a), len(b))

for i in range(min_len):
    c.append(a[i])
    c.append(b[i])

if len(a) > min_len:
    c.extend(a[min_len:])
elif len(b) > min_len:
    c.extend(b[min_len:])

print(c)


# import numpy as np

# a = np.array([21, 31, 58])
# b = np.array([24, 44, 67])
# c = np.empty(len(a) + len(b), a.dtype)
# c[0::2] = a
# c[1::2] = b
# print(c)


# p68 6번
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9])

print(a[:-1] + b)


# p83 1번
import numpy as np

result = np.array([[3, 5, 7], [2, 3, 6]])
print(result)


# p83 2번
import numpy as np

a = np.array([[8,10,7,8,],[2,4,5,5],[7,6,1,7],[2,6,8,6],[9,3,4,2]])

result = np.array([a[1],a[3],a[4]])
print(result)


# p83 3번
import numpy as np

a = np.array([[8,10,7,8],[2,4,5,5],[7,6,1,7],[2,6,8,6],[9,3,4,2]])

result = np.empty((0, a.shape[1]))
for i in range(len(a)):
    if a[i][2] > 3:
        result = np.append(result, [a[i]], axis=0)
print(result)


# p83 4번
import numpy as np

a = np.array([[8,10,7,8],[2,4,5,5],[7,6,1,7],[2,6,8,6],[9,3,4,2]])
b = np.sum(a, axis=1)
print(a.shape)
result = np.empty((0, a.shape[1]))
for i in range(len(b)):
    if b[i] >= 20:
        result = np.append(result, [a[i]], axis=0)
print(result)


# p84 5번
import numpy as np

a = np.array([[8,10,7,8],[2,4,5,5],[7,6,1,7],[2,6,8,6],[9,3,4,2]])
b = np.mean(a, axis=0)
result = np.where(b >=5)[0]
print(result)


# p84 6번
import numpy as np

a = np.array([[8,10,7,8],[2,4,5,5],[7,6,1,7],[2,6,8,6],[9,3,4,2]])
result = np.empty((0, a.shape[1]), dtype=int)
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i][j] >= 7:
            result = np.append(result, [a[i]], axis=0)
            break
# print(a)
print(result)


# p146 1번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
df.info()


# p146 2번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
print(df[df['midterm'] >= 85])


# p146 3번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
print(df.sort_values(by='final', ascending=False).head(5))
# print(df.sort_values(by='final', ascending=False).head(5).loc[:, ['name', 'final']])


# p146 4번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
print(df.groupby('gender')[['midterm', 'final']].mean())


# p147 5번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
df['student_id'] = df['student_id'].astype(str)
print(df.info())


# p147 6번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
print(df[df['assignment'] == df['assignment'].max()])
print(df[df['assignment'] == df['assignment'].min()])
# print(df[df['assignment'] > df['assignment'].mean()]['assignment'].mean())


# p147 7번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
df['average'] = df[['midterm', 'final', 'assignment']].mean(axis=1)
print(df.head(5))


# p147 8번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
# print(df.isna().sum())
df = df.dropna()
# print(df)
df.info()


# p147 9번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')

additional_data = {
    'student_id': ['1', '3', '5', '7', '9'],
    'club': ['Art', 'Science', 'Math', 'Music', 'Drama']
}
df_additional = pd.DataFrame(additional_data)

df['student_id'] = df['student_id'].astype(str)
rs = pd.merge(df, df_additional, on='student_id', how='left')
print(rs)


# p148 10번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
df['average'] = df[['midterm', 'final', 'assignment']].mean(axis=1)
df = pd.pivot_table(
    df,
    index='gender',
    columns='student_id',
    values='average'
)
print(df)


# p148 11번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
df['average'] = df[['midterm', 'final', 'assignment']].mean(axis=1)
df = df.groupby('gender')[['assignment', 'average', 'final', 'midterm']].mean()
print(df) 


# p148 12번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
df['average'] = df[['midterm', 'final', 'assignment']].mean(axis=1)
rs = df[df['average'] == df['average'].max()]
print(rs)


# p166 1번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/bike_data.csv')
# print(df)
df.info()