import random
import time

def merge_sort(a):
    if len(a)>1:
        mid = len(a)//2
        l = a[:mid]
        r = a[mid:]
        
        merge_sort(l)
        merge_sort(r)
        
        i = 0
        j = 0
        k = 0
        while i<len(l) and j < len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i += 1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1

k_min = 1
k_max = 1000
nums = 1000
a = []
start = time.process_time()
for i in range(nums):
    a.append(random.randint(k_min,k_max))
print(f"Time 1 : {time.process_time()-start}")

print(a[:20])

start = time.process_time()
a.sort()
print(f"Time 2 : {time.process_time()-start}")

print(a[:20])


