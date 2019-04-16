# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:22:14 2019

@author: Hello
"""
'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import time


def main():
    pal = []
    for n in range(1,1000001):
        if isPalindrome(n):
            if isPalindrome(tobinary(n)):
                if n not in pal:
                    pal.append(n)
        else:
            continue
    print(pal)
    print(sum(pal))
    
def isPalindrome(p):
    pal = [int(i) for i in str(p)]
    if pal[::-1] == pal:
        return True
    
def tobinary(n):
    binary = "{0:b}".format(n)
    return binary
        
        

if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
        
    