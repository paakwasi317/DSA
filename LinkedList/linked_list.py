class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.number_of_items = 0

    def insert_at_start(self, data):
        self.number_of_items = self.number_of_items + 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        self.number_of_items = self.number_of_items + 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

#not too sure
    def remove_at_start(self):
        if self.head is not None:
            self.head = self.head.next_node

#not too sure
    def remove_at_end(self):
        if self.head is not None:
            current_node = self.head
            previous_node = None
            while current_node.next_node is not None:
                previous_node = current_node
                current_node = current_node.next_node
        previous_node.next_node = None

    def remove_arbituarily(self, data):
        if self.head is None:
            return

        current_node = self.head
        previous_node = None
        
        while current_node is not None and current_node.data != data:
           previous_node = current_node
           current_node = current_node.next_node

        if current_node is None:
            return

        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

                


    def get_length(self):
        print(self.number_of_items)

    def traverse(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_start("hello")
    linked_list.insert_at_start("world")
    linked_list.insert_at_start("trial")
    linked_list.get_length()
    linked_list.traverse()
    print("----------------------------")
    linked_list.insert_at_end("someday")
    linked_list.traverse()
    print("----------------------------")
    linked_list.remove_at_start()
    linked_list.traverse()
    print("----------------------------")
    linked_list.remove_at_end()
    linked_list.traverse()
    print("----------------------------")
    linked_list.remove_arbituarily("world")
    linked_list.traverse()