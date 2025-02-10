# Initalize the inventory using a dictionary. Variables as the keys, and number of items as values.
inventory = { 'muffin': 10, 'cupcake': 10 }

print("Welcome to my cool bakery!")
print("\nEnter 'muffin' to buy a muffin or 'cupcake' to buy a cupbcake.\nEnter '0' to exit.")

# Putting logic within a try loop to handle errors like unexpected keystrokes or keyboard interrupts 
try:
    # Start a loop, defining a break condition when false.
    while True:
        # Get the input, strip the whitespace after the end of the input, convert to lowercase
        item = input("What would you like to buy? ").strip().lower()

        # Break condition if user inputs '0'
        if item == '0':
            print(f"muffins: { inventory['muffin'] } cupcakes: { inventory['cupcake'] }")
            break

        # Check if the item exists in the inventory
        if item in inventory:
            # Check to see if there are any available. (Value > 0)
            if inventory[item] > 0:
                # Decrease inventory amount by 1 if available
                inventory[item] -= 1
                print(f"Purchased 1 {item}!")
            else:
                print("Out of stock")
        else:
            print("Invalid item. please enter 'muffin' or 'cupcake'.")

# Logic for keyboard interrupt and print summary 
except KeyboardInterrupt:
    print("\nThank you for visiting! Here's our remaining inventory:")
    print(f"muffins: { inventory['muffin'] } cupcakes: { inventory['cupcake'] }")
