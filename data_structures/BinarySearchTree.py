class TNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []

    def __repr__(self):
        return f"Node({self.val})"

    def add_child(self, val):
        self.children.append(Node(val))

    def depth(self):
        if not self.parent:
            return 0
        return self.parent.depth() + 1

    def height(self):
        if not self.children:
            return 0
        return 1 + max(child.height() for child in self.children)

    def size(self):
        return 1 + sum(child.size() for child in self.children)

    def preorder_traversal(self):
        traversal = [self.val]
        for child in self.children:
            traversal.extend(child.preorder_traversal())
        return traversal

    def inorder_traversal(self):
        traversal = []
        for child in self.children[:len(self.children) // 2]:
            traversal.extend(child.inorder_traversal())
        traversal.append(self.val)
        for child in self.children[len(self.children) // 2:]:
            traversal.extend(child.inorder_traversal())
        return traversal

    def postorder_traversal(self):
        traversal = []
        for child in self.children:
            traversal.extend(child.postorder_traversal())
        traversal.append(self.val)
