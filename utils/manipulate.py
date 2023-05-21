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


def nearest(x):
    t = random.randint(0, 1)
    y = x % 12
    if y == 0 or y == 2 or y == 4 or y == 7 or y == 9:
        return x
    if y == 1 or y == 3 or y == 8:
        return x-1+t*2
    if y == 5 or y == 10:
        return x-1
    if y == 6 or y == 11:
        return x+1


def clamp(x):
    return np.where(x >= 21, nearest(x), x)
