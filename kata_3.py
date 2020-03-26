#!/usr/bin/env python3

#Beginner Series #3 Sum of Numbers

#def get_sum(a,b):
#    for i in range(a, b):
#        return sum(number for number in range)

def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        return print(sum(range(a,b + 1)))
    elif a > b:
        return print(sum(range(b,a + 1)))






        
def main():
    get_sum(0,1)

if __name__ == "__main__":
    main()


#res = sum(x for x in range(100, 2001) if x % 3 == 0) ##generator expression