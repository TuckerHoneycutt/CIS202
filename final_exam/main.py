#   Name: Tucker Honeycutt
#   A#: A00341746
#   Class: CIS-202-W05
#   Final exam


# Attempt to open and read the file
try:
    file = open('numbers-1.txt', 'r')

    # Read all lines and close the file
    lines = file.readlines()
    file.close()

    # Store numbers in a list
    numbers = []
    for line in lines:
        numbers.append(int(line.strip()))

    # Calculate total
    total = 0
    for num in numbers:
        total = total + num

    # Find maximum
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num

    # Calculate average
    average = total / len(numbers)

    # Find unique numbers
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    # Find numbers greater than 200
    greater_than_200 = []
    for num in numbers:
        if num > 200:
            greater_than_200.append(num)

    # Display results
    print("Total of the numbers is:", total)
    print("The maximum number is:", maximum)
    print("The number greater than 200 is:", greater_than_200)
    print("The average of the numbers is:", average)
    print("The unique numbers in file are")
    print(unique_numbers)

except FileNotFoundError:
    print("The file is not found")
