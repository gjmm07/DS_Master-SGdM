import numpy as np
from RealDatabenfordsLaw import RealDataBenfordLaw
import matplotlib.pyplot as plt
import read_prepare_data as rpd
import BenfordExpectancy
from functools import partial


def digit_plot(benford_check: RealDataBenfordLaw, index: int, ax: plt.axes):
    real_dist = benford_check.get_distribution_at_index(index)
    expected_dist = BenfordExpectancy.expected_distribution_n_digit(index, 1, 0.1)
    print(expected_dist)
    ax.bar(real_dist[0], real_dist[1], width=.3, label="real")
    ax.plot(expected_dist[0], expected_dist[1], label="expected", c="orange")


def digit_barplot(benford_check: RealDataBenfordLaw, index: int, ax: plt.axes):
    real_dist = benford_check.get_distribution_at_index(index)
    expected_dist = BenfordExpectancy.expected_distribution_n_digit(index, 1)
    ax.bar(real_dist[0] - .2, real_dist[1], width=.3, label="real")
    ax.bar(expected_dist[0] + .2, expected_dist[1], width=.3, label="expected")


def sequence_plot(benford_check: RealDataBenfordLaw, field: tuple, ax: plt.axes):
    real_dist = np.stack([(i, benford_check.get_sequence_distribution(i)) for i in range(*field)])
    exp_dist = np.stack([(i, BenfordExpectancy.probability_multi_digit(i)) for i in range(*field)])
    ax.bar(*real_dist.T, label="real")
    ax.plot(*exp_dist.T, label="expected", c="orange")


def plot(handler, title: str = None):
    fig, ax = plt.subplots()
    ax.set_title(title)
    handler(benford_check=bl, ax=ax)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    # Change between these two
    data = rpd.read_population()
    # data = rpd.read_height()
    # _________________

    bl = RealDataBenfordLaw(data)
    bl.check_dispersion()
    plot(partial(sequence_plot, field=(10, 100)), title="Distribution of first two digits")
    plot(partial(digit_plot, index=0), title="First Digit Distribution Population Large Cities")
    plot(partial(digit_barplot, index=0), title="First Digit Distribution Population Large Cities")
    plot(partial(digit_plot, index=1), title="Second Digit Distribution Large Cities")
    plot(partial(digit_barplot, index=1), title="Second Digit Distribution Large Cities")
