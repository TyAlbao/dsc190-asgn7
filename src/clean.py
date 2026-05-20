import pandas as pd

raw = pd.read_csv('data/raw/events.csv')

# drop any nan values
df = raw.dropna().copy()

# normalize timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed').dt.strftime("%Y-%m-%dT%H:%M:%S")

# drop non-positive duration seconds
df = df[df['duration_seconds'] > 0]

# drop invalid events
df = df[df['event_type'].isin({'click','login','purchase','scroll','view'})]

# save to cleaned directory
df.to_csv('data/clean/events.csv', index=False)
