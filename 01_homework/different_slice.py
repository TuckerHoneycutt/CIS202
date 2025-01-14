"""
CIS.202.W05
Name: Tucker Honeycutt
Date: 01-13-2025
A#: a00341746
Assignment: HW #1 
Program: different_slice.py 
"""


# Constants
SLICES_PER_PIZZA = 8
FAMILY_SIZE = 4

# Dictionary to store each person's slices
family_slices = {}

# Get input for each family member using a for loop
print("Program: Different number of slices for each person")
for person_num in range(1, FAMILY_SIZE + 1):
    while True:
        try:
            slices = int(input(f"Enter slices for person {person_num}: "))
            if slices < 0:
                print("Please enter a non-negative number")
                continue
            family_slices[f"Person {person_num}"] = slices
            break
        except ValueError:
            print("Please enter a valid number")

# Calculate total slices needed using sum()
total_slices_needed = sum(family_slices.values())

# Calculate number of whole pizzas needed
pizzas_needed = (total_slices_needed + SLICES_PER_PIZZA - 1) // SLICES_PER_PIZZA

# Calculate leftover slices
leftover_slices = (pizzas_needed * SLICES_PER_PIZZA) - total_slices_needed

# Print results
print("\nOrder Summary:")
for person, slices in family_slices.items():
    print(f"{person} wants {slices} slices")
print(f"Total slices needed: {total_slices_needed}")
print(f"Number of pizzas needed: {pizzas_needed}")
print(f"Number of leftover slices: {leftover_slices}")
