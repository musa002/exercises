def line(length: int, character: str):
    print(character * length)

def triangle(size: int):
    for i in range(1, size + 1):
        line(i, "#")


triangle(6)
print()
triangle(3)
