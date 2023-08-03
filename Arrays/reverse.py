from typing import List
def reverse_items(items: list):
    first_index = 0
    last_index = len(items) - 1

    while last_index > first_index:
        items[first_index], items[last_index] = items[last_index], items[first_index]
        first_index = first_index + 1
        last_index = last_index - 1
    return items


if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]
    print(reverse_items(items))