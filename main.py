from stats import word_counter
from stats import char_counter
from stats import sorted_list

def get_book_text(filepath):
    
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents
  
 


        
   
chars = char_counter("books/frankenstein.txt")
sorted_chars = sorted_list(chars)

print("--------- Character Count -------")
for item in sorted_chars:
    ch = item["char"]
    if not ch.isalpha():
        continue
    print(f"{ch}: {item["num"]}")

