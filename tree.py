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

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

    def get_index(self):
        if self.index is not None:
            return [self.index] + self.parent.get_index()
        else:
            return []

    def expand(self):
        """
        Expands tree by generating its children.

        """
        n = [x for x in range(0, t.shape[1])]
        nodes = [Node(max_phi(t, self.get_index() + [x]), self, x) for x in
             np.setdiff1d(n, self.get_index())]
        for node in nodes:
            self.add_child(node)

tree = Node(None, None, None)
print(tree)