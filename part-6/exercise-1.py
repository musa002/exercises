with open("numbers.txt") as new_file:
    contents = new_file.read()
for num in contents:
    word = num.split(",")
    print(word)