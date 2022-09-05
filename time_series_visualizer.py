import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
raw=pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'],index_col='date')

# Clean data
df = raw[(raw['value']>raw['value'].quantile(0.025))&(raw['value']<raw['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.plot(df.index,df['value'],'r',linewidth=1)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df2=df.copy()
    df2['month']=df.index.month
    df2['year']=df.index.year
    # modify the data Set
    df_bar=df2.groupby(['year','month'])['value'].mean()
    df_bar=df_bar.unstack()
    df_bar.columns =['January','February','March','April','May','June','July','August','September','October','November','December']
    # Draw bar plot
    fig=df_bar.plot(kind='bar',figsize=(13,6),xlabel='Years',ylabel='Average Page Views',fontsize=8).figure
    plt.legend( loc='upper left', title='Months')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box=df.copy()
    df_box.reset_index(inplace=True)
    #如果唔reset index,個日期既data會係index, 咁就要 df.index 而非df.date
    #if reset_index個inplace係False,個index係唔會轉
    df_box['year']=[d.year for d in df_box.date]
    df_box['month']=[d.strftime('%b') for d in df_box.date]
    #line3-4加個'year'同'month' 的columns比df_box.
    #month個到轉成str while adding as column
    df_box['month_number']=[d.month for d in df_box.date]
    df_box=df_box.sort_values('month_number')
    #排order 由1月-12月
    df_box

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(nrows=1, ncols=2,figsize=(20,6))
    sns.boxplot(x='year',y='value',data=df_box,ax=axs[0],width=0.8,fliersize=1,linewidth=1).set(xlabel='Year',ylabel='Page Views',title='Year-wise Box Plot (Trend)')
    sns.boxplot(x="month", y="value", data=df_box,ax=axs[1],fliersize=1,linewidth=1).set(xlabel='Month',ylabel='Page Views',title='Month-wise Box Plot (Seasonality)')





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
