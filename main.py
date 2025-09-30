from stats import get_num_words



def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()



def main():

    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    print(get_num_words(book_text))


if __name__ == '__main__':
    main()