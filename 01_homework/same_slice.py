"""
CIS.202.W05
Name: Tucker Honeycutt
Date: 01-13-2025
A#: a00341746
Assignment: HW #1
Program: same_slice.py 
"""


# Constants
SLICES_PER_PIZZA = 8
FAMILY_SIZE = 4

# Dictionary to store family information
family_slices = {}

# Get input with error checking for valid input
print("Program: Same number of slices for everyone")
while True:
    try:
        slices_per_person = int(input("Enter the number of slices each person eats: "))
        if slices_per_person < 0:
            print("Please enter a non-negative number")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

# Create dictionary for each family member
for person_num in range(1, FAMILY_SIZE + 1):
    family_slices[f"Person {person_num}"] = slices_per_person

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
