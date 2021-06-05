import numpy as np
from lomnicki import lomnicki

zadanie1 = np.array([
   [4, 8, 1],
   [2, 3, 7],
   [6, 2, 5]
])
print(lomnicki(zadanie1))

zadanie2 = np.array([
   [6, 4, 5, 7],
   [3, 6, 4, 8],
   [7, 3, 8, 6]
])
print(lomnicki(zadanie2))

zadanie3 = np.random.randint(1,15, size=(10,5))
print(lomnicki(zadanie3))
