from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.utils.np_utils import to_categorical
import numpy as np

X_list = [[0, 0], [1, 1], [0, 0], [1, 1], [1, 1], [1, 1]]
Y_list = [0, 1, 0, 1, 1, 1]

X = np.array(X_list)
Y = to_categorical(Y_list)

model = Sequential()
model.add(Dense(input_dim=2, output_dim=10))
model.add(Activation("relu"))
model.add(Dense(output_dim=2))
model.add(Activation("softmax"))
model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

model.fit(X, Y, nb_epoch=3000, batch_size=32)

results = model.predict_proba(np.array([[1,1], [0,0]]))
print("Predict:¥n", results)