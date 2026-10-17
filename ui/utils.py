import numpy as np
from PIL import Image
import joblib
from network.ann import Network


def load_model(path="modele.npz"):
    data = np.load(path , allow_pickle=True)
    model = Network(config=((784,512),(512,256),(256,10)), f= ["relu" ,"relu" ,"softmax"]) 
    model.layers = data["layers"]
    return model

def formater_pourcentage(p):
    pct = p * 100
    if pct < 0.01:
        return "< 0.01 %"
    return f"{pct:.2f} %"

def get_input(image):
    img = image.resize((28, 28), Image.LANCZOS)
    x = np.array(img, dtype=np.float32) / 255.0   # valeurs entre 0 et 1
    result = load_model().forward(x.reshape(1, 784))
    ma = max(result.flatten())

    confiance = ma * 100
    num = list(result.flatten()).index(ma)
    return confiance , num




# def find_number(canvas):
#     x = canvas.get_input()
#     pred = f.predict(x)   # adapte au nom de ta méthode
#     self.result_number.configure(text=str(pred))
