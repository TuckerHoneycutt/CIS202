def format_names(name_string):
    names = [name.strip() for name in name_string.split(',')]
    
    formatted_names = []
    for name in names:
        parts = name.split()
        
        if len(parts) >= 2:
            last_name = parts[-1]
            first_name = ' '.join(parts[:-1])
            
            formatted_names.append(f"{last_name}, {first_name}")
    
    formatted_names.sort()
    
    return formatted_names

def main():
    user_input = input("Enter a list of names separated by commas: ")
    
    result = format_names(user_input)
    
    output = '; '.join(result)
    print(output)

if __name__ == "__main__":
    main()
