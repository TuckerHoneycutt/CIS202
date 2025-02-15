def validate_time():
    while True:
        try:
            hours = int(input("Enter hours (0-23): "))
            if hours < 0 or hours > 23:
                print("Hours must be between 0 and 23")
                continue
            
            minutes = int(input("Enter minutes (0-59): "))
            if minutes < 0 or minutes > 59:
                print("Minutes must be between 0 and 59")
                continue
            
            return hours, minutes
            
        except ValueError:
            print("Please enter valid integer numbers")

def main():
    hours, minutes = validate_time()
    print(f"Time entered: {hours:02d}:{minutes:02d}")

if __name__ == "__main__":
    main()
