class SymbolTable:
    def __init__(self):
        self.table = []
        self.id_index = 0
        self.student_id_digits = [2, 1, 1, 1, 5, 3, 9, 6, 4]

    def add_entry(self, identifier, operators, digits):
        self.table.append([self.get_next_id(), identifier, operators, digits])

    def display_table(self):
        print(f"{'ID':<5}{'Identifiers':<20}{'Operators':<20}{'Digits':<20}")
        self.print_dashes()
        for entry in self.table:
            print(f"{entry[0]:<5}{entry[1]:<20}{entry[2]:<20}{entry[3]:<20}")
            self.print_dashes()

    def search_entry(self, search_identifier):
        result = [entry for entry in self.table if entry[1]
                  == search_identifier]
        if result:
            print(f"{'ID':<5}{'Identifiers':<20}{'Operators':<20}{'Digits':<20}")
            self.print_dashes()
            for entry in result:
                print(
                    f"{entry[0]:<5}{entry[1]:<20}{entry[2]:<20}{entry[3]:<20}")
                self.print_dashes()
        else:
            print(f"No entries found for identifier '{search_identifier}'.")

    def get_next_id(self):
        next_id = str(
            self.student_id_digits[self.id_index % len(self.student_id_digits)])
        self.id_index += 1
        return next_id

    def print_dashes(self):
        print(f"{'':<5}{'':-<20}{'':-<20}{'':-<20}")


def main():
    symbol_table = SymbolTable()

    # Input data from users
    symbol_table.add_entry("a", "=,+", "10,20")
    symbol_table.add_entry("b", "=", "20")
    symbol_table.add_entry("c", "=,/", "30,3")
    symbol_table.add_entry("f", "=,+", "14,12")
    symbol_table.add_entry("k", "=", "9")
    symbol_table.add_entry("e", "+", "30")
    symbol_table.add_entry("i", "=,*", "25,9")
    symbol_table.add_entry("m", ">", "90")
    symbol_table.add_entry("p", "<,+", "100,16")

    # Display the symbol table
    print("Symbol Table:")
    symbol_table.display_table()

    # Search operation
    search_identifier = input("\nEnter an identifier to search: ")
    print("\nSearch Result:")
    symbol_table.search_entry(search_identifier)


if __name__ == "__main__":
    main()
