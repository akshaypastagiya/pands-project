# createdata.py
# This program is to separate the data of the iris dataset
# In this we will be saperate ot the iris data and assign to the array
# Author: Akshay Pastagiya

# Import Iris data to generate the summery of the data
import load_iris as li

def iris_data():
    # Gethred the iris data
    features,variables,iris_df = li.iris()

    # Transfer sepal length to a numpy array
    sepal_length = iris_df['sepal length'].values

    # Transfer sepal width to a numpy array
    sepal_width = iris_df['sepal width'].values

    # Transfer petal length to a numpy array
    petal_length = iris_df['petal length'].values

    # Transfer petal width to a numpy array
    petal_width = iris_df['petal width'].values

    # Transfer target to a numpy array
    targets = iris_df['targets'].values

    # Get Individual iris flower data
    iris_setosa = iris_df[iris_df['targets'] == 'Iris-setosa']
    iris_versicolor = iris_df[iris_df['targets'] == 'Iris-versicolor']
    iris_virginica = iris_df[iris_df['targets'] == 'Iris-virginica']

    return sepal_length, sepal_width, petal_length, petal_width, targets, iris_setosa, iris_versicolor, iris_virginica