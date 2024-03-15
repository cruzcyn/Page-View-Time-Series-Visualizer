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
    line_df = df.copy()

    # Draw line plot
    fig = plt.figure(figsize=(12,6))
    plt.plot(line_df.index, line_df["value"])
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig.figure


# DRAW BAR PLOT
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar["year"] = df.index.year
    df_bar["month"] = df.index.month
    df_bar = df_bar.groupby(["year", "month"], as_index=False).agg({"value": pd.Series.mean})

    # Draw bar plot
    fig = sns.barplot(data=df_bar, 
                           x="year", y="value", 
                           hue="month", 
                           palette="tab10")

    plt.legend(title="Months")

    plt.xlabel("Years")
    plt.xticks(rotation=90)

    plt.ylabel("Average Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig.figure


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
    fig, (box_1, box_2) = plt.subplots(1,2, figsize=(13,5))

    # FIRST PLOT
    box_1 = sns.boxplot(data=df_box, 
                    x="year", y="value", 
                    hue="year", palette="tab10", 
                    legend=False, ax=box_1)

    box_1.set_title("Year-wise Box Plot (Trend)")

    box_1.set_xlabel("Year")
    box_1.set_ylabel("Page Views")

    # SECOND PLOT
    box_2 = sns.boxplot(data=df_box,
                    x="month", y="value",
                    order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                    hue="month", palette="husl",
                    legend=False, ax=box_2)
    box_2.set_title("Month-wise Box Plot (Seasonality)")
    box_2.set_xlabel("Month")
    box_2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig.figure
