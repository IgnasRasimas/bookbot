import string

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(get_word_count(file_contents))
    print(count_letters(file_contents))


def get_word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dictionary = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char in string.ascii_letters:
            if char in letter_dictionary:
                letter_dictionary[char] +=1
            else:
                letter_dictionary[char] = 1
    return letter_dictionary

main()