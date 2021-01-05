'''
Monk has a matrix of size , and he wants to pick one element from each row to make a new array A of size N. He wants to find the minimum possible value of absolute difference between any two adjacent elements in the array A. Please note that the element picked from row 1, will become , element picked from row 2 will become , and so on.

# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import numpy as np
import sys

def search_nearest_pt(num, arr, arr_size):
    best_diff = sys.maxsize

    l, r = 0, arr_size-1

    while l <= r:
        m = l + (r-l)//2
        if arr[m] == num:
            return 0
        else:
            best_diff = min(best_diff, abs(arr[m]-num))
            
            if arr[m] > num:
                r = m-1
            else:
                l = m+1

    return best_diff

N, M = tuple(map(int, input().split()))
matrix = np.zeros((N,M), dtype=int)
for i in range(N):
    arr = list(map(int, input().split()))
    matrix[i] = sorted(arr)

min_diff = sys.maxsize
for r in range(N-1):
    for num in matrix[r]:
        min_diff = min(min_diff, search_nearest_pt(num, matrix[r+1], M))
        
print(min_diff)






