def get_num_words(book_text):
    words = book_text.split()
    num_words = 0
    for word in words:
        num_words +=1
    return num_words


def get_char_count(book_text):
    chars = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in chars:
            chars[char] += 1
        else:
           chars[char] = 1
    
    return chars


def sorted_dict(char_dictionary):
    char_list = []
    for char in char_dictionary:
        char_list.append({"char": char, "count": char_dictionary[char]})

    def sort_on(char_dict):
        return char_dict["count"]
        
    char_list.sort(reverse=True, key=sort_on)
    return char_list
