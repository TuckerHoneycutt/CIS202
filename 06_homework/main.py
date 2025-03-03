def main():
    # List of month names
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # Empty list to store rainfall data
    rainfall_data = []

    # Get rainfall data for each month
    print("Enter the rainfall for each month:")
    for month in months:
        valid_input = False
        while not valid_input:
            try:
                rain = float(input(f"{month}: "))
                if rain < 0:
                    print("Rainfall cannot be negative. Please enter a valid value.")
                else:
                    rainfall_data.append(rain)
                    valid_input = True
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Calculate total rainfall
    total_rainfall = sum(rainfall_data)

    # Calculate average monthly rainfall
    average_rainfall = total_rainfall / len(months)

    # Find month with highest rainfall
    max_rainfall_index = rainfall_data.index(max(rainfall_data))
    max_rainfall_month = months[max_rainfall_index]

    # Find month with lowest rainfall
    min_rainfall_index = rainfall_data.index(min(rainfall_data))
    min_rainfall_month = months[min_rainfall_index]

    # Display results
    print("\nRainfall Summary:")
    print(f"Total yearly rainfall: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month with highest rainfall: {max_rainfall_month} ({rainfall_data[max_rainfall_index]:.2f} inches)")
    print(f"Month with lowest rainfall: {min_rainfall_month} ({rainfall_data[min_rainfall_index]:.2f} inches)")

if __name__ == "__main__":
    main()
