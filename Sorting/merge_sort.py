#t(arr, 0, len(arr)-1)

def merge_sort(arr, l, r):
    if l >= r:
        return 
    m = l + (r-l)//2 ## int division in python 3
    print(l, m, r)
    merge_sort(arr,l, m)
    merge_sort(arr,m+1, r)
    merge(arr, l, m, r)

def merge(arr, l, m, r):
    tmp = []
    l1, r1, l2, r2 = l, m, m+1, r
    while l1 <= r1 and l2 <= r2:
        if arr[l1]%k <= arr[l2]%k:
            tmp.append(arr[l1])
            l1 += 1
        else:
            tmp.append(arr[l2])
            l2 += 1
    
    while l1 <= r1:
        tmp.append(arr[l1])
        l1 += 1

    while l2 <= r2:
        tmp.append(arr[l2])
        l2 += 1
    
    t = 0
    for i in range(l, r+1):
        arr[i] = tmp[t]
        t += 1

arr = [12, 18, 17, 65, 46]
k = 6
#arr = [5,2,4,1,6,4,9]
print(arr,'\n')
merge_sort(arr, 0, len(arr)-1)
print('\n',arr)
