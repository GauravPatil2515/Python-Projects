class Restaurant:
    def __init__(self):
        self.menu = {
            'PIZZA': 100,
            'PASTA': 80,
            'BURGER': 50,
            'TACO': 70,
            'COFFEE': 80,
            'SALAD': 60,
            'SANDWICH': 40,
            'SOUP': 50,
            'STEAK': 200,
            'ICE_CREAM': 30
        }
        self.tables = {i: None for i in range(1, 11)}  # 10 tables

    def show_menu(self):
        print("MENU:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def take_order(self, table_number):
        if table_number not in self.tables:
            print("Invalid table number.")
            return
        
        if self.tables[table_number] is None:
            self.tables[table_number] = Order()
        order = self.tables[table_number]
        while True:
            item = input("Enter the name of the item you want to order (or 'done' to finish): ").upper()
            if item == 'DONE':
                break
            elif item in self.menu:
                try:
                    quantity = int(input(f"Enter the quantity of {item}: "))
                    if quantity > 0:
                        order.add_item(item, quantity, self.menu[item])
                        print(f"Added {quantity} x {item} to table {table_number}'s order.")
                    else:
                        print("Quantity must be positive.")
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
            else:
                print(f"{item} is not available on the menu.")

    def generate_bill(self, table_number):
        if table_number not in self.tables:
            print("Invalid table number.")
            return

        order = self.tables[table_number]
        if order is None or not order.items:
            print(f"No orders for table {table_number}.")
            return
        
        total = order.calculate_total()
        sgst_rate = 0.035  # 3.5%
        cgst_rate = 0.035  # 3.5%
        
        sgst_amount = total * sgst_rate
        cgst_amount = total * cgst_rate
        grand_total = total + sgst_amount + cgst_amount
        
        print(f"BILL FOR TABLE {table_number}:")
        for item, (quantity, price) in order.items.items():
            print(f"{item} x {quantity}: ${quantity * price}")
        print(f"Subtotal: ${total:.2f}")
        print(f"SGST (3.5%): ${sgst_amount:.2f}")
        print(f"CGST (3.5%): ${cgst_amount:.2f}")
        print(f"TOTAL: ${grand_total:.2f}")

    def clear_table(self, table_number):
        if table_number not in self.tables:
            print("Invalid table number.")
            return
        
        self.tables[table_number] = None
        print(f"Table {table_number} has been cleared and is ready for new customers.")

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity, price):
        if item in self.items:
            self.items[item] = (self.items[item][0] + quantity, price)
        else:
            self.items[item] = (quantity, price)

    def calculate_total(self):
        return sum(quantity * price for quantity, price in self.items.values())

def show_main_menu():
    print("\nWelcome to the Restaurant Management System")
    print("1. Show Menu")
    print("2. Take Order")
    print("3. Generate Bill")
    print("4. Clear Table")
    print("5. Exit")

def main():
    restaurant = Restaurant()
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            restaurant.show_menu()
        elif choice == '2':
            try:
                table_number = int(input("Enter table number (1-10): "))
                restaurant.take_order(table_number)
            except ValueError:
                print("Invalid table number. Please enter a number between 1 and 10.")
        elif choice == '3':
            try:
                table_number = int(input("Enter table number (1-10): "))
                restaurant.generate_bill(table_number)
            except ValueError:
                print("Invalid table number. Please enter a number between 1 and 10.")
        elif choice == '4':
            try:
                table_number = int(input("Enter table number (1-10): "))
                restaurant.clear_table(table_number)
            except ValueError:
                print("Invalid table number. Please enter a number between 1 and 10.")
        elif choice == '5':
            print("Thank you for using the Restaurant Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
