"""
Saves, loads and cleans data
"""

import pandas as pd

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
