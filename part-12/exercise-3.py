def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    while beginning <= maximum:
        yield beginning
        beginning += 2

numbers = even_numbers(2, 10)
for number in numbers:
    print(number)

print()

numbers = even_numbers(3, 15)
for number in numbers:
    print(number)
