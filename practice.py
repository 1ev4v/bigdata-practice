import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/bike_data.csv')
# df.info()
df = df[df['season']==1]
df['datetime'] = pd.to_datetime(df['datetime'])
# df.info()
df['hour'] = df['datetime'].dt.hour
print(df.groupby('hour')['count'].sum().max())

# import pandas as pd
# df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/bike_data.csv')

# df = df.astype({'datetime' : 'datetime64[ns]', 'weather' : 'int64', 'season' : 'object', 'workingday' : 'object', 'holiday' : 'object'})
# df_sub = df.loc[df['season'] == 1, ]

# df_sub['hour'] = df_sub['datetime'].dt.hour

# summary_data = df_sub.groupby(['season', 'hour']).agg({'count': 'sum'}).reset_index()

# max_count_hour = summary_data.loc[summary_data['count'].idxmax(), 'hour']
# max_count = summary_data['count'].max()

# print(f"count가 가장 큰 hour는 {max_count_hour}시이며, 대여량은 {max_count}입니다.")
