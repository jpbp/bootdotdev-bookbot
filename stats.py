def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents += f.read()    
    return file_contents
 
def get_count_of_words_text(book):
    words = book.split()
    count_words = len(words)
    return count_words 