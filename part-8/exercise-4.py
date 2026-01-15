class ShoppingList:
    def __init__(self):
        self._items = []      
        self._amounts = []    

    def add_item(self, item: str, amount: int):
        self._items.append(item)
        self._amounts.append(amount)

    def number_of_items(self):
        return len(self._items)

    def item(self, index: int):
        return self._items[index]

    def amount(self, index: int):
        return self._amounts[index]

    def print_list(self):
        for i in range(self.number_of_items()):
            print(f"{self.item(i)}: {self.amount(i)}")

shopping_list = ShoppingList()
shopping_list.add_item("Milk", 2)
shopping_list.add_item("Eggs", 12)
shopping_list.add_item("Bread", 1)

print(shopping_list.number_of_items())  
print(shopping_list.item(1))            
print(shopping_list.amount(1))          

shopping_list.print_list()
