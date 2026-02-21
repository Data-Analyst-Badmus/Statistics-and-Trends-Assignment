"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""


from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots()
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):

 
    """
    plotting pie chart of pizza category
    by the total price
    """
    dfgrp_pizza = df.groupby('pizza_category.)['total_price'].sum()

    fig, ax = plt.subplots()
    dfgrp_pizza.plot(kind = 'pie', y = 'total_price', style={'dpi':144}, legend = False autopct = '%1.1f%%')
    plt.title('Pizza Category')                  
    plt.savefig('categorical_plot.png')                 
    return
                     

def plot_statistical_plot(df):
    """
    plotting box plot for the unit_price, total_price and quantity
    """
 
    fig, ax = plt.subplots()
               
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    mean =
    stddev =
    skew =
    excess_kurtosis =
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    # You should preprocess your data in this function and
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    return df


def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    # Delete the following options as appropriate for your data.
    # Not skewed and mesokurtic can be defined with asymmetries <-2 or >2.
    print('The data was right/left/not skewed and platy/meso/leptokurtic.')
    return


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = df[[col for col in df.columns if 'price' in col or 'quantity' in col]].copy()'<your chosen column for analysis>'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
