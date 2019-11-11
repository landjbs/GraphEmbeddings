import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def gen_data(dLen, cityNum):
    # assert and init data matrix
    assert (dLen**2) >= cityNum, 'dLen squared should be geq than cityNum'
    dataMatrix = np.zeros(shape=(dLen, dLen))
    # city loc assignment
    cityDict = dict()
    skipNum = 0
    for i in range(cityNum + skipNum):
        x, y = np.random.randint(0, dLen), np.random.randint(0, dLen)
        if (x, y) in cityDict:
            skipNum += 1
            continue
        # suburbLocs = np.random.choice()
        connectionNum = np.random.randint(0, cityNum)
        cityDict.update({(x, y): connectionNum})
    # route hubs
    routeList = list()
    for fromLoc, connectionNum in cityDict.items():
        for toLoc in range(connectionNum):
            


    dataMatrix[finalX, finalY] = 10
    return dataMatrix

for _ in range(5):
    plt.imshow(gen_data(10, 4))
    plt.show()
