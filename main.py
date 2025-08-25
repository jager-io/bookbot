from stats import word_counter
from stats import char_counter
def get_book_text(filepath):
    
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents
  
 


        
   

print(word_counter("books/frankenstein.txt"))
print(char_counter("books/frankenstein.txt"))