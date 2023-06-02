import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import sklearn as sk
import sklearn.multiclass
import sklearn.model_selection
import sklearn.linear_model
from sklearn.datasets import fetch_openml

trafficSigns = fetch_openml("GTSRB-HueHist")

X = trafficSigns.data
Y = trafficSigns.target

X_train, X_test, Y_train, Y_test = sk.model_selection.train_test_split(X, Y, train_size=0.8)

# преобразование данных в нужный формат
#X_train = X_train.reshape((X_train.shape[0], 3, 32, 32))
#X_test = X_test.reshape((X_test.shape[0], 3, 32, 32))

# нормализация данных
X_train /= 255.0
X_test /= 255.0

# преобразование меток классов в нужный формат
#Y_train = tf.keras.utils.to_categorical(Y_train, 43)
#Y_test = tf.keras.utils.to_categorical(Y_test, 43)

# создание модели сверточной нейронной сети
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(16,16,3)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(43, activation='softmax')
])

# компиляция модели
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# обучение модели
history = model.fit(X_train, Y_train, epochs=10, validation_data=(X_test, Y_test))

# оценка точности модели на тестовых данных
test_loss, test_acc = model.evaluate(X_test, Y_test)
print('Test accuracy:', test_acc)

# визуализация процесса обучения
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(10)

plt.figure(figsize=(15, 15))
plt.subplot(2, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(2, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()