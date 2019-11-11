import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from itertools import permutations

def gen_data(dLen, cityNum):
    # assert and init data matrix
    assert (dLen**2) >= cityNum, 'dLen squared should be geq than cityNum'
    dataMatrix = np.zeros(shape=(dLen, dLen))
    # city loc assignment
    cityDict = dict()
    skipNum = 0
    for i in range(cityNum + skipNum):
        loc = np.random.randint(0, dLen), np.random.randint(0, dLen)
        if loc in cityDict:
            skipNum += 1
            continue


    dataMatrix[finalX, finalY] = 10
    return dataMatrix

for _ in range(5):
    plt.imshow(gen_data(10, 4))
    plt.show()
