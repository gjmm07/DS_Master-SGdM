import warnings
import numpy as np
from RealDatabenfordsLaw import RealDataBenfordLaw
import BenfordExpectancy as Be
from scipy.stats import chi2
import read_prepare_data as rpd


def sequence_distribution(seq: int):
    """
    Calculates the probability of a certain beginning sequence
    :param seq: to be inspected
    :return:
    """
    real_dist = bl.get_sequence_distribution(seq)
    exp_dist = Be.probability_multi_digit(seq)
    print(f"The expected probability for the first {len(str(seq))} digits being {seq} is: {round(exp_dist * 100, 4)} %")
    print(f"The percentage of the first {len(str(seq))} digits actually being {seq} is {round(real_dist * 100, 4)} %")
    print("____________________\n")


def chi2_test(index, alpha=.001):
    """
    Chi squared test at a certain index. For example check if first digit conform to Benford's Law
    :param index: index, where to do inspection
    :param alpha: threshold which is compared to the calculated p-value
    :return:
    """
    in1, dist = bl.get_distribution_at_index(index, True)
    in2, exp_dist = Be.expected_distribution_n_digit(index)
    if np.any(in1 != in2):
        warnings.warn("Not all digits are the same in expected and actual distribution")
    chi_square = sum((dist - exp_dist) ** 2 / exp_dist)
    p = 1 - chi2.cdf(chi_square, df=len(in2) - 1)
    print(p)
    print("H0: The population first significant digit distribution conforms to Benford's Law")
    print("H1: The population first significant digit distribution is different from Benford's Law")
    if p >= alpha:
        print("HO is True, H1 is False")
    else:
        print("H0 is False, H1 is True")
    print("____________________\n")


if __name__ == "__main__":
    data = rpd.read_population()
    # data = rpd.read_height()
    bl = RealDataBenfordLaw(data)
    bl.check_dispersion()
    # sequence_distribution(32)
    chi2_test(0)


