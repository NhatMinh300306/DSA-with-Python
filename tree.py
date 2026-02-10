class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self._insert(self.root, item)
    def _insert(self, current, item):
        if item < current.item:
            if current.left is None:
                current.left = Node(item)
            else:
                self._insert(current.left, item)
        elif item > current.item:
            if current.right is None:
                current.right = Node(item)
            else:
                self._insert(current.right, item)

    def preorderTraversal(self):
        self._preorderTraversal(self.root)
        print()

    def _preorderTraversal(self, node):
        if node is None:
            return
        print(node.item, end=" ")
        self._preorderTraversal(node.left)
        self._preorderTraversal(node.right)

    def inorderTraversal(self):
        self._inorderTraversal(self.root)
        print()

    def _inorderTraversal(self, node):
        if node is None:
            return
        self._inorderTraversal(node.left)
        print(node.item, end=" ")
        self._inorderTraversal(node.right)

    def postorderTraversal(self):
        self._postorderTraversal(self.root)
        print()
    
    def _postorderTraversal(self, node):
        if node is None:
            return
        self._postorderTraversal(node.left)
        self._postorderTraversal(node.right)
        print(node.item, end=" ")

    def flipTree(self):
        self._flipTree(self.root)
        print()

    def _flipTree(self, node):
        if node is None:
            return
        temp = node.left
        node.left = node.right
        node.right = temp

        self._flipTree(node.left)
        self._flipTree(node.right)


tree = BinarySearchTree()
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(0.5)

tree.preorderTraversal()
tree.inorderTraversal()
tree.postorderTraversal()
        
tree.flipTree()
tree.preorderTraversal()
tree.inorderTraversal()
tree.postorderTraversal()
