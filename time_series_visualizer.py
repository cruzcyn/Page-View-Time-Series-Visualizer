import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# READ DATA
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=0, parse_dates=["date"])

# CLEAN DATA
# Filter out values (which represent page views) that are above or below the top and bottom
# 2.5% of the dataset respectively.
df = df[(df["value"] >= (df["value"].quantile(0.025))) & 
        (df["value"] <= (df["value"].quantile(0.975)))]

# USE A COPY OF THE DF FOR EACH CHART.

# DRAW LINE PLOT
def draw_line_plot():
    # Make copy of df
    line_df = df

    # Draw line plot
    fig = plt.figure(figsize=(12,6))
    plt.plot(line_df.index, line_df["value"])
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig.figure


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
