class Item:
    def __init__(self, item_id, name, description, price):  #constructor
        self.item_id = item_id  #instance variables
        self.name = name
        self.description = description
        self.price = price

    def __str__(self): 
         return (f"Product ID: {self.item_id}\n"
                f"Product Name: {self.name}\n"
                f"Product Description: {self.description}\n"
                f"Product Price: ₱{self.price:.2f}")

items = {}  #Dictionary to store items

def add_item():
    try:
        print(" ADD ITEM ".center(40, '-'))
        item_id = input("Enter Item ID (6 digits): ").strip()
        if not item_id.isdigit() or len(item_id) != 6: #checks if the ID is number and has 6 digits
            print("-" * 40)
            print("Error: Item ID must be a 6-digit number.") #error message
            print("-" * 40)
            return 
 
        if item_id in items: #checks if the item ID in already existing (id needs to be unique)
            print("-" * 40)
            print("Error: Item ID already exists.")
            print("-" * 40)
            return 

        name = input("Enter Item Name: ").strip() #remove unnecessary spaces
        if not name: #checks if the user entered a value 
            print("-" * 40)
            print("Error: Item Name cannot be empty.") 
            print("-" * 40)
            return 

        description = input("Enter Item Description: ").strip()
        if not description:
            print("-" * 40)
            print("Error: No Description Entered.")
            print("-" * 40)
            return

        price = float(input("Enter Item Price: ₱ "))
        if price <= 0:
            print("-" * 40)
            print("Error: Price must be more than 0.")
            print("-" * 40)
            return 

        items[item_id] = Item(item_id, name, description, price)
        print("-" * 40)
        print(f"Item ID {item_id} is Added Successfully.")
        print("-" * 40)

    except ValueError: #invalid value
        print("-" * 40)
        print("Error: Invalid input. Try Again!")
        print("-" * 40)
        return


def view_items():
    if not items:
        print("-" * 40)
        print("No items available. Add one first.")
        print("-" * 40)
        return

    print(" LIST OF ITEMS ".center(40, '-'))
    for item in items.values():
        print(item)
        print("-" * 40)


def update_item():
    view_items()
    
    print(" UPDATE ITEM ".center(40, '-'))
    item_id = input("Enter Item ID to update: ").strip()
    if not item_id.isdigit() or len(item_id) != 6: #checks the validity of item ID, similar to add items
        print("-" * 40)
        print("Error: Item ID must be a 6-digit number.")
        print("-" * 40)
        return

    if item_id not in items: #checks if the item id exist
        print("-" * 40)
        print("Error: Item ID does not exist.")
        print("-" * 40)
        return

    while True: #list of options for users to update
        print("=" * 40)
        print("What do you want to update?".center(40))
        print("=" * 40)
        print("[1] Item Name".center(38))
        print("[2] Item Description".center(43))
        print("[3] Item Price".center(38))
        print("[0] Go Back".center(36))
        print("-" * 40)
        choice = input("Enter your choice: ")

        if choice == '1':
            new_name = input("Enter new Item Name: ").strip()
            if new_name:
                items[item_id].name = new_name #store the new name to items dictionary
                print("-" * 40)
                print("Item Name Updated Successfully!")
                print("-" * 40)
            else:
                print("-" * 40)
                print("Error: Item Name cannot be empty.")
                print("-" * 40)

        elif choice == '2':
            new_description = input("Enter new Item Description: ").strip()
            items[item_id].description = new_description #store the new desc to items dictionary
            print("-" * 40)
            print("Item Description Updated Successfully!")
            print("-" * 40)

        elif choice == '3':
            new_price = input("Enter new Item Price: ₱ ").strip()
            if new_price.replace(".", "").isdigit():
                price = float(new_price)
                if price > 0:
                    items[item_id].price = price #store the new price to items dictionary
                    print("-" * 40)
                    print("Item Price Updated Successfully!")
                    print("-" * 40)
                else:
                    print("-" * 40)
                    print("Error: Price must be greater than zero.")
                    print("-" * 40)
            else:
                print("-" * 40)
                print("Error: Invalid Price! Enter a valid number.")
                print("-" * 40)

        elif choice == '0':
            break

        else:
            print("-" * 40)
            print("Invalid choice. Please try again.")
            print("-" * 40)


def delete_item():
    view_items()

    item_id = input("Enter Item ID to delete: ").strip()
    if not item_id.isdigit() or len(item_id) != 6: #checks the validity of item id
        print("-" * 40)
        print("Error: Item ID must be a 6-digit number.")
        print("-" * 40)
        return

    if item_id not in items: #checks if the item id exist
        print("-" * 40)
        print("Error: Item ID does not exist.")
        print("-" * 40)
        return

    confirm = input("Proceed with item deletion? (yes/no): ").strip().lower() #asks user to confirm deletion
    if confirm == "yes":
        del items[item_id]
        print("-" * 40)
        print(f"Item ID {item_id} is Deleted Successfully.")
        print("-" * 40)
    else:
        print("-" * 40)
        print("Deletion canceled.")
        print("-" * 40)


# Main menu
while True:
    print("=" * 40)
    print(" ITEM MANAGEMENT SYSTEM ".center(40, '='))
    print("[1]. Add Item".center(37))
    print("[2]. View Items".center(40))
    print("[3]. Update Item".center(40))
    print("[4]. Delete Item".center(40))
    print("[0]. Exit".center(33))
    print("=" * 40)

    choice = input("Enter your choice: ")
    print("-" * 40)
    
    if choice == "1":
        add_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "0":
        print("Thank you. Have a nice day!")
        print("-" * 40)
        break
    else:
        print("Invalid choice. Try Again!")
        print("-" * 40)
