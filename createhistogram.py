# createdata.py
# This program is to saperate the data of the iris dataset
# In this we will be saperate ot the iris data and assign to the array
# Aurthor: Akshay Pastagiya

# Import Iris data to generate the summery of the data
import load_iris as li
import histogram as hist

# Gethred the iris data
features,targets,variables,iris_df = li.iris()

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

hist.histplot(sepal_length,"sepal length")
hist.histplot(sepal_width,"sepal width")
hist.histplot(petal_length,"petal length")
hist.histplot(petal_width,"petal width")