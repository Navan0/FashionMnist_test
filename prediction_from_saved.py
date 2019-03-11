from model import 
from prediction import prediction
from keras.models import load_model
model = load_model('my_model_weights.h5')
test_image = x_test[3].reshape([1,28,28])
result = model.predict(test_image)
result = result.argmax()
print(prediction(result))
