from sklearn import datasets as ds
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# carregando os dados do arquivo csv
data = pd.read_csv('Prostate_Cancer.csv')

# define X

X = data.index

#define y

y = data.values





# iris = ds.load_iris()

# # print(data)

# # print(iris)

# custom_data = {
#     'data': data[['radius', 'texture', 'perime', 'area', 'smoothness', 'compactness', 'concavity', 'concave points', 'symmetry', 'fractal dimension']].values,
#     'target': data['diagnosis_result'].apply(lambda x: 1 if x == 'M' else 0).values,  # Convertendo 'M' para 1 e 'B' para 0
#     'target_names': ['Benign', 'Malignant'],  # Nomes das classes
#     'feature_names': ['radius', 'texture', 'perime', 'area', 'smoothness', 'compactness', 'concavity', 'concave points', 'symmetry', 'fractal dimension']
# }
    
# custom_iris = ds.base.Bunch(**custom_data)

plot_pd = pd.plotting.scatter_matrix(data)

knn = KNeighborsClassifier(n_neighbors= 6)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)



# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()
