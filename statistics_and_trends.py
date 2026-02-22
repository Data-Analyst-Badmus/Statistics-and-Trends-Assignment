"""
Global Water Consumption - Statistics and Trends Analysis

This script performs preprocessing, visualization, and statistical
analysis on a global water consumption dataset.

The dataset includes:
- Country
- Total Water Consumption (Billion m3)
- Per Capita Water Use (L/Day)
- Agricultural Water Use (%)
- Industrial Water Use (%)
- Household Water Use (%)
- Rainfall Impact (mm)
- Groundwater Depletion Rate (%)
- Water Scarcity Level
- Year (index)

The script produces:
1. Relational plot
2. Categorical plot
3. Statistical distribution plot
4. Descriptive statistical moments
"""

from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    """
    Creates a relational scatter plot showing the relationship
    between Rainfall Impact and Groundwater Depletion Rate.
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.scatterplot(
        data=df,
        x="Rainfall Impact (mm)",
        y="Groundwater Depletion Rate (%)",
        hue="Water Scarcity Level",
        palette="viridis",
        ax=ax
    )

    ax.set_title("Rainfall vs Groundwater Depletion")
    ax.set_xlabel("Rainfall Impact (mm)")
    ax.set_ylabel("Groundwater Depletion Rate (%)")
    ax.legend(title="Water Scarcity Level")

    plt.tight_layout()
    plt.savefig("relational_plot.png")
    plt.close()


def plot_categorical_plot(df):
    """
    Creates a categorical bar plot showing average
    Total Water Consumption per Water Scarcity Level.
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    grouped = df.groupby("Water Scarcity Level")[
        "Total Water Consumption (Billion m3)"
    ].mean().reset_index()

    sns.barplot(
        data=grouped,
        x="Water Scarcity Level",
        y="Total Water Consumption (Billion m3)",
        palette="magma",
        ax=ax
    )

    ax.set_title("Average Total Water Consumption by Scarcity Level")
    ax.set_xlabel("Water Scarcity Level")
    ax.set_ylabel("Avg Total Water Consumption (Billion m3)")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("categorical_plot.png")
    plt.close()


def plot_statistical_plot(df):
    """
    Creates a histogram with KDE for
    Per Capita Water Use.
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.histplot(
        df["Per Capita Water Use (L/Day)"],
        kde=True,
        bins=30,
        color="steelblue",
        ax=ax
    )

    ax.set_title("Distribution of Per Capita Water Use")
    ax.set_xlabel("Per Capita Water Use (L/Day)")
    ax.set_ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("statistical_plot.png")
    plt.close()


def statistical_analysis(df, col: str):
    """
    Computes statistical moments for a selected column.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataset.
    col : str
        Column name to analyze.

    Returns
    -------
    tuple
        Mean, standard deviation, skewness, excess kurtosis.
    """

    data = df[col].dropna()

    mean = np.mean(data)
    stddev = np.std(data, ddof=1)
    skew = ss.skew(data)
    excess_kurtosis = ss.kurtosis(data)

    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    """
    Cleans and prepares the dataset.

    - Sets Year as index
    - Removes missing values
    - Prints summary statistics
    - Displays correlation matrix
    """

    # Set Year as index
    if "Year" in df.columns:
        df = df.set_index("Year")

    # Remove duplicates
    df = df.drop_duplicates()

    # Drop missing values
    df = df.dropna()

    # Quick exploration
    print("\nDataset Head:\n", df.head())
    print("\nDataset Description:\n", df.describe())
    print("\nCorrelation Matrix:\n", df.corr(numeric_only=True))

    return df


def writing(moments, col):
    """
    Prints statistical interpretation of results.
    """

    print(f"\nFor the attribute {col}:")
    print(
        f"Mean = {moments[0]:.2f}, "
        f"Standard Deviation = {moments[1]:.2f}, "
        f"Skewness = {moments[2]:.2f}, and "
        f"Excess Kurtosis = {moments[3]:.2f}."
    )

    # Skewness interpretation
    if moments[2] > 0.5:
        skew_text = "right-skewed"
    elif moments[2] < -0.5:
        skew_text = "left-skewed"
    else:
        skew_text = "approximately symmetric"

    # Kurtosis interpretation
    if moments[3] > 1:
        kurt_text = "leptokurtic (heavy-tailed)"
    elif moments[3] < -1:
        kurt_text = "platykurtic (light-tailed)"
    else:
        kurt_text = "mesokurtic (normal-like)"

    print(f"The data is {skew_text} and {kurt_text}.")


def main():
    """
    Main execution function.
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
