from stats import count_words,all_elements
import sys 

def get_book_text(file_book):
    with open(file_book) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    filepath = sys.argv[1] 

    content = get_book_text(filepath) 
    words = count_words(content)

    result = all_elements(content)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for key,val in result.items():
        print(f"{key}: {val}")

    print("============= END ===============")

main() 
