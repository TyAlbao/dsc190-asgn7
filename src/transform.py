import pandas as pd

# import cleaned data
df = pd.read_csv('data/clean/events.csv')

# add date column
df['date'] = df['timestamp'].str[:10]

# save to transformed directory
df.to_csv('data/transformed/events.csv', index=False)
