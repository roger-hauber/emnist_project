"""
Saves, loads and cleans data
"""

import pandas as pd
import numpy as np

def create_mapping() -> pd.DataFrame: #TO DO: add path as a variable?
    """
    reads mapping file as dataframe and adds "translated" label as "char" variable,
    returns dataframe with label, ascii, char:
    label is in data,
    ascii is the corresponding unicode code,
    char is the "translation"
    """
    mapping = pd.read_csv("../../data/emnist-balanced-mapping.txt", sep=" ", header=None)
    mapping = mapping.rename(columns={0: "label", 1: "ascii"})
    mapping.loc[:, "char"] = mapping.ascii.apply(chr)

    return mapping

def data_prep(filepath="../../data/") -> \
    tuple[np.ndarray, np.ndarray,  np.ndarray, np.ndarray]:
        """
        takes all the original data in idx format and preps them for
        model training:
        train_img is the array of train set images
        test_img is the array of test set images
        train_lab_enc is the one hot encoded array of train set labels
        test_lab_enc is the array of one hot encoded test set labels
        """
        #necessary imports
        import idx2numpy
        from keras.utils import to_categorical
        import numpy as np

        #loading data
        train_img = idx2numpy.convert_from_file(
            filepath+"emnist-balanced-train-images-idx3-ubyte")
        test_img = idx2numpy.convert_from_file(
            filepath+"emnist-balanced-test-images-idx3-ubyte")

        train_lab = idx2numpy.convert_from_file(
            filepath+"emnist-balanced-train-labels-idx1-ubyte")
        test_lab = idx2numpy.convert_from_file(
            filepath+"emnist-balanced-test-labels-idx1-ubyte")

        ### Encode label arrays
        train_lab_enc = to_categorical(train_lab)
        test_lab_enc = to_categorical(test_lab)

        ### Prep of image arrays
        # reshape and normalize
        train_img = np.reshape(train_img, (-1, 28, 28, 1))/255
        test_img = np.reshape(test_img, (-1, 28, 28, 1))/255

        # transpose tilted img data
        train_img = np.transpose(train_img, (0, 2, 1, 3))
        test_img = np.transpose(test_img, (0, 2, 1, 3))

        return train_img, test_img, train_lab_enc, test_lab_enc
