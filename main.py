def get_book_text(filepath):
    
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents
  
 


def word_counter(filepath):
    with open(filepath) as file:
        data = file.read()
        word_list = data.split()
        word_count = len(word_list)
        print(f'{word_count} words found in the document')
        
   

print(word_counter("books/frankenstein.txt"))
