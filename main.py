import string

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
   
  
    
    counted_letters = dict_to_list(count_letters(file_contents))
    counted_letters.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_word_count(file_contents)} words found in the document")
    print_list_report(counted_letters)
 

def get_word_count(text):
    words = text.split()
    return len(words)


def sort_on(dict):
    return dict["num"]



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

def dict_to_list(dict):
    new_list = []
    for item in dict:
        new_list.append({"char":item, "num":(dict[item])})
    return new_list

def print_list_report(list):
    for i in range(0, len(list)):
        print(f"The {list[i]['char']} character was found {list[i]['num']} times")
main()