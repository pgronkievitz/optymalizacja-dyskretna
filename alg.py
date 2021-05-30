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


######### Permutacje
perm = np.array([2,3])


def get_permutation(arr: np.array, permutaion : np.array):
    """
    Generuje macierz z zamienionymi kolumnami (w_r w OneNote)

    Parameters
    ----------
    arr : np.array
        Macierz którą permutujemy.

    permutaion : np.array
        Lista identyfikująca permutację. Zawierają indeksy elementów, które
        mają być zwrócone jako pierwsze, pozostałe są zwracane w kolejności
        występowania.

    Returns
    -------
    np.array
        Macierz z kolumnami zamienionymi zgodnie z podaną permutacją.
    """
    p = np.array([x for x in range(0, arr.shape[1])])
    return arr[:,np.concatenate((permutaion, np.setdiff1d(p, permutaion)))]

def calc(t, r, phi_index):
    t = get_permutation(t, r)

    tp, tk = macierze_czasow(t)

    p = np.array([x for x in range(0, t.shape[1])]) # Columns index
    k = np.array([x for x in range(0, t.shape[0])]) # Rows index
    cols = np.setdiff1d(p, r) # Excluded columns
    if phi_index == 0:
        suma = np.sum(t[phi_index,])
    else:
        suma = np.sum(t[phi_index,len(r):]) + tk[phi_index, len(r)-1]
    minimum = np.min(np.sum(t[phi_index+1:,:][:,len(r):],axis=0))
    return suma + minimum


def macierze_czasow(t):
    tp = np.zeros(t.shape)
    tk = np.zeros(t.shape)
    tp[0] = np.cumsum(np.concatenate((np.array([0]), t[0][:-1])))
    tp[:, 0] = np.cumsum(np.concatenate((np.array([0]), t[:, 0][:-1])))
    tk[0] = np.cumsum(t[0])
    tk[:, 0] = np.cumsum(t[:, 0])
    for i in range(1, t.shape[0]):
        for j in range(1, t.shape[1]):
            tp[i, j] = max([tk[i - 1, j], tk[i, j - 1]])
            tk[i, j] = tp[i, j] + t[i, j]

    return tp, tk


assert (calc(t,[0], 0)) == 31
assert (calc(t,[1], 0)) == 32
assert (calc(t,[2], 0)) == 31

assert (calc(t,[0], 1)) == 30
assert (calc(t,[1], 1)) == 31
assert (calc(t,[2], 1)) == 29

assert (calc(t,[0,1], 0)) == 34
assert (calc(t,[0,2], 0)) == 31
assert (calc(t,[0,3], 0)) == 31

