def line(length: int, character: str):
    print(character * length)


def square(length: int, character: str):
    for _ in range(length):
        line(length, character)



square(5, "*")
print()
square(3, "o")
