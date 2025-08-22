from operator import itemgetter

def count_words(book):
    count = len(book.split())
    return count 


def all_elements(book:str) -> dict:
    book = book.lower()
    elements = {}

    for char in book:
        if char >= 'a' and char <= 'z' or char.isalpha(): 
            elements[char] = elements.get(char,0)+1
    return dict(sorted(elements.items(), key=itemgetter(1), reverse=True))




