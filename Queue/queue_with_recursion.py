class Queue:
    def __init__(self) -> None:
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    def dequeue(self):
        if len(self.stack) == 1:
            return self.stack.pop()

        item = self.stack.pop()
        print(f'item before: {item}')
        dequeued_item = self.dequeue()
        print(f'item after: {item}')
        self.stack.append(item)

        return dequeued_item


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(45)
    queue.enqueue(4)
    queue.enqueue(3)
    print(queue.dequeue())