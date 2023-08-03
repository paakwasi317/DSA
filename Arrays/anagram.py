
def is_anagram(first_item: str, second_item: str) -> bool:
    if len(first_item) != len(second_item):
        return False

    sorted_first_item = sorted(first_item)
    sorted_second_item = sorted(second_item)

    for i in range(len(first_item)):
        if sorted_first_item[i] != sorted_second_item[i]:
            return False
    return True 


if __name__ == "__main__":
    print(is_anagram("angel", "glean"))