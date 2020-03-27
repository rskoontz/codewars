#!/usr/bin/env python3

def is_isogram(string):
    string_lc = string.lower()
    letter_dict = {}

    for letter in string_lc:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    #use of dict comprehension with the all func
    return print(all(x <= 1 for x in letter_dict.values()))

def main():
    string = "moOse"
    is_isogram(string)

    

if __name__ == "__main__":
    main()