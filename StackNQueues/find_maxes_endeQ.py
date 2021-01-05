#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:06:58 2020

@author: vdixit
"""


'''
Aragog shows them a queue of N spiders of which only X spiders are to be selected. Each spider has some power associated with it. There are X iterations on the queue.
In each iteration, X spiders are dequeued (if queue has less than X entries, all of them will be dequeued) and the one with maximum power is selected and remaining spiders are enqueued back to the queue (in the order they were dequeued) but their power is decreased by one unit. If there are multiple spiders with maximum power in those dequeued spiders, the one which comes first in the queue is selected. If at any moment , power of any spider becomes 0, it can't be decremented any further, it remains the same.
Now, Aragog asks the boys to tell him the positions of all the selected spiders (positions in the initial given queue) in the order they are selected'''

# Write your code here
from collections import deque 

N, X = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

enque = deque([(i+1, num) for i, num in enumerate(arr)])
dequed = deque()

for _ in range(X):
    max_num = None
    for _ in range(X):
        if len(enque) == 0:
            break
        num = enque.popleft()
        if max_num == None or max_num[1] < num[1]:
            max_num = num
        
        dequed.append(num)
    
    while len(dequed) > 0:
        num = dequed.popleft()
        if num != max_num:
            enque.append((num[0], max(0, num[1]-1)))

    print(max_num[0], end=' ')    

