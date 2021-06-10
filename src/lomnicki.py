import numpy as np
from tree import Node


def lomnicki(time_cost: np.ndarray) -> tuple:
    """
    Oblicza optymalną kolejność obsługiwanych zadań/mieszkań wykorzystując
    algorytm Łomnickiego [1]_

    Parameters
    ----------
    time_cost : np.ndarray
        Macierz z kosztami. W wierszach są pracownicy/grupy mające do wykonania
        zadanie. W kolumnach znajdują się zadania/mieszkania, które mają
        obsłużyć pracownicy/grupy.

    References
    ----------
    [1] Brown, A. P. G., & Lomnicki, Z. A. (1966). Some Applications of the
    “Branch-and-Bound” Algorithm to the Machine Scheduling Problem. OR, 17(2),
    173. doi:10.2307/3007282

    Exampless
    --------
    | Maszyna    | Projekt 1 | Projekt 2 | Projekt 3 |
    |------------|-----------|-----------|-----------|
    | Tokarka    | 4         | 8         | 1         |
    | Skrawarka  | 2         | 3         | 7         |
    | Anodyzacja | 6         | 2         | 5         |

    >>> dane = np.array([
    ...    [4, 8, 1],
    ...    [2, 3, 7],
    ...    [6, 2, 5]
    ... ])
    >>> lomnicki(dane)
    ([[0, 2, 1]], [20.0])

    Returns
    -------
    (list, list)
        (Lisa ze wszystkimi rozwiązaniami (kolumhy liczone są od 0),
        Lista kosztów danych rozwiązań)

    """
    tree = Node(None, None, None)
    Node.t = time_cost

    # Rozwijam korzeń
    tree.expand()
    upper_bound = 100000000  # upper_bound na bardzo dużą wartość

    # Dopóki są elementy które mogę rozwijać
    while expandable_leafs := list(
            filter(lambda node: node.data <= upper_bound and len(
                node.get_index()) < tree.t.shape[1],
                   tree.get_leafs())):

        # Sprawdzam czy mogę obniżyć upper_bound znajdując wszystkie liście
        # oddalone od korzenia o ilość kolumn macierzy timecost  i o koszcie
        # mniejszym niż jest obecnie
        possible_upper = list(
            filter(lambda node: node.data <= upper_bound and len(
                node.get_index()) == tree.t.shape[1],
                   tree.get_leafs()))

        # Jeżeli takie istnieją tak to przypisuję nowe upper_bound
        if len(possible_upper):
            upper_bound = min(possible_upper, key=lambda node: node.data).data

        # Aktualizuję listę liści
        expandable_leafs = list(
            filter(lambda node: node.data <= upper_bound and len(
                node.get_index()) < tree.t.shape[1],
                   expandable_leafs))

        if expandable_leafs:
            # Rozwijam wierzchołek o najmniejszym koszcie
            min(expandable_leafs, key=lambda node: node.data).expand()

    # Zwracam odpowiedź, jako listę indeksów od korzenia do liścia stanowiącego
    # optymalne rozwiązanie co odpowiada kolejności w jakiej powinny być
    # wykonywanie mieszkania/cokolwiek.
    answers = list(
        filter(
            lambda node: node.data == upper_bound and len(node.get_index()) ==
                         tree.t.shape[1],
            tree.get_leafs()))

    # Zwracam wynik
    return [node.get_index() for node in answers], [node.data for node in
                                                    answers]
