import numpy as np
import random


def crossOver(x, y):
    m = np.random.random(32)
    result = np.where(m < 0.5, x, y)
    return result


def shift(x, n):
    return np.where(x >= 21, x+n, x)


def randomShift(x):
    return shift(x, random.randint(-12, 12))


def shadow(x, n):
    return np.where(x >= 21, n*2-x, x)


def c_shadow(x):
    return shadow(x, 60)


def reverse(x):
    return x[::-1]
