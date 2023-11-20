import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import warnings


class RealDataBenfordLaw:
    # Expect the data to be in the 10-positional system
    # todo: implement other systems?
    # todo: implement pre checks such as standard deviation etc.

    def __init__(self, data: np.ndarray):
        self.data = data.flatten().astype(str)
        self.len = len(self.data)

    def get_distribution_at_index(self, index: int):
        """
        Returns the real distribution at a certain index.
        :param index: Index to inspect
        :return:
        """
        unique, counts = np.unique(self._get_digits(index), return_counts=True)
        return unique.astype(int), counts

    def _get_digits(self, indices: int or slice):
        """
        Gets digits at certain index. E.g. Give me all the first digit in the real data
        Index can also be slice. E.g. Give me first and second index etc.
        :param indices: Indices to be inspected
        :return:
        """
        if isinstance(indices, slice):
            length = indices.stop
        else:
            length = indices
        if np.min(np.vectorize(len)(self.data)) <= length:
            warnings.warn("Dataset Values not large enough for index")
        return self.data.view("<U1").reshape(self.data.shape + (-1, ))[:, indices]


if __name__ == "__main__":
    df = pd.read_csv(os.path.join("sample_data", "BigCityGermany.csv"))
    bl = RealDataBenfordLaw(df["2010"].to_numpy())
    print(bl.get_distribution_at_index(1))

