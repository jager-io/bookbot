
def word_counter(text):
        word_list = text.split()
        word_count = len(word_list)
        return word_count

def char_counter(text):    
        chars = {}
        l_letters = text.lower()
       
    
        for char in l_letters:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        return(chars)

def sort_on(item):
    return item["num"]
 
def sorted_list(sorts_dict):
    result = []
    for ch, cnt in sorts_dict.items():
        result.append({"char": ch, "num": cnt})
    result.sort(reverse=True, key=sort_on)
    return (result)


