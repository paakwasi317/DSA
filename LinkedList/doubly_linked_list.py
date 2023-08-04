
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, data):
        current_node = Node(data)

        if self.head is None:
            self.head = current_node
            self.tail = current_node
        else:
            current_node.previous_node = self.tail
            self.tail.next_node = current_node
            self.tail = current_node

    def traverse_forward(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def traverse_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.previous_node


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    doubly_linked_list.insert(3)

    doubly_linked_list.traverse_forward()
    print("---------------------------")
    doubly_linked_list.traverse_backward()