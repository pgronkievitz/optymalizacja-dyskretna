import numpy as np
from phi import max_phi


class Node(object):
    t = None  # Macierz kosztów

    def __init__(self, data, parent, index):
        self.parent = parent
        self.children = []

        self.index = index
        self.data = data

    def add_child(self, obj):
        self.children.append(obj)

    def __str__(self):
        return str(self.data)

    def get_index(self) -> list:
        """
        Zwraca index liścia (listę punków wokół których był rozwijany).

        Returns
        -------
        list
            Lista liści
        """
        if self.index is not None:
            return self.parent.get_index() + [self.index]
        else:
            return []

    def expand(self):
        """
        Rozszerza drzewo w obecnym node (dodaje liście i oblicza max_phi).

        """
        n = [x for x in range(0, self.t.shape[1])]
        index = self.get_index()

        nodes = [Node(max_phi(self.t, index + [x]), self, x) for x in
                 np.setdiff1d(n, index)]
        for node in nodes:
            self.add_child(node)

    def get_leafs(self):
        """
        Zwraca wszystkie liście poddrzewa.

        Returns
        -------
        list
            Lista Node
        """
        if len(self.children) == 0:
            return [self]
        else:
            l = []
            for child in self.children:
                l.extend(child.get_leafs())
            return l

    def get_min_leaf(self):
        """
        Zwraca liść z minimalnym kosztem.

        Returns
        -------
        Node
            Liść z minimalnym kosztem.
        """
        return min(self.get_leafs(), key=lambda node: node.data)
