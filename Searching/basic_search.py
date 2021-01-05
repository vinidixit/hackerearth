#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:48:05 2020

@author: vdixit
"""


arr = list(map(int, input().split()))  ## list IMP if to be REUSED
print(list(arr))
Q = int(input())
for _ in range(Q):
    p, x = map(int, input().split())
    cnt = 0
    print(arr)
    for num in arr:
        
        print("*****", (p == 0 and num >= x), (p ==1 and num > x))
        
        if (p == 0 and num >= x) or (p ==1 and num > x):
            cnt += 1
    print(cnt)