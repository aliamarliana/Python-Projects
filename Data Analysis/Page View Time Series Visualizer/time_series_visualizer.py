import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025))
            & (df['value'] <= df['value'].quantile(0.975))]
#df = df[df["value"].between(df["value"].quantile(0.025), df["value"].quantile(0.975))]


def draw_line_plot():
  # Draw line plot
  date = df.index
  value = df['value']
  plt.figure(figsize=(12, 6))
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  fig = plt.plot(date, value, color='red')
  plt.show()

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.groupby([df.index.year, df.index.month]).mean()
  df_bar = df_bar.unstack()
  df_bar.columns = [
      'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
      'September', 'October', 'November', 'December'
  ]
  df_bar.index.names = ['Years']

  # Draw bar plot
  fig = df_bar.plot(kind='bar',
                    figsize=(6, 14),
                    legend=True,
                    xlabel='Years',
                    ylabel='Average Page Views')
  plt.legend(loc='upper left', title='Months', fontsize='8')
  plt.show()

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
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

  # Year-wise Box Plot (Trend)
  color1 = sns.color_palette('deep',4)
  sns.boxplot(x='year', y='value', ax=ax1, data=df_box, palette=color1, hue='year', legend=False)
  ax1.set_title('Year-wise Box Plot (Trend)')
  ax1.set_xlabel('Year')
  ax1.set_ylabel('Page Views')

  #Moth-wise Box Plot (Seasonality)
  color2 = sns.color_palette('Set2', 12)
  sns.boxplot(x='month',
              y='value',
              ax=ax2,
              data=df_box,
              palette=color2,
              hue='month',
              legend=False)
  ax2.set_title('Month-wise Box Plot (Seasonality)')
  ax2.set_xlabel('Month')
  ax2.set_ylabel('Page Views')

  plt.show()
  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
