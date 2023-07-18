"""
Saves, loads and cleans data
"""

import pandas as pd

def create_mapping(filepath='../../data/') -> pd.DataFrame:
    """
    reads mapping file as dataframe and adds "translated" label as "char" variable,
    returns dataframe with label, ascii, char:
    label is in data,
    ascii is the corresponding unicode code,
    char is the "translation"
    """
    mapping = pd.read_csv(filepath+"emnist-balanced-mapping.txt", sep=" ", header=None)
    mapping = mapping.rename(columns={0: "label", 1: "ascii"})
    mapping.loc[:, "char"] = mapping.ascii.apply(chr)

    return mapping
