import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import calendar

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset
# or bottom 2.5% of the dataset.
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(df.index, df['value'], color='r')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Group the data by year and month, and compute the mean of the page views for each group
    df_bar = df.groupby([df.index.year, df.index.month])["value"].mean().unstack()

    # Set the month names as the columns of the dataframe
    df_bar.columns = calendar.month_name[1:]

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(14, 6))
    df_bar.plot(kind="bar", ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(ncols=2, figsize=(20, 10))
    ax1 = sns.boxplot(x="year", y="value", data=df_box, ax=ax[0])
    ax2 = sns.boxplot(x="month", y="value", data=df_box, ax=ax[1], order=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
        'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ])

    # Set titles and axis labels
    ax1.set_title('Year-wise Box Plot (Trend)', fontsize=18)
    ax1.set_xlabel('Year', fontsize=16)
    ax1.set_ylabel('Page Views', fontsize=16)
    ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize=18)
    ax2.set_xlabel('Month', fontsize=16)
    ax2.set_ylabel('Page Views', fontsize=16)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
