from stats import (get_num_words, get_chars_dict, get_sorted_dict)
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    num_words = get_num_words(file_content)
    char_dict = get_chars_dict(file_content)
    sorted_dict = get_sorted_dict(char_dict)
    print_report(file_path, num_words, sorted_dict)
    

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def print_report(file_path, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dic in sorted_dict:
        if not dic["char"].isalpha():
            continue
        print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")
    
    

main()
