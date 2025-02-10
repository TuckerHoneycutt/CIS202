def main():
    try:
        avg_speed = float(input("Enter your average speed in mph: "))
        speed_limit = float(input("Enter the speed limit in mph: "))
        distance = float(input("Enter the distance traveled in miles: "))
    except:
        print("Invalid input. Please enter numeric values.")
        return 

    if avg_speed <= 0 or speed_limit <= 0 or distance <= 0:
        print("Please enter positive values for speeds and distance.")
        return 

    time_at_avg_speed = distance / avg_speed 
    time_at_speed_limit = distance / speed_limit 
    time_saved_hours = time_at_speed_limit - time_at_avg_speed
    time_saved_minutes = time_saved_hours * 60 

    print(f"\nTime saved: {time_saved_minutes:.2f} minutes.")


if __name__ == '__main__':
    main() 
