# This Program is to load iris database
# To load the data base we have used ucimlrepo
# please refer below link to load the iris data set
# https://archive.ics.uci.edu/dataset/53/iris


from ucimlrepo import fetch_ucirepo 

def iris():
    # fetch dataset 
    iris = fetch_ucirepo(id=53) 

    #get iris data of the datase
    features = iris.data.features
    targets = iris.data.targets
    variables = iris.variables
            
    # return the iris dataset data and variable
    return features,targets,variables

iris()