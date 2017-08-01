#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:08:48 2017

@author: smsxgz
"""

l =[[1, 9],
    [3, 3],
    [7, 7],
    [9, 1]
    ]

'''
l = []
for i in range(10):
    for j in range(10):
        if i * j % 10 == 9:
            l.append([i, j])
'''

'''
def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

for i in range(20):
    for j in range(20):
        for a, b in l:
            x, y = 10 * i + a, 10 * j + b
            n = (1000 - x) * (1000 - y)
            if is_palindrome(n):
                print(x, y)
'''


def reverse(n):
    reverse = 0
    while n > 0:
        reverse = 10 * reverse + (n % 10)
        n = n // 10
    return reverse

def isPalindrome(n):
    return n == reverse(n)

def LargestPalindrome(n_max):
    largestPalindrome = 0
    a = min((n_max - 1) // 100, 999)
    #a = 999
    while a >= 100:
        b = min((n_max - 1) // a, 999)
        #b = 999
        while b >= a:
            n = a * b
            if n <= largestPalindrome:
                break
            if isPalindrome(n):
                largestPalindrome = n
            b = b - 1
        a = a - 1
    return largestPalindrome
print(LargestPalindrome(999 * 999))