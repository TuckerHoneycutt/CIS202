import re
import sys

def get_unique_words(filename):
    try:
        # Open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Convert to lowercase and split into words using regex
        words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
        
        # Create a set of unique words
        unique_words = set(words)
        
        # Return the set of unique words
        return unique_words
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return set()
    except Exception as e:
        print(f"An error occurred: {e}")
        return set()

def main():
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python unique_words.py <filename>")
        return
    
    filename = sys.argv[1]
    unique_words = get_unique_words(filename)
    
    if unique_words:
        print(f"Found {len(unique_words)} unique words in '{filename}':")
        # Sort the words alphabetically for better readability
        for word in sorted(unique_words):
            print(word)

if __name__ == "__main__":
    main()
