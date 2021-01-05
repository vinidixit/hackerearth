#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:28:51 2020

@author: vdixit
"""


'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def bin_search(k_ranges, k, n):
    l, r = 0, n-1
    while l <=r :
        m = l + (r-l)//2
        left, right = k_ranges[m]
    
        if k >= left and k <= right:
            return m, k-left
        elif k < left:
            r = m - 1
        elif k > right:
            l = m+1
    

n, q = map(int, input().split())
k_ranges = []
ranges = []

prev = 0
for _ in range(n):
    l, r = map(int, input().split())
    diff = r - l
    new_l = prev + 1
    ranges.append((l,r))
    k_ranges.append((new_l, new_l+diff))
    prev = new_l+diff

#print(ranges)
#print(k_ranges, '\n')
for _ in range(q):
    k = int(input())
    ind, shift = bin_search(k_ranges, k, n)
    print(ranges[ind][0] + shift)
