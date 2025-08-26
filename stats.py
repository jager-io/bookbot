
def word_counter(filepath):
    with open(filepath) as file:
        data = file.read()
        word_list = data.split()
        word_count = len(word_list)
        return(f'{word_count} words found in the document')

def char_counter(filepath):
    
    
    with open(filepath) as file:
        data = file.read()
        letters = []
        chars = {}
        l_letters = data.lower()
        letters = list(l_letters)
    
        for letter in letters:
            if letter in chars:
                chars[letter] += 1
            else:
                chars[letter] = 1
        return(chars)

def sort_on(item):
    return item["num"]
 
def sorted_list(sorts_dict):
    result = []
    for ch, cnt in sorts_dict.items():
        result.append({"char": ch, "num": cnt})
    result.sort(reverse=True, key=sort_on)
    return (result)


