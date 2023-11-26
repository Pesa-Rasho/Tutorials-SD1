pizza_toppings = []

available_toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bell Peppers", "Olives", "Cheese"]

def display_menu():
    print("\nMenu:")
    print("a: Add a topping")
    print("r: Remove a topping")
    print("o: Order the current pizza")
    print("s: Start the current pizza over")
    print("q: Quit the program")

def display_available_toppings():
    print("\nAvailable toppings:")
    print(available_toppings)

while True:
    display_menu()
    user_choice = input("Enter your choice: ")

    if user_choice.lower() == 'a':
        display_available_toppings()
        topping_to_add = input("Enter a topping to add: ")
        if topping_to_add.capitalize() in available_toppings:
            pizza_toppings.append(topping_to_add.capitalize())
            print(f"{topping_to_add.capitalize()} added to your pizza!")
        else:
            print("Sorry, that topping is not available. Please choose from the available toppings.")

    elif user_choice.lower() == 'r':
        if pizza_toppings:
            display_available_toppings()
            topping_to_remove = input("Enter a topping to remove: ")
            if topping_to_remove.capitalize() in pizza_toppings:
                pizza_toppings.remove(topping_to_remove.capitalize())
                print(f"{topping_to_remove.capitalize()} removed from your pizza!")
            else:
                print("Sorry, you don't have that topping on your pizza.")
        else:
            print("You don't have any toppings to remove.")

    elif user_choice.lower() == 'o':
        if pizza_toppings:
            print("\nYour pizza with the following toppings has been ordered:")
            print(pizza_toppings)
            break  
        else:
            print("Your pizza is empty. Please add toppings before ordering.")

    elif user_choice.lower() == 's':
        pizza_toppings = []
        print("Current pizza has been started over. It's now empty.")

    elif user_choice.lower() == 'q':
        print("Quitting the program. Goodbye!")
        break  

    else:
        print("Invalid choice. Please choose a valid option from the menu.")
