# Complete the following tasks:
# 1. Write an add method to BinaryTree
# 2. Create an instance of BinaryTree
# 3. Add items to BinaryTree
# 4. Add depth-first traversals (pre, in, post)
# 5. Add breadth-first traversals (you need to build a queue data structure for this)
# 6. Add a display feature to visualise the tree
# 6. Create a new class based on this one for normal trees


class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, new_value):
        new_node = Node(item=new_value)
        placed = False
        last_node = None
        current_node = self.root
        while not placed:
            if current_node is None:
                placed = True
                if last_node.item < current_node.item:
                    last_node.right = new_node
                else:
                    last_node.left = new_node
                current_node = new_node
            if new_node.item < current_node.item:
                last_node = current_node
                current_node = current_node.left
            else:
                last_node = current_node
                current_node = current_node.right

    def pre_order(self, node):
        if node is not None:
            print(node.item)
            self.pre_order(node=node.left)
            self.pre_order(node=node.right)

    def in_order(self, node):
        if node is not None:
            self.pre_order(node=node.left)
            print(node.item)
            self.pre_order(node=node.right)

    def post_order(self, node):
        if node is not None:
            self.pre_order(node=node.left)
            self.pre_order(node=node.right)
            print(node.item)


binary = BinaryTree()
arr = [5, 3, 2, 6, 7]
for i in range(0, len(arr)):
    binary.add_node(arr[i])
