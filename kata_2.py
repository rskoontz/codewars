#!/usr/bin/env python3

def friend(x):
    friend_list = x
    pos = [n for n in friend_list if (len(n) == 4)]
    return pos

def main():
    x = (["Ryan", "Kieran", "Mark",])
    friend(x)

if __name__ == "__main__":
    main()