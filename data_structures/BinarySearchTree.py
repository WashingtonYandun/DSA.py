class BST_Node:

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
        self.root = BST_Node(data)
