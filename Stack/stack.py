class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            return

        last_item = self.stack[-1]
        del self.stack[-1]
        return last_item

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)



if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(23)
    stack.push("Ama")
    print(stack.size())
    stack.pop()
    print(stack.size())
    print(stack.peek())