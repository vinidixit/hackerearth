#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:44:24 2020

@author: vdixit
"""


'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def bin_search(arr, x, n):
    l, r = 0, n-1
    ind = -1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] <= x:
            ind = m
            l = m+1
        else:
            r = m-1
    return ind

t = int(input())
radiuses = []

import math
for _ in range(t):
    x, y = map(int, input().split())
    radiuses.append(math.sqrt(x**2 + y**2))

radiuses = sorted(radiuses)

q = int(input())
for _ in range(q):
    r = int(input())
    ind = bin_search(radiuses, r, t)
    if ind == -1:
        print(0)
    else:
        print(ind + 1)



