#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:30:03 2020

@author: vdixit
"""


'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

def bin_search(arr, p, x, n):
    l, r = 0, n-1
    ind = -1
    while l <= r:
        m = l + (r-l)//2
        if arr[m]==x:
            if p ==0:
                ind = m
                r = m-1
            else:
                l = m+1
        elif arr[m] > x:
            ind = m
            r = m-1
        else:
            l = m+1
    return ind

# Write your code here
n = int(input())
arr = sorted(list(map(int, input().split())))

Q = int(input())
for _ in range(Q):
    p, x = map(int, input().split())
    cnt = 0

    ind = bin_search(arr, p, x, n)
    if ind == -1:
        print(0)
    else:
        print(n - ind) 
    """ taking so much time
    for num in arr:
        if (p == 0 and num >= x) or (p ==1 and num > x):
            cnt += 1
    """
