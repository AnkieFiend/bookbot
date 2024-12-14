"""
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

def word_count(path)
    text=

main()
"""

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_text_count(text)
    num_repeats = num_characters(text)
    statement = iterate_chars(num_repeats)
    finale = ""
    finale = f"--- Begin report of {book_path} ---\n{num_words} words found in the document\n\n{statement}\n--- End report ---"
    print(finale)

def iterate_chars(num_repeats):
    counter=""
    for chars in num_repeats:
        nums = num_repeats[chars]
        if chars.isalpha():
            counter +=f"The '{chars}' character was found {nums} times\n"
    return counter

def num_characters(text):
    text_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in text_dict:
            text_dict[letter] += 1
        else:
            text_dict[letter] = 1
    return text_dict

def get_text_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
