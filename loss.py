import numpy as np

class Loss:

    def __init__(self) -> None:
        pass

    def categorical_cross_entropy(y_pred: np.ndarray, y_true: np.ndarray): # type: ignore
        epsilon = 1e-9
        y_pred_clipped = np.clip(y_pred, epsilon, 1.0 - epsilon)
        summ = -np.sum(y_true * np.log(y_pred_clipped) ,axis=1)

        return np.mean(summ)
    



