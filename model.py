import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def gen_data(dLen, mainNodes):
    assert (dLen**2) >= mainNodes, 'dLen squared should be geq than main nodes'
    dataMatrix = np.zeros(shape=(dLen, dLen))
    xLocs = np.random.randint(0, dLen, size=mainNodes)
    yLocs = np.random.randint(0, dLen, size=mainNodes)
    cityLocs = set(zip(xLocs, yLocs))
    while len(cityLocs) < mainNodes:
        x = np.random.int(0, dLen, size=mainNodes),
        y = np.random.int(0, dLen, size=mainNodes)
        if not (x, y) in cityLocs:
            cityLocs.add((x, y))
    dataMatrix[cityLocs] = 10
    return dataMatrix

plt.imshow(gen_data(10, 4))
plt.show()
