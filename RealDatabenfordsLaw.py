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
        """
        Drop everything behind the decimal
        :param data:
        """
        self.data = data.flatten().astype(int).astype(str)
        self.len = len(self.data)

    def get_distribution_at_index(self, index: int, norm: bool = True):
        """
        Returns the real distribution at a certain digit index. E.g. Distribution at Index 1
        :param index: Index to inspect
        :param norm: norm result
        :return:
        """
        unique, counts = np.unique(self._get_digits(index), return_counts=True)
        if norm:
            counts = counts / len(self.data)
        return unique.astype(int), counts

    def get_sequence_distribution(self, seq: int or str):
        if isinstance(seq, int):
            seq = str(seq)
        ary = self._get_digits(slice(0, len(seq)))
        return np.count_nonzero(
            np.apply_along_axis(''.join, 0, [ary[:, i] for i in range(len(seq))]) == seq) / len(self.data)

    def check_dispersion(self):
        dispersion = np.max(np.vectorize(len)(self.data)) - np.min(np.vectorize(len)(self.data))
        if dispersion < 5:
            warnings.warn("Dispersion not high enough")
        else:
            print("Dispersion check passed")

    def _get_digits(self, indices: int or slice):
        """
        Gets digits at certain index. E.g. Give me all the first digit in the real data
        Index can also be a slice. E.g. Give me first and second index etc.
        :param indices: Indices to be inspected
        :return:
        """
        if isinstance(indices, slice):
            length = indices.stop - 1
        else:
            length = indices
        if np.min(np.vectorize(len)(self.data)) <= length:
            warnings.warn("Dataset Values not large enough for index")
        return self.data.view("<U1").reshape(self.data.shape + (-1, ))[:, indices]


if __name__ == "__main__":
    df = pd.read_csv(os.path.join("Data", "BigCityGermany.csv"))
    bl = RealDataBenfordLaw(df["2010"].to_numpy())
    bl.check_dispersion()
    print(bl.get_distribution_at_index(1))

