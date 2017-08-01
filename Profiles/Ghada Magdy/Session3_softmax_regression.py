from data_reader.reader import CsvReader
from util import *
import numpy as np
import matplotlib.pyplot as plt
import copy as cp


class SoftmaxRegression(object):
    def __init__(self, learning_rate=0.01, epochs=50):
        self.__epochs= epochs
        self.__learning_rate = learning_rate

    def fit(self, X, y):
        self.w_ = np.zeros((X.shape[1], X.shape[1]))
        self.b = np.ones((1, X.shape[1]))
        self.cost_ = []

        for i in range(self.__epochs):
            # 1- Calculate the net input W^T * x

               res = self.__net_input(X, self.w_, self.b)
            # 2- Get the activation using Softmax function
               sft = self.__activation(res)
            # 3- Calculate the gradient
               err = (y - sft)
               grd = X.T.dot(err)
            # 4- Update the weights and bias using the gradient and learning rate
               self.b = self.b + self.__learning_rate *err.sum()
               self.w_ = self.w_ + self.__learning_rate * grd
            # 5- Uncomment the cost collecting line

               self.cost_.append(self.__cost(self._cross_entropy(output=sft, y_target=y)))

    def _cross_entropy(self, output, y_target):
        return -np.sum(np.log(output) * (y_target), axis=1)

    def __cost(self, cross_entropy):
        return 0.5 * np.mean(cross_entropy)

    def __softmax(self, z):
        return (np.exp(z.T) / np.sum(np.exp(z), axis=1)).T

    def __net_input(self, X, W, b):
        return (X.dot(W) + b)

    def __activation(self, X):
        return self.__softmax(X)

    def predict(self, X):
        # 1- Calculate the net input W^T * x
            net_in = X.dot(self.w_)
        # 2- Return the corresponding one-hot vector for each testing item
            act = self.__activation(net_in)
            indx = 0
            mx = -1
            vec = np.zeros(act.shape)
            #print(act)
            for i in range (0,act.shape[0]):
                for j in act[i]:
                  if j > mx:
                    indx+=1
                    mx = j
                if not(mx == -1):
                   vec[i][indx-1] = 1
                indx = 0
                mx = -1
            return vec


        #pass

reader = CsvReader("./data/Iris.csv")

iris_features, iris_labels = reader.get_iris_data()

print(len(iris_features))
print(len(iris_labels))

iris_features, iris_labels = shuffle(iris_features, iris_labels)
iris_labels = to_onehot(iris_labels)

train_x, train_y, test_x, test_y = iris_features[0:139], iris_labels[0:139], iris_features[139:], iris_labels[139:]
train_x, train_y, test_x, test_y = np.asarray(train_x), np.asarray(train_y), np.asarray(test_x), np.asarray(test_y)

train_x, means, stds = standardize(train_x)
test_x = standardize(test_x, means, stds)

lr = SoftmaxRegression(learning_rate=0.001, epochs=500)
lr.fit(train_x, train_y)

plt.plot(range(1, len(lr.cost_) + 1), np.log10(lr.cost_))
plt.xlabel('Epochs')
plt.ylabel('Cost')
plt.title('Softmax Regression - Learning rate 0.02')

plt.tight_layout()
plt.show()

predicted_test = np.asarray(lr.predict(test_x))

print("Test Accuracy: " + str(((sum([np.array_equal(predicted_test[i], test_y[i]) for i in range(0, len(predicted_test))]) / len(predicted_test)) * 100.0)) + "%")
