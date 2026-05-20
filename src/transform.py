from pathlib import Path
import pandas as pd

Path("data/transformed").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/clean/events.csv")

df["date"] = df["timestamp"].str[:10]

df.to_csv("data/transformed/events.csv", index=False)