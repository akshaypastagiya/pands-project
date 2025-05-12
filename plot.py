# histogram.py
# This program is to generate the histogram
# This will be define as a function
# Where we will pass the information of the data and it will generate the histogram in to png file
# Author: Akshay Pastagiya

# Import matplotlib function to plot the histogram 
import matplotlib.pyplot as plt

def histplot(data,columnname):
    
    plt.figure()
    plt.hist(data)
    plt.xlabel(columnname)
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {columnname}")
    plt.savefig(f"Histogram_{columnname}.png")
    plt.close()

def scaplot(xaxis,yaxis,xcolumn_name,ycolumn_name):
    plt.figure()
    plt.scatter(xaxis,yaxis)
    plt.xlabel(xcolumn_name)
    plt.xlabel(xcolumn_name)
    plt.title(f"Scatter plot of {xcolumn_name} vs {ycolumn_name}")
    plt.savefig(f"Scatter_{xcolumn_name}_{ycolumn_name}.png")
    plt.close()