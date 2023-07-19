## First trained run to save model

from emnist.ml_emnist.model import initialize_model, train_model
from emnist.ml_emnist.data import data_prep
from tensorflow import keras
from keras import Model

#init model
mod_init = initialize_model()

#get train data
X_train, y_train = data_prep()[0], data_prep()[2]

#train model
mod = train_model(mod_init, X_train, y_train, verbose=1)

#save h5 mod
mod.save("current_mod", "h5")
