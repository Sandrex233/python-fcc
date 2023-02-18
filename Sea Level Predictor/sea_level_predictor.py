import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 6))

    ax.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    x1 = np.arange(1880, 2051)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    y1 = intercept + slope * x1
    ax.plot(x1, y1, color='r', label=f'Linear Fit ({slope:.2f})')

    # Create second line of best fit
    df_recent = df.loc[df['Year'] >= 2000]
    x2 = np.arange(2000, 2051)
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    y2 = intercept2 + slope2 * x2

    ax.plot(x2, y2, color='g', label=f'Linear Fit 2000-Now ({slope2:.2f})')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
