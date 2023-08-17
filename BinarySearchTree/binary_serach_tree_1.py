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
            self._insert_node(data, self.root)

    def _insert_node(self, data, node: Node):
        if data < node.data:
            if node.left_node:
                self._insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, parent=node)
        else:
            if node.right_node:
                self._insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, parent=node)

    def max_item(self):
        return self._get_max_item(self.root)

    def _get_max_item(self, node: Node):
        current_node = node

        if current_node.right_node:
            return self._get_max_item(current_node.right_node)
        return current_node.data

    def min_item(self):
        return self._get_min_item(self.root)

    def _get_min_item(self, node: Node):
        current_node = node

        if current_node.left_node:
            return self._get_min_item(current_node.left_node)
        return current_node.data

    def traverse(self):
        if self.root:
            self._traverse_in_order(self.root)

    def _traverse_in_order(self, node: Node):
        if node.left_node:
            self._traverse_in_order(node.left_node)

        print(node.data)
        if node.right_node:
            self._traverse_in_order(node.right_node)

        
if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(5)
    binary_search_tree.insert(1)
    binary_search_tree.insert(6)
    binary_search_tree.insert(10)
    binary_search_tree.insert(2)
    binary_search_tree.insert(15)
    print(binary_search_tree.min_item())
    print(binary_search_tree.max_item())