#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:10:08 2020

@author: vdixit
"""


'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import numpy as np
n = int(input())
arr = list(map(int, input().split()))

x = np.zeros(n, dtype=int)
x[0] = -1
for i in range(1, n):
    cur_i = i-1
    #print(cur_i)
    while cur_i>=0 and arr[i] >= arr[cur_i]:
        cur_i = x[cur_i]
        print(cur_i)
    
    x[i] = cur_i 

y = np.zeros(n, dtype=int)
y[n-1] = -1
for i in range(n-2, -1, -1):
    cur_i = i+1
    while -1<cur_i< n and arr[i]>=arr[cur_i]:
        cur_i = y[cur_i] 
    
    y[i] = cur_i 

for n1, n2 in zip(x, y):
    i = n1+1 if n1!= -1 else -1
    j = n2+1 if n2!= -1 else -1
    print(i+j, end=' ')
"""
max_so_far = None
for i, num in enumerate(arr):
    if not max_so_far:
        max_so_far = i
        print('-1', end= ' ')
    elif arr[max_so_far] > num:
        print(max_so_far+1, end = ' ')
    elif arr[max_so_far] <= num:
"""

"""
x = []
for i, num1 in enumerate(arr):
    found = False
    for j in range(i-1, -1, -1):
        if arr[j] > num1:
            found = True
            x.append(j+1)
            break
    if not found:
        x.append(-1)


y = []
for i, num1 in enumerate(arr):
    found = False
    for j in range(i+1, n):
        if arr[j] > num1:
            found = True
            y.append(j+1)
            break
    if not found:
        y.append(-1)

for n1, n2 in zip(x, y):
    print(n1+n2, end = ' ')

"""