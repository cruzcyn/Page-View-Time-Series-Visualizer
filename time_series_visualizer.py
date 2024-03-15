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
df = df[(df["value"] > (df["value"].quantile(0.025))) & 
        (df["value"] < (df["value"].quantile(0.975)))]


def draw_line_plot():
    # Make copy of df
    line_df = df.copy()

    # Draw line plot
    fig = plt.figure(figsize=(12,6))
    plt.plot(line_df.index, line_df["value"])
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar.reset_index(inplace=True)
    df_bar["year"] = df_bar["date"].dt.year
    df_bar["month"] = df_bar["date"].dt.month
    df_bar = df_bar.groupby(["year", "month"], as_index=False).agg({"value": pd.Series.mean})

    # Draw bar plot
    fig = sns.catplot(data=df_bar,
                      x="year", y="value", 
                      kind="bar",
                      hue="month",
                      palette="tab10",
                      legend=False)
    
    fig.set_xlabels("Years")
    fig.set_ylabels("Average Page Views")

    plt.legend(labels=["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December"], 
                       title="Months")
    plt.xticks(rotation=90)

    fig = fig.figure

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

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
