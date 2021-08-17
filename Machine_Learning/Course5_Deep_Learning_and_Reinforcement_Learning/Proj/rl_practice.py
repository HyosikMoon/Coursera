import tensorflow as tf
from tensorflow.keras import models, layers

# optimizer = tf.keras.optimizers.RMSprop(0.001)

def build_model1():
    model = models.Sequential()
    model.add(layers.Dense(64, activation = 'relu', input_shape=(x_mat.shape[1], )))
#     model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model

model1 = build_model1()
model1.fit(x_mat, y, epochs = 50)