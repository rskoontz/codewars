#!/usr/bin/env python3

def remove_every_other(my_list):
    return print(my_list[0::2])

def main():
    my_list = ['Hello', 'Goodbye', 'Hello Again', 'This is the 4th element']
    remove_every_other(my_list)

if __name__ == "__main__":
    main()