import numpy as np
from RealDatabenfordsLaw import RealDataBenfordLaw
import matplotlib.pyplot as plt
import pandas as pd
import os
import BenfordExpectance
from functools import partial


def digit_plot(benford_check: RealDataBenfordLaw, index: int, ax: plt.axes):
    real_dist = benford_check.get_distribution_at_index(index)
    expected_dist = BenfordExpectance.expected_distribution_n_digit(index, benford_check.len, 0.1)
    ax.bar(real_dist[0], real_dist[1], width=.3, label="real")
    ax.plot(expected_dist[0], expected_dist[1], label="expected", c="orange")


def digit_barplot(benford_check: RealDataBenfordLaw, index: int, ax: plt.axes):
    real_dist = benford_check.get_distribution_at_index(index)
    expected_dist = BenfordExpectance.expected_distribution_n_digit(index, benford_check.len)
    ax.bar(real_dist[0] - .2, real_dist[1], width=.3, label="real")
    ax.bar(expected_dist[0] + .2, expected_dist[1], width=.3, label="expected")


def plot(handler, title: str=None):
    fig, ax = plt.subplots()
    ax.set_title(title)
    handler(benford_check=bl, ax=ax)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv(os.path.join("sample_data", "worldcitiespop.csv"))
    data = df["Population"].to_numpy()
    data = data[~np.isnan(data)]
    data = data[data > 10]
    bl = RealDataBenfordLaw(data)
    plot(partial(digit_plot, index=0), title="First Digit Distribution Population Large Cities")
    plot(partial(digit_barplot, index=0), title= "")
    plot(partial(digit_plot, index=1))
    plot(partial(digit_barplot, index=1))
