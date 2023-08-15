class Stack:
    def __init__(self) -> None:
        self.main_stack = []
        self.max_stack = []

    def push(self, data: int):
        self.main_stack.append(data)

        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return

        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def get_max_item(self):
        return self.max_stack.pop()


if __name__ == '__main__':
    stack = Stack()
    stack.push(100)
    stack.push(10)
    stack.push(300)
    print(stack.get_max_item())

