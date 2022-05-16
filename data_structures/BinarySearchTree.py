# TODO: SOLVE METHODS BUGS
class BstNode:
    data = None
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

    def insert(self, node, data):
        if data < node.data:
            if node.left is not None:
                self.insert(node.left, data)
            else:
                node.left = BstNode(data)
        else:
            if node.right is not None:
                self.insert(node.right, data)
            else:
                node.left = BstNode(data)

    def traverse_preorder(self, node):
        if node is not None:
            print(node.data, end="\n")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.data, end="\n")
            self.traverse_inorder(node.right)

    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)
            print(node.data, end="\n")


btree = BinarySearchTree(10)

for i in range(0, 10):
    btree.insert(btree.root, i)

btree.traverse_preorder(btree.root)
