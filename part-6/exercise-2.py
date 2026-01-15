def read_fruits() -> dict:
    fruits = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.strip()
            if line: 
                name, price = line.split(";")
                fruits[name] = float(price)
    return fruits



if __name__ == "__main__":
    fruit_dict = read_fruits()
    print(fruit_dict)
