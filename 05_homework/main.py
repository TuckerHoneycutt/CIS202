def calculate_numbers():
    try:
        with open('numbers.txt', 'r') as file:
            numbers = []

            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Warning: Could not convert '{line.strip()}' to a number. Skipping this value")

            if not numbers:
                print("No valid numbers found in the file")
                return 

            total_sum = sum(numbers)
            average = total_sum / len(numbers)
            
            print(f"Sum of numbers: {total_sum}")
            print(f"Average of numbers: {average:.2f}")
            print(f"Number of valid entries: {len(numbers)}")

    except IOError:
        print("Error: Could not open or read the file 'numbers.txt'")

if __name__ == "__main__":
    calculate_numbers()
