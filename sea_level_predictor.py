import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    fl_bf = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    years_ext1 = list(range(1880, 2051))
    plt.plot(years_ext1, [fl_bf.slope * year + fl_bf.intercept for year in years_ext1], color="yellow")
   
    # Create second line of best fit
    mask = df['Year']>=2000
    years_ext2 = list(range(2000, 2051))
    sl_bf = linregress(df[mask]['Year'], df[mask]['CSIRO Adjusted Sea Level'])
    plt.plot(years_ext2, [sl_bf.slope * year + sl_bf.intercept for year in years_ext2], color='red')
    # Add labels and title
    
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()