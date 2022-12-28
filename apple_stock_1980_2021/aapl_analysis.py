import polars as pl 
import seaborn as sns 
import pyarrow as pa
import matplotlib.pyplot as plt
import matplotlib

aapl_df = pl.read_csv('AAPL.csv')

# Open
# It is the price at which the financial security opens in the market when trading begins.

# High
#The high is the highest price at which a stock traded during a period.

# Low
# The low is the lowest price at which a stock traded during a period.

# Close
# Closing price generally refers to the last price at which a stock trades during a regular trading session.

# Adj Close 
# The adjusted closing price amends a stock's closing price to reflect that stock's value after accounting.

# Volume
# Volume measures the number of shares traded in a stock or contracts traded in futures or options.

# So first, it would be a good idea to compare the variance between open, highs and lows of each day
# then, assist this plot with volume, so we get to know if there is a relation between volume variance and
# stock price variance during the day.
# p1-p0 / p0

aapl_df = aapl_df.with_columns(
    [
        (((pl.col('High')) - pl.col('Open')) / pl.col('Open')).alias('HighGain'),
        (((pl.col('Low')) - pl.col('Open')) / pl.col('Open')).alias('LowGain'),
    ]
)

aapl_df = aapl_df.with_columns(
    [
        ((pl.col('HighGain') + pl.col('LowGain'))/ 2).alias("AvgGain"),
    ]
)

aapl_df = aapl_df.to_pandas()

# Now, we should plot this in actually to tell what is going on:
matplotlib.rc_file_defaults()
axis1 = sns.set_style(style=None, rc=None)
fig, axis1 = plt.subplots(figsize=(16, 6))

g = sns.lineplot(x='Date', y='AvgGain', data=aapl_df, ax=axis1)
axis2 = axis1.twinx()
g = sns.barplot(x='Date', y='Volume', data=aapl_df, ax=axis2)
plt.show()
