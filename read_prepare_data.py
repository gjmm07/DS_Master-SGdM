# Central script to read the data from hard-drive
# Do not read in another script to ensure to have the same data source

import pandas as pd
import numpy as np
import os


def read_population():
    df = pd.read_csv(os.path.join("Data", "worldcitiespop.csv"), usecols=["Population"])
    data = df["Population"].to_numpy()
    data = data[~np.isnan(data)]  # drop Nan values
    data = data[data > 10]  # drop "cities" with less than 10 inhabitants -- allow comparison of 2nd digit
    return data


def read_height():
    df = pd.read_csv(os.path.join("Data", "SOCR-HeightWeight.csv"), usecols=["Height(Inches)"])
    data = df.to_numpy() * 100000  # include valid digits after decimal
    data *= 2.54  # convert to cm
    return data


if __name__ == "__main__":
    read_population()
