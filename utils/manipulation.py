import numpy as np
import random

# 杂交水稻


def crossOver(x, y):
    m = np.random.random(32)
    result = np.where(m < 0.5, x, y)
    return result

# 平移变换


def shift(x, n):
    return np.where(x >= 21, x+n, x)

# 随机平移


def randomShift(x):
    return shift(x, random.randint(-12, 12))

# 倒影变换


def shadow(x, n):
    return np.where(x >= 21, n*2-x, x)

# 围绕中央c倒影


def c_shadow(x):
    return shadow(x, 60)

# 逆行变换


def reverse(x):
    return x[::-1]


def nearest_CAGED(x):
    y = x % 12
    delta = np.zeros_like(x)
    delta[(y == 1) | (y == 3) | (y == 8)] = -1 + (np.random.rand(((y == 1) | (y == 3) | (y == 8)).sum()) > 0.5) * 2
    delta[(y == 5) | (y == 10)] = -1
    delta[(y == 6) | (y == 11)] = 1
    return x + delta


def nearest_Cmaj(x):
    y = x % 12
    delta = np.zeros_like(x)
    delta[(y == 1) | (y == 3) | (y == 8)] = -1 + (np.random.rand(((y == 1) | (y == 3) | (y == 8)).sum()) > 0.5) * 2
    delta[(y == 10)] = -1
    delta[(y == 6)] = 1
    return x + delta


# 靠拢五声音阶


def clamp_CAGED(x):
    return np.where(x >= 21, nearest_CAGED(x), x)
