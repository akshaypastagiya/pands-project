# This code is to get the data summary of the iris dataset.
# To get the datasummery of the dataset we have used the ucimlrepo
# Using pands we will explore the data stracture of the datasets
# Given dataframe to the load iris dataset we have used pands
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

# Import Iris data to generate the summery of the data
import load_iris as li
# Import Iris data
import createdata as data
# Import histogram to create the histogram of the data
import plot as plt
# Import pands function to gethred the data summary data
import pandas as pd
# Import custome write function to write the summury data
import writefile as wf
# Import socket function to check the internet connectivity
import socket

# To run this module required internet.
# 1st need to check internet connectivityis there or not to run the module
# https://docs.python.org/3/library/socket.html#socket.socket.connect

def check_internet_connection():
    try:
      # Try to ping the server to check the internet connectivity
      socket.create_connection(("8.8.8.8", 53), timeout=3)
      return True
    except OSError:
      return False
    socket.close()
if check_internet_connection():
   print("Internet is connected.")
else:
   print("Internet is not connected.")
   exit()


# Gethred the iris dataset
features,variables,iris_df = li.iris()
# Gethred the iris data
sepal_length, sepal_width, petal_length, petal_width, targets, iris_setosa, iris_versicolor, iris_virginica = data.iris_data()

# Get file name of the file where we need to write down the summury of the data in to text file
filename = "summary.txt"

# Step 1: Get the summery of the dataset we will be using pands shape command
# shape is return a tuple representing the dimensionality of the DataFrame.
data_summary = f"Shape of the dataset: \n {iris_df.shape}\n"

# pands dtypes function we will get the data type of each column.
data_summary += f"\n Data type of the dataset:\n{iris_df.dtypes}\n"

# Gether the feture names of the data set
data_summary += f"\nFeature of the dataset:\n{variables.head(4)['name']}\n"

# Gether the tagrate class of the data set
data_summary += f"\nTarget class of the dataset:\n{variables.iloc[4]['description']}\n"

#calculate mean of dataset
data_summary += f"\nMean of the dataset:\n{iris_df.mean(numeric_only = True)}\n"

# Find the minimum value of the dataset
data_summary = data_summary + f"\nMinimum value of the dataset:\n{iris_df.min(numeric_only = True)}\n"

# Find the maximum value of the dataset
data_summary += f"\nMaximum value of the dataset:\n{iris_df.max(numeric_only = True)}\n"

#print the standard deviation of the dataset
data_summary = data_summary + f"\nStandard deviation of the dataset:\n{iris_df.std(numeric_only = True)}\n"

#print the median of the dataset
data_summary += f"\nMedian of the dataset:\n{iris_df.median(numeric_only = True)}\n"

# Write data in to text file
wf.write(filename,data_summary)

# Step 2: Generate histogram
# Histogram give you a graph showing frequency distributions. 
# It is a graph showing the number of observations within each given interval.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist

plt.histplot(sepal_length,"sepal length")
plt.histplot(sepal_width,"sepal width")
plt.histplot(petal_length,"petal length")
plt.histplot(petal_width,"petal width")

# Step3: Generate Scatter Plot
# Scatter plot is a graph where each value in the data set is represented by a dot.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter

plt.scaplot(sepal_length,sepal_width,"sepal length","sepal width")
plt.scaplot(petal_length,petal_width,"petal length","petal width")
plt.scaplot(sepal_length,petal_length,"sepal length","petal length")
plt.scaplot(sepal_width,petal_width,"sepal width","petal width")
print("Plot saved")

# Step4: Additional Analysis of the iris data set
# Created box plot for addtional analysis of the dataset.
# Box plot gived you the summury of the dataset like  including minimum, first quartile, median, third quartile and maximum
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html

import matplotlib.pyplot as plt1
plt1.figure()
plt1.subplot()
plt1.boxplot([iris_setosa['sepal length'],iris_versicolor['sepal length'],iris_virginica['sepal length']], label = ['Setosa', 'Versicolor', 'Virginica'])
plt1.xlabel('Iris Species')
plt1.ylabel('Sepal Length(cm)')
plt1.savefig('Boxplot Sepal Length.png')
plt1.close()
plt1.boxplot([iris_setosa['petal length'],iris_versicolor['petal length'],iris_virginica['petal length']], label = ['Setosa', 'Versicolor', 'Virginica'])
plt1.xlabel('Iris Species')
plt1.ylabel('Petal Length(cm)')
plt1.savefig('Boxplot Petal Length.png')
plt1.close()
plt1.boxplot([iris_setosa['sepal width'],iris_versicolor['sepal width'],iris_virginica['sepal width']], label = ['Setosa', 'Versicolor', 'Virginica'])
plt1.xlabel('Iris Species')
plt1.ylabel('Sepal width(cm)')
plt1.savefig('Boxplot Sepal width.png')
plt1.close()
plt1.boxplot([iris_setosa['petal width'],iris_versicolor['petal width'],iris_virginica['petal width']], label = ['Setosa', 'Versicolor', 'Virginica'])
plt1.xlabel('Iris Species')
plt1.ylabel('Petal width(cm)')
plt1.savefig('Boxplot Sepal width.png')
plt1.close()