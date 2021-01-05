#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:44:36 2020

@author: vdixit
"""


def get_subsets(arr, level,out, n, cur_prod, cur_ind, subset_prods):
    if level >= n:
        return 
    
    for i in range(cur_ind, n):
        out[level] = arr[i]
        level_prod = cur_prod*arr[i]
        subset_prods.add(cur_prod*arr[i])
        
        print(out[:level+1])
        print('i:%d, level: %d, num: %d, cur_prod: %d, level_prod:%d\n' %(
              i, level, arr[i], cur_prod, level_prod))
        
        get_subsets(arr, level+1,out, n, level_prod, i+1, subset_prods)
        
            

arr = [2,3,3,3]
subset_sum = [1]
out = [0, 0, 0, 0]

subset_prods = set([1])
get_subsets(arr, 0,out, 4, 1, 0, subset_prods)

print(subset_prods)
print(sum(subset_prods))