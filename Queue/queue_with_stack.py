class Queue:
    def __init__(self) -> None:
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if not self.enqueue_stack and not self.enqueue_stack:
            # breakpoint()
            raise Exception("nothing to take out")

        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
            return self.dequeue_stack.pop()
        return self.dequeue_stack.pop()

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(45)
    queue.enqueue(4)
    queue.enqueue(3)
    print(queue.dequeue())