class Pet:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name}, {self.species}"


class Person:
    def __init__(self, name: str, pet: Pet):
        self.name = name
        self.pet = pet

    def __str__(self):
        return f"{self.name}, has a pet: {self.pet}"

hulda = Pet("Hulda", "mixed-breed dog")
levi = Person("Levi", hulda)

print(levi)

