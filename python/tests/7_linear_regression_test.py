import pytest
import os
import numpy as np

from machine_learning.linear_regression import gradient_descent

def test_linear_regression():
    data = np.loadtxt('tests/assets/house_prices.txt', delimiter=',')
    X, y, theta = data[:, 0], data[:, 1], np.zeros(2)

    ans = np.array([-3.6303, 1.1664])
    theta = np.round(gradient_descent(X, y, theta, 0.01, 1500), 4)

    assert np.array_equal(theta, ans)
