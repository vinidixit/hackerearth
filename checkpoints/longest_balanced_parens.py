'''
# Sample code to perform I/O:

Initially , we push 0 in the stack. This acts as a marker for identifying subarrays.
When we encounter a positive element, we simply push it's index into the stack.
On encountering a negative element, we pop an element from stack:
If the value at popped index is equal to positive value of current element and stack is not empty, we know that the subarray length is (current index- top of stack). But if stack is empty, we push the current element's index as our new marker in the stack. At each step, we maintain the maximum length of subarray.
If the values are not equal, then we don't have a positive number which is there to balance this negative number, so we push the current element's index as our new marker in the stack.

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N = int(input())
arr = list(map(int, input().split()))

st = list()
longest_len = 0

st.append(0)

for i in range(1, N):
    if arr[i] > 0:
        st.append(i)
    else:
        if not st:
            st.append(i)
        else:
            pop_el = arr[st.pop()]
            if pop_el == abs(arr[i]):
                seq_len = i-st[-1] if st else i+1
                longest_len = max(longest_len, seq_len)
            
            elif pop_el != abs(arr[i]) or not st:
                st.append(i)
            
print(longest_len)


"""
for num in arr:
    if num > 0:
        st.append(num)
    else:
        if not st:
            continue

        prev_seq = 0
        while st and type(st[-1]) == tuple:
            prev_seq += st.pop()[0]
            longest_len = max(longest_len, prev_seq)
        
        if not st:
            continue

        if st[-1] == abs(num):
            st.pop()
            prev_seq += 2
            while st and type(st[-1]) == tuple:
                prev_seq += st.pop()[0]
                
            st.append((prev_seq,))
            longest_len = max(longest_len, prev_seq)
        else:
            st.clear()
            prev_seq = 0

print(longest_len)
"""
