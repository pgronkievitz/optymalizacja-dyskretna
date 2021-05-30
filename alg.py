import numpy as np

t = np.array([
    [6, 4, 5, 7],
    [3, 6, 4, 8],
    [7, 3, 8, 6]
])

def get_permutation(arr: np.array, permutaion: np.array):
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
    return arr[:, np.concatenate((permutaion, np.setdiff1d(p, permutaion)))]


def phi(time_cost : np.ndarray, w_r : np.array, phi_index : int):
    """
    Oblicza phi dla zadanej macierzy czasów, permutacji.

    Parameterss
    ----------
    time_cost : np.ndarray
        Macierz czasów wykonania prac dla poszczególnych brygad w mieszkaniach.
    w_r : np.array
        Permutacja.
    phi_index : int
        Numer phi. Tj. phi_1 to 0, phi_2 to 1 itp...

    Returns
    -------
    phi : int
        Phi.

    """
    time_cost = get_permutation(time_cost, w_r)

    tp, tk = job_matrices(time_cost)

    if phi_index == 0:
        suma = np.sum(time_cost[phi_index,])
    else:
        suma = np.sum(time_cost[phi_index, len(w_r):]) + tk[phi_index, len(w_r) - 1]
    minimum = np.min(np.sum(time_cost[phi_index + 1:, :][:, len(w_r):], axis=0))
    return suma + minimum


def job_matrices(time_cost : np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Dla podanej macierzy `t` zwraca macierze czasów początkowych i końcowych.
    Parameters
    ----------
    time_cost : np.ndarray
        Macierz czasów wykonania prac dla poszczególnych brygad w mieszkaniach.

    Returns
    -------
    (tp, tk) : (np.ndarray, np.ndarray)
        Macierze czasów pocztkowych i końcowych.

    """
    tp = np.zeros(time_cost.shape)
    tk = np.zeros(time_cost.shape)
    tp[0] = np.cumsum(np.concatenate((np.array([0]), time_cost[0][:-1])))
    tp[:, 0] = np.cumsum(np.concatenate((np.array([0]), time_cost[:, 0][:-1])))
    tk[0] = np.cumsum(time_cost[0])
    tk[:, 0] = np.cumsum(time_cost[:, 0])
    for i in range(1, time_cost.shape[0]):
        for j in range(1, time_cost.shape[1]):
            tp[i, j] = max([tk[i - 1, j], tk[i, j - 1]])
            tk[i, j] = tp[i, j] + time_cost[i, j]

    return tp, tk


assert (phi(t, [0], 0)) == 31
assert (phi(t, [1], 0)) == 32
assert (phi(t, [2], 0)) == 31

assert (phi(t, [0], 1)) == 30
assert (phi(t, [1], 1)) == 31
assert (phi(t, [2], 1)) == 29

assert (phi(t, [0], 2)) == 33
assert (phi(t, [1], 2)) == 34
assert (phi(t, [2], 2)) == 33

assert (phi(t, [0, 1], 0)) == 34
assert (phi(t, [0, 2], 0)) == 31
assert (phi(t, [0, 3], 0)) == 31

assert (phi(t, [0, 2, 1], 0)) == 36
assert (phi(t, [0, 2, 3], 0)) == 31

assert (phi(t, [0, 2, 1], 1)) == 35
assert (phi(t, [0, 2, 3], 1)) == 35

assert (phi(t, [0, 2, 1], 2)) == 33
assert (phi(t, [0, 2, 3], 2)) == 35