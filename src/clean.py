from pathlib import Path
import pandas as pd

VALID_EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}

Path("data/clean").mkdir(parents=True, exist_ok=True)

raw = pd.read_csv("data/raw/events.csv")

df = raw.dropna().copy()

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    format="mixed",
    errors="coerce",
).dt.strftime("%Y-%m-%dT%H:%M:%S")

df = df.dropna(subset=["timestamp"])

df = df[df["duration_seconds"] > 0]

df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

df.to_csv("data/clean/events.csv", index=False)