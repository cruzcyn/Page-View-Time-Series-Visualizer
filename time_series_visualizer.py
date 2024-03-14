import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# TODO Import data
# (Make sure to parse dates. Consider setting index column to 'date'.)
df = None

# TODO Clean data
# Filter out days when page views were in the top 2.5% or bottom 2.5% of the dataset
df = None

# USE A COPY OF THE DF FOR EACH CHART.

# TODO Create draw_line_plot func.
# It has to use Matplotlib to draw a line chart similar to Figure_1
# The title should be: "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
# Label on x axis: "Date"
# Label on y axis: "Page Views"
def draw_line_plot():
    # Draw line plot





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


# TODO Create draw_bar_plot func
# The chart should be similar to Figure_2
# It should show average daily page views for each month grouped by year
# Legend should show month labels and have a title of "Months"
# Label on x axis: "Years"
# Label on y axis: "Average Page Views"
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


# TODO Create draw_box_plot func.
# Use Seaborn to draw two adjacent box plots similar to Figure_3
# The plots should show how the values are distributed within a given year or month and how it compares over time.
# Title of the first plot: "Year-wise Box Plot (Trend)"
# Title of the second plot: "Month-wise Box Plot (Seasonality)"
# Make sure month labels on bottom start at "Jan"
# Make sure x and y axes are labeled correctly.
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
