import numpy as np

t = np.array([
    [6,4,5,7],
    [3,6,4,8],
    [7,3,8,6]
])

tp = np.zeros(t.shape)
tk = np.zeros(t.shape)
tp[0] = np.cumsum(np.concatenate((np.array([0]), t[0][:-1])))
tp[:,0] = np.cumsum(np.concatenate((np.array([0]), t[:, 0][:-1])))

tk[0] = np.cumsum(t[0])
tk[:,0] = np.cumsum(t[:, 0])

for i in range(1, t.shape[0]):
    for j in range(1, t.shape[1]):
        tp[i,j] = max([tk[i-1,j],tk[i,j-1]])
        tk[i,j] = tp[i,j] + t[i,j]


print(t)
print(tp)
print(tk)
