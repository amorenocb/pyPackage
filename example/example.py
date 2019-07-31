import numpy as np

"""
Test function. Generates N numbers from a normal distribution with unit variance and mean 0.

Parameters:
    - n (int) : Number of samples to draw from distribution

Returns:
    Numpy.array of floats with the n samples taken
"""


def test(n=100):
    return np.random.normal(size=n)
