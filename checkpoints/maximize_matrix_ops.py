'''
Monk is fond of matrices. Today, he created a matrix A of size 
N
×
M
. He defines four types of operations on the matrix as follows:
	1.	Add v 1   to all elements of a row. 
	2.	Update the value of all elements of a row to v 2  , i.e., all elements of that row become equal to v 2  . 
	3.	Add v 3   to all elements of a column. 
	4.	Update the value of all elements of a column to v 4  , i.e., all elements of that column become equal to v 4  . 
He defines a function
 refers to absolute value of any integer x.
Now, he has defined some restrictions:
	1.	On any cell of the matrix, at most one operation can be performed. This operation can be of any type. 
	2.	Any type of operation can be used any number of times. 

# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import numpy as np

n, m = tuple(map(int, input().split()))
mat = np.zeros((n,m), dtype=int)

for i in range(n):
    mat[i] = list(map(int, input().split()))

v1, v2, v3, v4 = tuple(map(int, input().split()))

row_ops = 0
row_ans = 0

col_ops = 0
col_ans = 0

# check rows
for i in range(n):
    orig_sum = 0 
    row_sum1 = 0
    for num in mat[i]:
        row_sum1 += abs(num+v1)
        orig_sum += abs(num)

    row_sum2 = abs(v2)*m
    row_ans += max(orig_sum, row_sum1, row_sum2)

# check cols
for i in range(m):
    orig_sum = 0 
    col_sum1 = 0
    for num in mat[:,i]:
        col_sum1 += abs(num+v3)
        orig_sum += abs(num)

    col_sum2 = abs(v4)*n
    col_ans += max(orig_sum, col_sum1, col_sum2)

print(max(row_ans, col_ans))

