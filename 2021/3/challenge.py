import pandas as pd
import numpy as np


def _read_file(filename):
    """
    Read lines from a text file called <filename> in the current directory.
    """
    with open(filename, "r") as fo:
        lines = [line.strip() for line in fo.readlines()]
    return lines


import statistics
from statistics import mode


def most_common(List):
    return (mode(List))


def get_rating(diagnostic_list=[], oxygen=True, idx=0):
    one_list = []
    zero_list = []
    for line in diagnostic_list:
        if line[idx] == '1':
            one_list.append(line)
        else:
            zero_list.append(line)
    if oxygen:
        if len(one_list) == len(zero_list) == 1:
            return ''.join(one_list if one_list[0][idx] == '1' else zero_list)
        else:
            return get_rating(
                one_list if len(one_list) >= len(zero_list) else zero_list,
                oxygen, idx + 1)
    else:
        if len(one_list) == len(zero_list) == 1:
            return ''.join(one_list if one_list[0][idx] == '0' else zero_list)
        else:
            return get_rating(
                one_list if len(one_list) <= len(zero_list) else zero_list,
                oxygen, idx + 1)


if __name__ == "__main__":
    with open("data.txt") as f:
        diagnostic_list = []
        for line in f:
            diagnostic_list.append(line.replace('\n', ''))
    oxygen = get_rating(diagnostic_list, True)
    CO2 = get_rating(diagnostic_list, False)
    print(int(oxygen, 2) * int(CO2, 2))
