from pathlib import Path
import pandas as pd

Path("data/features").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/transformed/events.csv")

df["duration_minutes"] = (df["duration_seconds"] / 60).astype(int)
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

df.to_csv("data/features/events.csv", index=False)