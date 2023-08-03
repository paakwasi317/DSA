
def reverse_integer(integer: int) -> int:
    reversed_integer = 0
    while integer > 0:
        remainder = integer % 10
        reversed_integer = reversed_integer * 10 + remainder
        integer = integer // 10
    return reversed_integer


if __name__ == "__main__":
    print(reverse_integer(12345))