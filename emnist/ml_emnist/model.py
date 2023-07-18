
import numpy as np
from tensorflow import keras
from keras import Model, layers, models
from keras.callbacks import EarlyStopping

def initialize_model(input_shape: tuple = (28,28,1)) -> Model:
    """
    Initialize the Neural Network
    """
    model = models.Sequential()

    model.add(layers.Conv2D(8, (4,4), input_shape=input_shape, activation="relu", padding="same"))
    model.add(layers.MaxPool2D(pool_size=(2,2)))

    model.add(layers.Conv2D(64, (3,3), activation="relu"))
    model.add(layers.MaxPool2D(pool_size=(2,2)))

    model.add(layers.Conv2D(32, (3,3), activation="relu"))
    model.add(layers.MaxPool2D(pool_size=(2,2)))

    model.add(layers.Flatten())
    model.add(layers.Dense(47, activation="relu"))
    model.add(layers.Dense(47, activation="softmax"))

    print("✅ model initialized")

    """
    Compile the Neural Network
    """
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    print("✅ model compiled")

    return model


def train_model(model: Model,
                X: np.ndarray,
                y: np.ndarray,
                batch_size=32,
                epochs=100,
                patience=20,
                retore_best_weights=True,
                validation_data=None, # overrides validation_split
                validation_split=0.2,
                verbose=0) -> tuple[Model, dict]:
    """
    Fit model and return a the tuple (fitted_model, history)
    """
    es = EarlyStopping(monitor="val_loss",
                       patience=patience,
                       restore_best_weights=retore_best_weights,
                       verbose=1)

    history = model.fit(X,
                        y,
                        validation_data=validation_data,
                        validation_split=validation_split,
                        epochs=epochs,
                        batch_size=batch_size,
                        callbacks=[es],
                        verbose=verbose)

    print(f"✅ model trained")

    return model, history
