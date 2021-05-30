import numpy as np
from tree import Node


def lomnicki(time_cost):
    tree = Node(None, None, None)
    Node.t = time_cost

    # Rozwijam korzeń
    tree.expand()
    upper_bound = 100000  # upper_bound na bardzo dużą wartość

    # Dopóki są elementy które mogę rozwijać
    while expandable_leafs := list(
            filter(lambda node: node.data <= upper_bound and len(node.get_index()) < tree.t.shape[1] - 1,
                   tree.get_leafs())):

        # Sprawdzam czy mogę obniżyć upper_bound znajdując wszystkie liście oddalone od korzenia o
        # ilość kolumn macierzy timecost - 1 i o koszcie mniejszym niż jest obecnie
        possible_upper = list(
            filter(lambda node: node.data <= upper_bound and len(node.get_index()) == tree.t.shape[1] - 1,
                   tree.get_leafs()))

        # Jeżeli tak to przypisuję nowe upper_bound
        if len(possible_upper):
            upper_bound = min(possible_upper, key=lambda node: node.data).data

        # Rozwijam wierzchołek o najmniejszym koszcie
        min(expandable_leafs, key=lambda node: node.data).expand()

    # Zwracam odpowiedź, jako listę indeksów od korzenia do liścia stanowiącego optymalne rozwiązanie
    # co odpowiada kolejności w jakiej powinny być wykonywanie mieszkania/cokolwiek.
    answers = list(
        filter(lambda node: node.data == upper_bound and len(node.get_index()) == tree.t.shape[1] - 1,
               tree.get_leafs()))

    # Dopisuję ostatni liść
    n = [x for x in range(0, tree.t.shape[1])]
    return [node.get_index() + np.setdiff1d(n, node.get_index()).tolist() for node in answers]


# Przykład
m = lomnicki(np.array([
    [6, 4, 5, 7],
    [3, 6, 4, 8],
    [7, 3, 8, 6]
]))

print(m)
