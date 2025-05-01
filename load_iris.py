# This Program is to load iris database
# To load the data base we have used ucimlrepo
# please refer below link to load the iris data set
# https://archive.ics.uci.edu/dataset/53/iris
# Given dataframe to the load iris dataset we have used pands
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

from ucimlrepo import fetch_ucirepo 
import pandas as pd
def iris():
    # fetch dataset 
    iris = fetch_ucirepo(id=53) 

    # assign the dataframe to the data set
    iris_df = pd.DataFrame(data = iris.data.original, columns=iris.variables['name'])
    iris_df['target'] = iris.target

    # get the shape of the data set
    print("Shape of the dataset:", iris_df.shape)
    return[iris, iris_df]