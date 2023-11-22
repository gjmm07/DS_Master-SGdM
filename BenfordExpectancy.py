import numpy as np


def probability_multi_digit(digits: int or np.ndarray[int]):
    """
    Probability for a combination of digits e.g. probability for the first two digits being 16
    :param digits: digit or digit combination e.g. 6 or 62
    :return: Benford's probability
    """
    return np.log10(1 + 1 / digits)


def expected_probability_pos_digit(position: int, digit: int):
    """
    Calculates the expected probability of a certain digit at a certain position
    :param position: pos where probability is inspected
    :param digit:
    :return:
    """
    if not position:
        return probability_multi_digit(digit)
    x = int("1" + str().join(["0"] * (position - 1)))
    y = int(str().join(["9"] * position))
    return sum(probability_multi_digit(np.array([int(str(i) + str(digit)) for i in range(x, y + 1)])))


def expected_distribution_n_digit(position: int, length: int = 1, steps: float = 1.0):
    """
    Benford's distribution of all digits at a certain position e.g. digit distribution at second index
    :param position: pos to be inspected
    :param length: length of the original data (turn probability into expectancy)
    :param steps: Amount for steps to be taken (todo: implement)
    :return:
    """
    if not position:
        return _expected_distribution_first_digit(length, steps)
    return (np.arange(0, 9.1),
            np.array([expected_probability_pos_digit(position, digit) for digit in range(0, 10)]) * length)


def _expected_distribution_first_digit(length: int = 1, steps: float = 1.0):
    """
    Due to Benfords Law expected distribution only on first digit
    :return:
    """
    return (np.arange(1, 9.1, steps),
            np.log10((np.arange(1, 9.1, steps) + 1) / np.arange(1, 9.1, steps)) * length)


if __name__ == "__main__":
    print(expected_distribution_n_digit(0, 1))
