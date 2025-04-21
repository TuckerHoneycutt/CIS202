import re
import sys

def analyze_text_file(filename):
    try:
        # Open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Convert to lowercase and split into words using regex
        words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
        
        # Create a set of unique words 
        unique_words_set = set(words)
        
        # Create a dictionary to count word frequencies 
        word_frequency_dict = {}
        for word in words:
            # If word exists in dictionary, increment its count, otherwise set count to 1
            if word in word_frequency_dict:
                word_frequency_dict[word] += 1
            else:
                word_frequency_dict[word] = 1
        
        return unique_words_set, word_frequency_dict
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return set(), {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return set(), {}

def main():
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python word_analyzer.py <filename>")
        return
    
    filename = sys.argv[1]
    unique_words, word_frequencies = analyze_text_file(filename)
    
    if unique_words:
        # Display the unique words
        print(f"\n=== UNIQUE WORDS ({len(unique_words)}) ===")
        print("These words appear in the text file (sorted alphabetically):")
        for word in sorted(unique_words):
            print(word)
        
        # Display the word frequencies
        print(f"\n=== WORD FREQUENCIES ===")
        print("Word count for each word (sorted by frequency):")
        # Sort dictionary items by value (frequency) in descending order
        sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_words:
            print(f"{word}: {count}")
        
        # Example of set operations
        print("\n=== SET OPERATIONS EXAMPLE ===")
        # Create a small set of common English words
        common_words = {'the', 'and', 'of', 'to', 'in', 'a', 'is', 'that', 'for', 'it'}
        print("Common English words:", common_words)
        
        # Find intersection 
        common_in_text = unique_words.intersection(common_words)
        print("Common words found in text:", common_in_text)
        
        # Find words in text that are not common
        uncommon_words = unique_words - common_words
        print(f"Number of uncommon words in text: {len(uncommon_words)}")
        
        # Example of dictionary operations
        print("\n=== DICTIONARY OPERATIONS EXAMPLE ===")
        # Find the most frequent word
        most_frequent_word = max(word_frequencies.items(), key=lambda x: x[1])
        print(f"Most frequent word: '{most_frequent_word[0]}' appears {most_frequent_word[1]} times")
        
        # Find words that appear only once
        single_occurrence = {word: count for word, count in word_frequencies.items() if count == 1}
        print(f"Number of words that appear exactly once: {len(single_occurrence)}")

if __name__ == "__main__":
    main()
