#========The beginning of the class==========
class Shoe:
    """This is a class for shoes."""

    def __init__(self, country, code, product, cost, quantity):
        """The constructor for shoe class uses parameters.
        
        Parameters:
        country (str): The country the stock is located.
        code (str): The code of the shoe.
        product (str): The name of the shoe.
        cost (str): The cost of a single shoe unit.
        quantity (str): The quantity of shoes in stock.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """This function returns the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """This function returns the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        return f"{self.country:<20}{self.code:<15}{self.product:<25}{self.cost:<10}{self.quantity}"


#==========Functions outside the class==============
def read_shoes_data():
    """This function checks for a file called 'inventory.txt' and reads the content to update the shoe list."""
    # Create an empty global list variable to store shoe objects.
    global shoe_list
    shoe_list = []

    # Check if the file is present and if so split each line into object components and update the shoe list.
    # Else if the file is not present print an error message.
    inventory_file = None
    try:
        inventory_file = open("inventory.txt", "r", encoding="utf-8")
        next(inventory_file)
        lines = inventory_file.readlines()
        for line in lines:
            components = line.strip("\n").split(",")
            shoe = Shoe(components[0], components[1], components[2], components[3], components[4])
            shoe_list.append(shoe)
        print("The file has been found and the shoe list has been updated.")

    except FileNotFoundError:
        print("The file was not found.")
    
    finally:
        if inventory_file is not None:
            inventory_file.close()


def update_file():
    """This function updates the file using the shoe list."""
    with open("inventory.txt", "w", encoding="utf-8") as inventory_file:
        inventory_file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            inventory_file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")


def capture_shoes():
    """This function requests shoe information from the user to create a new shoe that is added to the list and file."""
    # Request shoe details from the user.
    country = input("Enter the country the stock is located: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the product name: ")
    while True:
        try:
            cost = int(input("Enter the cost of the product: "))
            break
        except ValueError:
            print("This was not a valid number. Try again.\n")

    while True:
        try:
            quantity = int(input("Enter the stock quantity: "))
            break
        except ValueError:
            print("This was not a valid number. Try again.\n")

    # Create a shoe then add it to the list and update the file.
    shoe = Shoe(country, code, product, str(cost), str(quantity))
    shoe_list.append(shoe)

    update_file()

    print("This shoe has been added to the inventory.")


def view_all():
    """This function prints all the shoes in the list."""
    print(f"{'Country':<20}{'Code':<15}{'Product':<25}{'Cost':<10}Quantity")
    print(f"{'-' * 80}")
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    """This function checks for the shoe with the lowest quantity and updates the file with the new quantity."""
    # Add the quantity of each shoe to a list and check for the lowest quantity.
    quantity_list = []
    for shoe in shoe_list:
        quantity_list.append(int(shoe.get_quantity()))
    lowest = min(quantity_list)
    position = quantity_list.index(lowest)

    # Print the shoe with the lowest quantity and ask the user how much they would like to add.
    print(f"{'Country':<20}{'Code':<15}{'Product':<25}{'Cost':<10}Quantity")
    print(shoe_list[position])
    print("\nThis shoe has the least stock.")
    num_to_add = int(input("Enter the quantity you want to add: "))

    # Update the shoe list with the new quantity.
    for shoe in shoe_list:
        if shoe.get_quantity() == str(lowest):
            shoe.quantity = str(int(shoe.quantity) + num_to_add)

    # Update the file using the updated shoe list.
    update_file()
    
    print("Shoe stock has been updated.")


def search_shoe():
    """This function prints the shoe with the code provided by the user."""

    # Loop through requesting a shoe code from the user and print the shoe else print an error message.
    while True:
        code = input("Enter shoe code (or '-1' to return to the menu): ")
        if code == "-1":
            break

        shoe_found = False

        for shoe in shoe_list:
            if code == shoe.code:
                print(f"{'Country':<20}{'Code':<15}{'Product':<25}{'Cost':<10}Quantity")
                print(shoe)
                shoe_found = True
                break

        if shoe_found == False:
            print("That was an invalid code. Try again.")

        elif shoe_found == True:
            break


def value_per_item():
    """This function prints the total value of each shoe in the list."""

    # Calculate the total value for each shoe and store it in a list called 'values'.
    # Print each shoe name with the value.
    values = []
    print(f"{'Product':<25}Total Value")
    for shoe in shoe_list:
        value = float(shoe.get_cost()) * int(shoe.get_quantity())
        print(f"{shoe.product:<25}{round(value)}")


def highest_qty():
    """This function checks for the shoe with the highest quantity and displays it as for sale."""

    # Add the quantity of each shoe to a list and check for the highest quantity.
    quantity_list = []
    for shoe in shoe_list:
        quantity_list.append(int(shoe.get_quantity()))
    highest_quantity = max(quantity_list)

    # For each shoe in the shoe list if the quantity is the highest print that shoe as for sale.
    for shoe in shoe_list:
        if shoe.get_quantity() == str(highest_quantity):
            print(f"{'Country':<20}{'Code':<15}{'Product':<25}{'Cost':<10}Quantity")
            print(shoe)
            print("\nThis shoe is for sale!")

#==========Main Menu=============
print("Welcome to the shoe inventory tracker.")

# Create the list of shoes from the file.
read_shoes_data()

# Loop through requesting an option from the menu.
while True:
    menu = input("""\nSelect one of the options below:
u  - update shoe list
a  - add shoe
va - view all
rs - restock
s  - search shoe
dv - display values
ds - display shoe on sale
e  - exit
""")
    # Call the relevant function depending on the selected option.
    # For certain options display an error message instead if there are no shoes in the list.
    if menu == "u":
        read_shoes_data()

    elif menu == "a":
        capture_shoes()

    elif menu == "va":
        if len(shoe_list) == 0:
            print("There are no shoes in the list to view.")
        else:
            view_all()

    elif menu == "rs":
        if len(shoe_list) == 0:
            print("There are no shoes in the list to restock.")
        else:
            re_stock()

    elif menu == "s":
        if len(shoe_list) == 0:
            print("There are no shoes in the list to search.")
        else:
            search_shoe()

    elif menu == "dv":
        if len(shoe_list) == 0:
            print("There are no shoes in the list to display values of.")
        else:
            value_per_item()

    elif menu == "ds":
        if len(shoe_list) == 0:
            print("There are no shoes in the list to show a sale.")
        else:
            highest_qty()

    elif menu == "e":
        exit()
    else:
        print("That was an invalid menu option. Try again.")

