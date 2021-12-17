import numpy as np
from day1 import window_depth_increases

window_size = 3
test_data = np.array([0, 1, 2, 3, 2, 1, 0])
window_sum = np.array([3, 6, 7, 6, 3])
answer = np.array([[0, 0, 0, 1, 1]])


def test_window_depth_increases():
    output = window_depth_increases(test_data, window_size)
    assert np.sum(answer) == output
