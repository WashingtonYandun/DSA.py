class BstNode:

    data = 0
    left = None
    right = None

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    root = None

    def __init__(self, data):
        self.root = BstNode(data)

    def insert(self):
        pass
