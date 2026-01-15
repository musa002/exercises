def read_input(prompt: str, lower: int, upper: int):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if lower <= number <= upper:
                return number
            else:
                print(f"You must type in an integer between {lower} and {upper}")
        except ValueError:
            print(f"You must type in an integer between {lower} and {upper}")


number = read_input("Please type in a number: ", 5, 10)
print("You typed in:", number)
