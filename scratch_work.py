import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import marimo as mo

    return mo, pd


@app.cell
def _(pd):
    raw = pd.read_csv('data/raw/events.csv')
    return (raw,)


@app.cell
def _(raw):
    raw.head()
    return


@app.cell
def _(raw):
    raw['event_type'].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # clean
    """)
    return


@app.cell
def _(raw):
    df = raw[~raw.isna().any(axis=1)]
    df
    return (df,)


@app.cell
def _(df, pd):
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed').dt.strftime("%Y-%m-%dT%H:%M:%S")
    return


@app.cell
def _(df):
    df_clean = df[df['duration_seconds'] > 0]
    return (df_clean,)


@app.cell
def _(df_clean):
    df_full = df_clean[df_clean['event_type'].isin({'click','login','purchase','scroll','view'})]
    return (df_full,)


@app.cell
def _(df_full):
    df_full
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # transform
    """)
    return


@app.cell
def _(df_full):
    df_full['date'] = df_full['timestamp'].str[:10]
    return


@app.cell
def _(df_full):
    df_full
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # features
    """)
    return


@app.cell
def _(df_full):
    df_full['duration_minutes'] = (df_full['duration_seconds'] / 60).astype(int)
    return


@app.cell
def _(df_full):
    df_full[['duration_seconds', 'duration_minutes']]
    return


@app.cell
def _(df_full, pd):
    df_full['weekday'] = pd.to_datetime(df_full['timestamp']).dt.day_name()
    return


@app.cell
def _(df_full):
    df_full
    return


if __name__ == "__main__":
    app.run()
