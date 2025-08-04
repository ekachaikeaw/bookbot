from stats import get_num_words, get_chars_dict

def main():
    file_content = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(file_content)
    char_dict = get_chars_dict(file_content)
    print(f"{num_words} words found in the document")
    print(char_dict)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    

    

main()
