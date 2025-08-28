from stats import word_counter
from stats import char_counter
from stats import sorted_list
import sys 

  
def main():

    sys_argv_length = len(sys.argv)
   
    if sys_argv_length >= 2:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
    else:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
   
    #### how to make two arguments


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    word_count = word_counter(text)
    print(f"Found {word_count} total words") 
    chars = char_counter(text)
    sorted_chars = sorted_list(chars)

    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item["num"]}")
    print("============= END ===============")


def get_book_text(filepath):
    
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

main()
