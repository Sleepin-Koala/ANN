import numpy as np
from PIL import Image
from network.ann import Network


def load_model(path="modele.npz"):
    data = np.load(path , allow_pickle=True)
    model = Network(config=((784,512),(512,256),(256,10)), f= ["relu" ,"relu" ,"softmax"]) 
    model.layers = data["layers"]
    return model

def get_input(image):
    img = image.resize((28, 28), Image.LANCZOS)
    x = np.array(img, dtype=np.float32) / 255.0 
    result = load_model().forward(x.reshape(1, 784))
    ma = max(result.flatten())
    confiance = ma * 100
    num = list(result.flatten()).index(ma)
    return confiance , num
