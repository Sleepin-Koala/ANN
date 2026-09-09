import numpy as np
from typing import List , Literal
from activation import Activation


class Neuron:
    """un neuronne simple : poids , biais , entrees (Pas vraiment utile , mais cest interressant)"""
    """simple neuron : weight , biais , input (not that useful, but interessing)"""


    def __init__(self , W: np.ndarray , B: float ,f) -> None:
        self.W = W
        self.B = B
        self.f = f

    def forward(self , inputs: np.ndarray) -> float:
        """forward pass d'un neuronne : c'est juste la sortie"""
        "the return value"
        z =  np.dot(inputs , self.W) + self.B
        return self.f(z)


t = 0

# W : [n_in , n_out]
class Layer:
    def __init__(self , W: np.ndarray, B: np.ndarray , f: Literal["relu","sigmoid","tanh","softmax","heaviside"]) -> None:
        self.W = W
        self.B = B
        self.f , self.f_derivative = Activation.get(f)

        self.z = None
        self.a = None
        self.inputs = None
        self.dw = None
        self.db = None

    def forward(self , inputs : np.ndarray) -> np.ndarray:
        self.inputs = inputs
        self.z = np.dot(inputs, self.W) + self.B

        self.a = self.f(self.z)
        return self.a

    def backward(self , error):
        assert self.inputs is not None

        m = self.inputs.shape[0]

        if self.f == Activation.softmax:
            dz = error
        else:
            da = error
            dz = np.multiply(da,  self.f_derivative(self.z)) # produit d'hadamard

        assert self.inputs is not None
        self.dw = (self.inputs.T @ dz) / m 
        self.db = np.sum(dz , axis = 0) / m

        dx = dz @ self.W.T


        return dx

    def update(self, learning_rate: float):
        """descente de gradient"""
        "gradient descent"
        assert self.dw is not None and self.db is not None
        self.W = self.W - learning_rate * self.dw
        self.B = self.B - learning_rate * self.db

        
        


class Network:
    def __init__(self , config: tuple , f: List) -> None:
        self.layers: List[Layer] = []

        for index , c in enumerate(config):
            W = np.random.randn(*c) * np.sqrt(2.0 / c[0]) 
            # passe per une distribution normale pour les valeurs oscillant entre -1 et 1 pour eviter lexplosion
            # use a normal distribution for getting values between  -1 et 1 for avoidign overflow
            B = np.zeros(c[1]) 

            self.layers.append(Layer(W , B , f[index]))

    def forward(self , X : np.ndarray):
        "forward pass"
        r = X
        for layer in self.layers:
            r = layer.forward(r)    
        return r

    def fit(self, X_train: np.ndarray , Y_train: np.ndarray , epochs: int , learning_rate: float , batch_size : int ):

        data =  X_train.shape[0]
        indexes = np.arange(data)

        for epoch in range(epochs):
            np.random.shuffle(indexes)

            X_shuffle = X_train[indexes]
            Y_shuffle = Y_train[indexes]


            for mini_batch in range(0 , data , batch_size):

                X = X_shuffle[ mini_batch : mini_batch + batch_size]
                Y = Y_shuffle[mini_batch : mini_batch + batch_size]

                f = self.forward(X)

                error = f - Y # softmax only - TODO : adapter - generaliser pour un modele polyvalent

                


                for layer in reversed(self.layers):
                    # if not np.all(np.isfinite(f)):
                    #     print("NaN détecté en sortie du forward, batch", mini_batch)
                    #     print("max/min de z par couche:", [ (layer.z.min(), layer.z.max()) for layer in self.layers])
                    #     break
                    error = layer.backward(error)

                for layer in self.layers:
                    layer.update(learning_rate)


            print(f"fin de {epoch+1}")



#vaut mieux entrer les valeurs en 2D
# i think - by my little experience in this ,  its better to enter data value in 2D (will seem to be evident for others but thats it)




