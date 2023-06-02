import numpy as np
import matplotlib.pyplot as plt
import os
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

imgSize = 256

train_ds = tf.keras.utils.image_dataset_from_directory(
    "workers",
    validation_split=0.2,
    subset="training",
    seed=1,
    image_size=(imgSize, imgSize)
)

val_ds = tf.keras.utils.image_dataset_from_directory(
     "workers",
    validation_split=0.2,
    subset="validation",
    seed=1,
    image_size=(imgSize, imgSize)
)

data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal",input_shape=(imgSize,imgSize,3)),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])


model = tf.keras.models.Sequential([
    data_augmentation,
    layers.Rescaling(1./255, input_shape=(imgSize, imgSize, 3)),    
    layers.Conv2D(16, 5, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 5, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 5, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(2)
])
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

hist = model.fit(train_ds, validation_data=val_ds, epochs=10)

acc = hist.history['accuracy']
val_acc = hist.history['val_accuracy']

plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

loss = hist.history['loss']
val_loss = hist.history['val_loss']

plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.title('Training and Validation Losses')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

model.export("model")