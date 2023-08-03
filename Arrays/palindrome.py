import reverse

def is_palindrome(item: str) -> bool:
    item_to_list = list(item)
    reversed_list_of_item = reverse.reverse_items(item_to_list)
    if item == ''.join(reversed_list_of_item):
        return True
    return False

def is_palindrome_implemented_another_way(item: str) -> bool:
    if item != item[::-1]:
        return False
    return True



if __name__ == '__main__':
    item = "mum"
    print(is_palindrome(item))
    print(is_palindrome_implemented_another_way(item))