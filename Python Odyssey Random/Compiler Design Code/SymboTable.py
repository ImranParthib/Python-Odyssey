class SymbolTable:
    def __init__(self):
        self.table = []

    def display_table(self):
        print("ID\tIdentifier")
        for i, entry in enumerate(self.table):
            print(f"{i}\t{entry}")

    def insert_identifier(self, identifier):
        self.table.append(identifier)

    def delete_identifier(self, identifier):
        try:
            index = self.table.index(identifier)
            del self.table[index]
            print(f"The item '{identifier}' is removed from the symbol table.")
        except ValueError:
            print(f"The item '{identifier}' is not found in the symbol table.")

    def search_identifier(self, identifier):
        try:
            index = self.table.index(identifier)
            print(f"The item '{identifier}' found in index: {index}.")
        except ValueError:
            print(f"The item '{identifier}' not found in the symbol table.")


# Example usage
symbol_table = SymbolTable()

while True:
    print("\n1. Insert\n2. Delete\n3. Search\n4. Display Table\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        identifier = input("Enter an identifier: ")
        symbol_table.insert_identifier(identifier)
    elif choice == 2:
        identifier = input("Enter an identifier to remove: ")
        symbol_table.delete_identifier(identifier)
    elif choice == 3:
        identifier = input("Enter an identifier to search: ")
        symbol_table.search_identifier(identifier)
    elif choice == 4:
        symbol_table.display_table()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
