import numpy as np

class Activation:
    """
    A collection of activation functions and their derivatives,
    implemented from scratch with NumPy.
    """

    @staticmethod
    def heaviside(x: np.ndarray):
        return (x >= 0).astype("float32")

    @staticmethod
    def relu(x: np.ndarray) -> np.ndarray:
        """Rectified Linear Unit: max(0, x)"""
        return np.maximum(0, x)

    @staticmethod
    def relu_derivative(x: np.ndarray) -> np.ndarray:
        """Derivative of ReLU: 1 if x > 0 else 0"""
        return (x > 0).astype(float)

    @staticmethod
    def sigmoid(x: np.ndarray) -> np.ndarray:
        """Sigmoid (logistic) function: 1 / (1 + exp(-x))"""
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoid_derivative(x: np.ndarray) -> np.ndarray:
        """Derivative of sigmoid: sigmoid(x) * (1 - sigmoid(x))"""
        s = Activation.sigmoid(x)
        return s * (1 - s)

    @staticmethod
    def tanh(x: np.ndarray) -> np.ndarray:
        """Hyperbolic tangent: tanh(x)"""
        return np.tanh(x)

    @staticmethod
    def tanh_derivative(x: np.ndarray) -> np.ndarray:
        """Derivative of tanh: 1 - tanh(x)^2"""
        t = Activation.tanh(x)
        return 1 - t * t

    @staticmethod
    def softmax(x: np.ndarray):
        max_val = np.max(x , axis=-1 ,keepdims=True)
        exp_x = np.exp(x - max_val) 
        return exp_x / np.sum(exp_x , axis=-1, keepdims=True)


    @staticmethod
    def get(name: str):
        mapping = {
            'relu': (Activation.relu, Activation.relu_derivative),
            'heaviside': (Activation.heaviside, Activation.relu_derivative),
            'sigmoid': (Activation.sigmoid, Activation.sigmoid_derivative),
            'tanh': (Activation.tanh, Activation.tanh_derivative),
            'softmax': (Activation.softmax, None),
        }
        return mapping.get(name.lower(), (None, None))