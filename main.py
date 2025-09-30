import sys
from stats import get_num_words, count_words, sort_characters_by_count



def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()



def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv[1]) == 0 :
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    sorted_characters = sort_characters_by_count(count_words(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(get_num_words(book_text))
    print("--------- Character Count -------")

    for char_data in sorted_characters:
        print(f"{char_data['char']}: {char_data['num']}")
    print("============= END ===============")

if __name__ == '__main__':
    main()