def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_dict = get_char_count(text)
    book_report = get_book_report(letter_dict)
    print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for i in range(0, len(book_report), 1):
        print(
            f"The '{book_report[i].get('Character')}' character was found {book_report[i].get('Count')} times"
        )


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    letters = {}
    for c in text:
        lowered = c.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters


def get_book_report(letter_dict):

    letters = [
        {"Character": key, "Count": value}
        for key, value in letter_dict.items()
        if key.isalpha()
    ]

    def sort_on(dict):
        return dict["Count"]

    letters.sort(reverse=True, key=sort_on)

    return letters


main()
