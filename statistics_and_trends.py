"""
Statistics and Trends Assignment
Global Water Consumption (2000–2025)

Panel dataset:
Countries observed annually from 2000 to 2025.
Total rows: 3900

This script performs:
- Data preprocessing
- Relational, categorical and statistical plots
- Statistical moment analysis
"""

from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    """
    Scatter plot:
    Rainfall Impact vs Groundwater Depletion Rate.
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.scatterplot(
        data=df.reset_index(),
        x="Rainfall Impact (mm)",
        y="Groundwater Depletion Rate (%)",
        hue="Water Scarcity Level",
        alpha=0.6,
        palette="viridis",
        ax=ax
    )

    ax.set_title("Rainfall vs Groundwater Depletion (2000–2025)")
    ax.set_xlabel("Rainfall Impact (mm)")
    ax.set_ylabel("Groundwater Depletion Rate (%)")

    plt.tight_layout()
    plt.savefig("relational_plot.png", dpi=300)
    plt.close()


def plot_categorical_plot(df):
    """
    Bar plot:
    Average agricultural water use by scarcity level.
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    grouped = (
        df.reset_index()
        .groupby("Water Scarcity Level")["Agricultural Water Use (%)"]
        .mean()
        .reset_index()
    )

    sns.barplot(
        data=grouped,
        x="Water Scarcity Level",
        y="Agricultural Water Use (%)",
        palette="coolwarm",
        ax=ax
    )

    ax.set_title("Average Agricultural Water Use by Scarcity Level")
    ax.set_xlabel("Water Scarcity Level")
    ax.set_ylabel("Average Agricultural Water Use (%)")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("categorical_plot.png", dpi=300)
    plt.close()


def plot_statistical_plot(df):
    """
    Time-series plot:
    Global average Total Water Consumption over time.
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    yearly_avg = (
        df.reset_index()
        .groupby("Year")["Total Water Consumption (Billion m3)"]
        .mean()
    )

    yearly_avg.plot(ax=ax)

    ax.set_title("Global Average Total Water Consumption (2000–2025)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Total Water Consumption (Billion m3)")

    plt.tight_layout()
    plt.savefig("statistical_plot.png", dpi=300)
    plt.close()


def statistical_analysis(df, col: str):
    """
    Compute mean, standard deviation, skewness and excess kurtosis.
    """

    data = df[col].dropna()

    mean = np.mean(data)
    stddev = np.std(data, ddof=1)
    skew = ss.skew(data)
    excess_kurtosis = ss.kurtosis(data)

    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    """
    Preprocess dataset:

    - Convert Year to integer
    - Set MultiIndex (Country, Year)
    - Remove duplicates
    - Drop missing values
    - Display summary and correlation
    """

    df["Year"] = df["Year"].astype(int)

    df = df.set_index(["Country", "Year"])

    df = df.drop_duplicates()
    df = df.dropna()

    print("\nHead:\n", df.head())
    print("\nDescription:\n", df.describe())
    print("\nCorrelation Matrix:\n", df.corr(numeric_only=True))

    return df


def writing(moments, col):
    """
    Interpret statistical moments.
    """

    print(f"\nFor the attribute {col}:")
    print(f"Mean = {moments[0]:.2f}, "
          f"Standard Deviation = {moments[1]:.2f}, "
          f"Skewness = {moments[2]:.2f}, "
          f"Excess Kurtosis = {moments[3]:.2f}.")

    if moments[2] > 0.5:
        skew_text = "right skewed"
    elif moments[2] < -0.5:
        skew_text = "left skewed"
    else:
        skew_text = "approximately symmetric"

    if moments[3] > 1:
        kurt_text = "leptokurtic"
    elif moments[3] < -1:
        kurt_text = "platykurtic"
    else:
        kurt_text = "mesokurtic"

    print(f"The data was {skew_text} and {kurt_text}.")


def main():
    """
    Main function.
    """

    df = pd.read_csv("data.csv")

    df = preprocessing(df)

    col = "Per Capita Water Use (L/Day)"

    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)

    moments = statistical_analysis(df, col)
    writing(moments, col)


if __name__ == "__main__":
    main()
