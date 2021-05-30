import numpy as np
from alg import t, max_phi


class Node(object):
    def __init__(self, data, parent, index):
        self.parent = parent
        self.children = []

        self.index = index
        self.data = data

    def add_child(self, obj):
        self.children.append(obj)

    def __str__(self):
        return str(self.data)

    def get_index(self):
        if self.index is not None:
            return [self.index] + self.parent.get_index()
        else:
            return []

    def expand(self):
        """
        Rozszerza drzewo w obecnym node (dodaje liście i oblicza max_phi).

        """
        n = [x for x in range(0, t.shape[1])]
        nodes = [Node(max_phi(t, self.get_index() + [x]), self, x) for x in
             np.setdiff1d(n, self.get_index())]
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
            return self
        else:
            return [child.get_leafs() for child in self.children]

    def get_min_leaf(self):
        """
        Zwraca liść z minimalnym kosztem.

        Returns
        -------
        Node
            Liść z minimalnym kosztem.
        """
        return min(self.get_leafs(), key=lambda node: node.data)


tree = Node(None, None, None)
print(tree)
tree.expand()
min(tree.get_leafs(), key = lambda node : node.data)