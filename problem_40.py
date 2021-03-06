# -*- coding: utf-8 -*-
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

import time

def main():
    num = []
    i = 0
    while len(num) < 1000001:
        for n in str(i):
            num.append(int(n)) 
        i+=1
    s = num[1] * num[10] * num[100] * num[1000] * num[10000] * num[100000] * num[1000000]
    print(s)
    
    
if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
