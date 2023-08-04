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

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        self.number_of_items = self.number_of_items + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

#not too sure
    def remove_at_start(self):
        if self.head:
            self.head = self.head.next_node

#not too sure
    def remove_at_end(self):
        if self.head:
            current_node = self.head
            previous_node = None
            while current_node.next_node:
                previous_node = current_node
                current_node = current_node.next_node
        previous_node.next_node = None

    def remove_arbituarily(self, data):
        if not self.head:
            return

        current_node = self.head
        previous_node = None
        
        while current_node and current_node.data != data:
           previous_node = current_node
           current_node = current_node.next_node

        if not current_node:
            return

        if not previous_node:
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

    def get_middle_node(self):
        faster_node = self.head
        slower_node = self.head

        while faster_node.next_node and faster_node.next_node.next_node:
            faster_node = faster_node.next_node.next_node
            slower_node = slower_node.next_node

        return slower_node.data


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

    linked_list_2 = LinkedList()
    linked_list_2.insert_at_end(1)
    linked_list_2.insert_at_end(2)
    linked_list_2.insert_at_end(3)
    linked_list_2.insert_at_end(4)
    linked_list_2.insert_at_end(5)
    linked_list_2.traverse()
    print("-------------------------------")
    print(linked_list_2.get_middle_node())