from pathlib import Path

import tensorflow as tf
from tensorflow import keras as ks

from configs import app_settings
from gather_data import gather_data


def build_model(train, validation):
    """This will create and save a model"""
    model = ks.models.Sequential()
    layers = ks.layers
    model.add(
        layers.Conv2D(16, (3, 3),
                      1,
                      activation="relu",
                      input_shape=(256, 256, 3)))
    model.add(layers.MaxPool2D())
    model.add(layers.Conv2D(16, (3, 3), 1, activation="relu"))
    model.add(layers.MaxPool2D())
    model.add(layers.Conv2D(32, (3, 3), 1, activation="elu"))
    model.add(layers.MaxPool2D())
    model.add(layers.Conv2D(32, (3, 3), 1, activation="relu"))
    model.add(layers.MaxPool2D())
    model.add(layers.Conv2D(16, (3, 3), 1, activation="relu"))
    model.add(layers.MaxPool2D())
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation="relu"))
    model.add(layers.Dense(256, activation="elu"))
    model.add(layers.Dense(256, activation="relu"))
    model.add(layers.Dense(256, activation="elu"))
    model.add(layers.Dense(256, activation="relu"))
    model.add(layers.Dense(1, activation="sigmoid"))

    model.compile("adam",
                  loss=tf.losses.BinaryCrossentropy(),
                  metrics=["accuracy"])

    model.summary()

    callback = ks.callbacks.TensorBoard(log_dir=app_settings.log_dir)

    model.fit(train,
              epochs=app_settings.reps,
              validation_data=validation,
              callbacks=callback)

    model.save(app_settings.save_file)


if __name__ == '__main__':
    t, v = gather_data(Path(app_settings.data_dir), app_settings.training_size)
    build_model(t, v)
