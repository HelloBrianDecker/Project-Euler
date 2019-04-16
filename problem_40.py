# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:47:42 2019

@author: Hello
"""
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