def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents += f.read()    
    return file_contents
 
def get_count_of_words_text(book):
    words = book.split()
    count_words = len(words)
    return count_words 

def get_number_of_times_each_character(book):
    characters = {}
    book = book.lower()
    for char in book:
        if (not char in characters):
            characters[char] = 1
        else:
            characters[char] += 1
    return characters
    