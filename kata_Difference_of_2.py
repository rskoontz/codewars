#!/usr/bin/env python3

def twos_difference(lst):
    
    final_list = []
    
    for x in lst:
        for y in lst:
            if y - x == 2:
                final_list.append((x,y))
                continue
            elif y - x == 2:
                final_list.append((x,y))
        final_list.sort()
    return print(final_list)

def main():
    
    lst = [6,3,4,1,5]
    twos_difference(lst)

if __name__ == "__main__":
    main()