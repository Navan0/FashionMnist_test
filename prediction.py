from model import *
import matplotlib.pyplot as plt

image_index = 8
pred = model.predict(x_test[image_index].reshape(1, 28, 28))
pred = pred.argmax()
def prediction(pred):
    if pred == 0:
        print("T-shirt/top")
    elif pred == 1:
        print("Trouser")
    elif pred == 2:
        print("Pullover")
    elif pred == 3:
        print("Dress")
    elif pred == 4:
        print("Coat")
    elif pred == 5:
        print("Sandal")
    elif pred == 6:
        print("Shirt")
    elif pred == 7:
        print("Sneaker")
    elif pred == 8:
        print("Bag")
    elif pred == 9:
        print("Ankle boot")
model.save('my_model_weights.h5')
