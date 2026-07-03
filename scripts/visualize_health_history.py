"""
Visualize the cleaned health history data (HRV, RHR, sleep) built by
parse_health_export.py.

Produces:
- A time series plot per metric with a 7-day rolling average overlay
- A correlation matrix between HRV, RHR, and sleep
- Printed descriptive statistics

Usage:
    python scripts/visualize_health_history.py
"""

import os

import matplotlib.pyplot as plt
import pandas as pd

INPUT_PATH = "data/health_history.csv"
OUTPUT_DIR = "data/plots"


def load_data(path):
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.sort_values("date").set_index("date")
    return df


def add_rolling_averages(df, window=7):
    for column in ["hrv", "rhr", "sleep"]:
        df[f"{column}_rolling"] = df[column].rolling(window=window, min_periods=3).mean()
    return df


def plot_metric(df, column, ylabel, color, output_path):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.scatter(df.index, df[column], s=8, alpha=0.3, color=color, label="Daily value")
    ax.plot(df.index, df[f"{column}_rolling"], color=color, linewidth=2, label="7-day rolling average")
    ax.set_ylabel(ylabel)
    ax.set_title(f"{ylabel} over time")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=120)
    plt.close(fig)


def print_correlations(df):
    corr = df[["hrv", "rhr", "sleep"]].corr()
    print("\nCorrelation matrix (HRV / RHR / sleep):")
    print(corr.round(2))


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = load_data(INPUT_PATH)
    df = add_rolling_averages(df)

    print(f"Loaded {len(df)} days from {INPUT_PATH}")
    print(f"Date range: {df.index.min().date()} to {df.index.max().date()}")
    print("\nDescriptive statistics:")
    print(df[["hrv", "rhr", "sleep"]].describe().round(2))

    print_correlations(df)

    plot_metric(df, "hrv", "HRV (ms)", "tab:blue", f"{OUTPUT_DIR}/hrv_over_time.png")
    plot_metric(df, "rhr", "Resting Heart Rate (bpm)", "tab:red", f"{OUTPUT_DIR}/rhr_over_time.png")
    plot_metric(df, "sleep", "Sleep (hours)", "tab:green", f"{OUTPUT_DIR}/sleep_over_time.png")

    print(f"\nSaved plots to {OUTPUT_DIR}/")
