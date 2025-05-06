# histogram.py
# This program is to generate the histogram
# This will be define as a function
# Where we will pass the information of the data and it will generate the histogram in to png file
# Aurthor: Akshay Pastagiya

# Import matplotlib function to plot the histogram 
import matplotlib.pyplot as plt
def histplot(data,columnname):
    
    plt.figure()
    plt.hist(data)
    plt.xlabel(columnname)
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {columnname}")
    plt.savefig(f"Histogram_{columnname}.png")
