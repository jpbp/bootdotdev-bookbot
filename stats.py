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

def sort_on(dict):
    return dict["num"]

def get_return_order_dic(dic_characters):
    list_dic_characters = []
    for key,value in dic_characters.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        list_dic_characters.append(new_dict)
    
    list_dic_characters.sort(reverse=True, key=sort_on)
    #print(list_dic_characters)
    return list_dic_characters
    
    
    