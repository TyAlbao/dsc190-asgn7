import pandas as pd

# read data in
df = pd.read_csv('data/transformed/events.csv')

# add duration in minutes
df['duration_minutes'] = df['duration_seconds'] / 60

# add weekday
df['weekday'] = pd.to_datetime(df['timestamp']).dt.day_name()

# save data to features directory
df.to_csv('data/features/events.csv', index=False)
