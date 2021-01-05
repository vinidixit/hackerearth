#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:02:27 2020

@author: vdixit
"""
"""
Special integer, K, of an array, is an integer such that none of its subarray of size K has 
sum of elements greater than X. To calm the array down, Monk decided to gift it the maximum 
possible value of special integer K. Now since Monk is busy with Code Monk he asked Micro to 
find the maximum value of special integer but right now, all Micro can think of is a Potato, 
so Micro asked for your help.
"""


# Write your code here
N, X = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, N
ans = 0

while l <= r:
    m = l + (r-l)//2
    S = 0
    
    for i in range(m):
        S += arr[i]
    
    for i in range(m, N):
        S = S + arr[i] - arr[i-m]
        if S > X:
            break
    
    if S <= X:
        ans = m
        l = m+1
    else:
        r = m-1

print(ans)    