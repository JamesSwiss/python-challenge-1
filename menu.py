#Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Create an empty list to store the customer's order. 
#They're using dictionary format from LN 2 to 51 
order_list = []

# Launch the store and present a greeting to the customer
#Verbatim from starter code 
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
#Copied verbatim from starter code    
## Ask the customer from which menu category they want to order    
    print("From which menu would you like to order? ")
#Verbatim from starter code

# Create a variable for the menu item number
    i = 1
    menu_items = {}
#Verbatim from starter code
#Assigning the variable i with the value 1 then creating an empty dictionary here.
# Have to use addition assignment += with this later on

# Print the options to choose from menu headings (all the first level
#dictionary items in menu).

    for key in menu.keys():
#This is a for loop using the method .key 
#Key is the variable name being associated with each value
        print(f"{i}: {key}")
#Printing the f-string i, holding a value of 1. 1: key, 2: key

#Store the menu category associated with its menu item number
        menu_items[i] = key
#Now printing should show 1: Snacks
#Add 1 to the menu item number. Starter code 
        i += 1 
# Need this to show each subsequent loop adding 1.Print should show 1 is snacks. 2: Meals 3: Drinks 4: Desserts
#Get the customer's input. 2. Ask customer to input menu item number. Starter code 
    menu_category = input("Type menu number: ")
# Check if the customer's input is a number. Starter code using .isdigit
    if menu_category.isdigit():
# Check if the customer's input is a valid option. Starter code
        if int(menu_category) in menu_items.keys():
#If conditional. If the integer input by the customer is one of the key options in the menu_items
# Save the menu category name to a variable. Starter code
#Assigning menu_items to the variable, converting numbers or string input here to an integer with int function
            menu_category_name = menu_items[int(menu_category)]
#Print out the menu category name they selected. Starter code
            print(f"You selected {menu_category_name}")
## Print out the menu options from the menu_category_name. Starter code. 
# Hitting 2 after menu order prompt should show customer: What Meals item would you like to order?
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            for key, value in menu[menu_category_name].items():
# Check if the menu item is a dictionary to handle differently. Starter code
                if type(value) is dict:
#Conditional statement if the value is a dictionary
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
#Up to here is nested code following the for loop. Below handles if that condition is't met 
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            menu_selection = input("Enter your selection: ")
#A-Check if the quantity is a number
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)

                if 1 <= menu_selection <= len(menu_items):
                    selected_item = menu_items[menu_selection]["Item name"]
                    quantity = input(f"How many {selected_item} would you like to order? (Default is 1): ")
#B-Default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1
#Add the item name, price, and quantity to the order list
#Code from previous activities, stack overlflow,and Bing ask. 
                    order_list.append({
                        "Item name": selected_item,
                        "Price": menu_items[menu_selection]["Price"],
                        "Quantity": quantity
                    })
                else:
                    print("Error: Invalid menu selection.")
            else:
                print("Error: Please enter a number.")
# Tell the customer they didn't select a menu option. Starter code
        else:
            print(f"{menu_category} was not a menu option.")
# Tell the customer they didn't select a number. Starter code
    else:
        print("You didn't select a number.")
#Ask the customer if they would like to order anything else. Starter code
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").lower()
#If conditional is met, Boolean of true. Continue loop starting at "From which menu..."
#Copied from activities lessons
        if keep_ordering == 'y':
            place_order = True
            break
# Since the customer decided to stop ordering, thank them for their order. Prints message.
        elif keep_ordering == 'n':
            place_order = False
            print("Thank you for your order.")
#Exit the keep ordering question loop
            break
#Tell the customer to try again. If they don't enter Y or N error message prints. 
        else:
            print("Error: Try again. Please enter 'Y' or 'N'.")

# Print out the customer's order
#If-else statement used 
if order_list:
    print("This is what we are preparing for you.\n")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
#Loop through the items in the customer's order with for loop. Copied from Bing Ask using past acvities as example
    for order_item in order_list:
        item_name, price, quantity = order_item["Item name"], order_item["Price"], order_item["Quantity"]
#Calculate the number of spaces for formatted printing        
        num_name_spaces = 26 - len(item_name)
        num_price_spaces = 8 - len(str(price))
        num_quantity_spaces = 10 - len(str(quantity))

        name_spaces = " " * num_name_spaces
        price_spaces = " " * num_price_spaces
        quantity_spaces = " " * num_quantity_spaces

        print(f"{item_name}{name_spaces}| ${price:.2f}{price_spaces}| {quantity}{quantity_spaces}")
#Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()and print the prices. Google search for syntax and Bing ask 
    total_price = sum(item["Price"] * item["Quantity"] for item in order_list)
    print("\nTotal Price: ${:.2f}".format(total_price))
else:
    print("No items in the order.")
