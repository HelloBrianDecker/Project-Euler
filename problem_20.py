# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 22:12:07 2019

@author: Hello
"""
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def factorialDigitSum(n):
    if n == 1:
        return n
    else:
        return n * factorialDigitSum(n-1)
        
def numToString(n):
    numbers = []
    for i in str(n):
        numbers.append(int(i))
    print(sum(numbers))
        
numToString(factorialDigitSum(100))