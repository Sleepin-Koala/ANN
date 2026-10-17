

from network.ann import Network
from network.activation import Activation
from keras.datasets import mnist 
from keras.utils import to_categorical
import numpy as np


##data 
(X_train_data,Y_train_data),(X_test_data,Y_test_data) = mnist.load_data()
X_train = X_train_data.astype("float32") / 255.0
X_test = X_test_data.astype("float32") / 255.0
Y_train = to_categorical(Y_train_data , num_classes=10)
X_train = X_train.reshape(X_train.shape[0] , 784)

f = Network(config=((784,512),(512,256),(256,10)), 
            f= ["relu" ,"relu" ,"softmax"])

f.fit(X_train , Y_train , epochs=40 , learning_rate=0.1, batch_size=32)
np.savez("modele.npz", layers = f.layers)




