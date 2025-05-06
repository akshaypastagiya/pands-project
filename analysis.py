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
plt.histplot(sepal_length,"sepal length")
plt.histplot(sepal_width,"sepal width")
plt.histplot(petal_length,"petal length")
plt.histplot(petal_width,"petal width")

# Step3: Generate Scatter Plot
plt.scaplot(sepal_length,sepal_width,"sepal length","sepal width")
plt.scaplot(petal_length,petal_width,"petal length","petal width")
plt.scaplot(sepal_length,petal_length,"sepal length","petal length")
plt.scaplot(sepal_width,petal_width,"sepal width","petal width")
print("Plot saved")

# Step3: Generate Scatter Plot
import matplotlib.pyplot as plt1
plt1.figure()
plt1.subplot()
plt1.boxplot([iris_setosa['sepal length'],iris_versicolor['sepal length'],iris_virginica['sepal length']])
plt1.savefig('boxplot1.png')
plt1.close()