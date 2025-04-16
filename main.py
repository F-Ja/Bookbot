import sys
from stats import (
    get_char_count, 
    get_num_words,
    sorted_dict
)


def get_book_text(path):
    with open (path) as file:
        content = file.read()
    return content


def print_report(path, num_words, sorted_list_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list_chars:
        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chars_count = get_char_count(book_text)
    sorted_list_chars = sorted_dict(chars_count)
    print_report(book_path, num_words, sorted_list_chars)


main()
