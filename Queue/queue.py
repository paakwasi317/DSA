class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.queue:
            return

        last_item = self.queue[0]
        del self.queue[0]
        return last_item

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)




if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(23)
    queue.enqueue("Ama")
    print(queue.size())
    print(queue.dequeue())

# NB: We could have used a doubly linked list to avoid O(N) during dequeue since with
# with doubly linked list we always have access to the head and tail of the node. That
# would mean that both enqueue and dequeue would have O(1) running time complexity. At
# the moment only enqueue has O(1) because of the array data structure we chose. 