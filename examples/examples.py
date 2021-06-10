import numpy as np
from src.lomnicki import lomnicki

# Zadanie przykładowe
dane = np.array([
   [4, 8, 1],
   [2, 3, 7],
   [6, 2, 5]
])
print(dane)
print(lomnicki(dane))

# Zadanie duże
dane = np.random.randint(1, 15, size=(10, 5))
print(dane)
print(lomnicki(dane))
