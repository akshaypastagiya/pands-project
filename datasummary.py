# This code is to get the data summery of the iris dataset.
# To get the datasummery of the dataset we have used the ucimlrepo
# Using pands we will explore the data stracture of the datasets
# Given dataframe to the load iris dataset we have used pands
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

import load_iris as li
import pandas as pd
features,targets,variables = li.iris()
print(features)
#Create a dataframe of the iris dataset
iris_df = features
iris_df['targets'] = targets
print(iris_df)

# Get the summery of the dataset we will be using pands shape command
# shape is return a tuple representing the dimensionality of the DataFrame.

print(f"Shape of the dataset: \n {iris_df.shape}")

# pands dtypes function we will get the data type of each column.

print(f"Data type of the dataset:\n{iris_df.dtypes}")

print(f"Feature of the dataset:\n{variables.head(4)['name']}")

print(f"Target class of the dataset:\n{variables.iloc[4]['description']}")

#calculate mean of dataset
print(f"Mean of the dataset:\n{iris_df.mean(numeric_only = True)}")

# Find the minimum value of the dataset
print(f"Minimum value of the dataset:\n{iris_df.min(numeric_only = True)}")

# Find the maximum value of the dataset
print(f"Maximum value of the dataset:\n{iris_df.max(numeric_only = True)}")

#print the standard deviation of the dataset
print(f"Standard deviation of the dataset:\n{iris_df.std(numeric_only = True)}")

#print the median of the dataset
print(f"Median of the dataset:\n{iris_df.median(numeric_only = True)}")