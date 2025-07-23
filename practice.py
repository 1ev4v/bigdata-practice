import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/logdata.csv')
# df.info()
df['year'] = df['로그'].str[:4]
print(df)

다른 방법 있음 그거 할꺼임