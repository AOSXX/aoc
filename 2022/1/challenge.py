import pandas as pd
import numpy as np


def _read_file(filename):
    """
    Read lines a text file called <filename> in the current directory.
    """
    with open(filename, "r") as fo:
        lines = [line.strip() for line in fo.readlines()]
    return lines




if __name__ == "__main__":
    with open("data.txt") as f:
        elves = f.read().split("\n\n")
        elves = [
            [int(cal) for cal in elf.split("\n")]
                           for elf in elves]
    total_cal = sorted([sum(elf) for elf in elves], reverse=True)

    print(f"First exercise {total_cal[0]} calories.")
    print(f"Second exercise {sum(total_cal[:3])} calories.")