# Day 1 prompt: https://adventofcode.com/2021/day/1

import numpy as np


def load_input():
    with open("2021/day1/input_1.txt", "r") as f:
        input = f.readlines()
    return [int(x.strip("\n")) for x in input]


def depth_increases(arr: np.ndarray) -> int:
    """
    Part 1: Single-measurement increases
    """
    return np.sum(arr[1:] > arr[:-1])


def window_depth_increases(arr: np.ndarray, window_size: int = 3) -> int:
    """
    Part 2: Compare sum of three-measurement windows
    """
    tot = np.zeros(arr.shape[0] - window_size + 1)
    for i in range(0, window_size - 1):
        tot += arr[i : -(window_size - i - 1)]

    # Add last one in separately because indexing [3:-0] returns empty set
    tot += arr[window_size - 1 :]

    assert tot[0] == np.sum(arr[:window_size])
    return depth_increases(tot)


if __name__ == "__main__":
    input = np.array(load_input())
    print(input.shape)
    out_1 = depth_increases(input)
    print(f"{out_1} single-step depth increases found!")

    window_size = 3
    out_2 = window_depth_increases(input, window_size)
    print(f"{out_2} {window_size}-step depth increases found!")
