from readline import insert_text


class Node:

    def __init__(self, data, parent=None) -> None:
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, parent=self.root)

    def insert_node(self, data, node: Node):
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, parent=node)
        else:
            if not node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, parent=node)