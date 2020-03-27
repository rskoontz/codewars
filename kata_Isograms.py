#!/usr/bin/env python3

def is_isogram(string):
    string_lc = string.lower()
    letter_dict = {}
    for letter in string_lc:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    print(letter_dict.values())
    return print(all(x <= 1 for x in letter_dict.values()))

        
    #print(letter_dict)
    #for k, v in letter_dict.items():
    #    if v == 1 or v == 0:
    #       return True
    #    else:
    #        return print(False)
    #        
    


    #for v in letter_dict.values():
        #while v == 1 or v == 0:
            #return print(True)
        #else v > 1:
            #return print(False)
    
        
        
        
        
        
        #if v == 1 or v == 0:
        #    return print(True)
        #else:
        #    return False
    #total = print(sum(1 for v in letter_dict.values() if v >= 1))
    #if total <= 1:
    #    return print(True)
    #else:
    #    return print(False)

def main():
    string = "moOse"
    is_isogram(string)
    #res = [ele for key in test_dict for ele in key] 
    #[dict([a, int(x)] for a, x in b.items()) for b in list]
    #for k, v in d.items():
    #print(k, v)

    

if __name__ == "__main__":
    main()