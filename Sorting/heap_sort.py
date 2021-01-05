from heapq import heappop, heappush, _heapify_max, heapify
import heapq
line = 'aacb 3'
s, K = line.split()[0], int(line.split()[1])

heap = [] 
_heapify_max(heap)

cur_s = s
for _ in range(K):
    if not cur_s:
        break
    heappush(heap, cur_s)
    #heap.append(cur_s)
    cur_s = cur_s[1:]

#_heapify_max(heap) # max heap

print(cur_s)

while cur_s:
    if cur_s < heap[0]:
        print(cur_s, heap[0])
        el = heapq._heappop_max(heap)
        print('removed:', el, '\n')
        heapq.heappush(heap, cur_s)
    cur_s = cur_s[1:]

_heapify_max(heap) 
print(heap)


heap = [] 
_heapify_max(heap) 
  
# Adding items to the heap using heappush 
# function by multiplying them with -1 
heappush(heap, 10) 
heappush(heap, 30) 
heappush(heap, 20) 
heappush(heap, 400)
heapq._heapify_max(heap)

print(heap) 

