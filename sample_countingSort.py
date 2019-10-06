import time,random


def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m
    sorted = [0] * len(array1)
    for a in array1:
        count[a] += 1
    print(array1)
    print(sorted)
    print(count)

    for i in range(1,len(count)):
        count[i] += count[i-1]
    print(count)

    for a in range(len(array1)-1,-1,-1):
        sorted[count[array1[a]]-1] = array1[a]
        count[array1[a]] -= 1
    return sorted


k_min = 1
k_max = 50
nums = 100
a = []
start = time.process_time()
for i in range(nums):
    a.append(random.randint(k_min,k_max))
print(f"Time 1 : {time.process_time()-start}")

start = time.process_time()
print(counting_sort(a, k_max))
print(f"Time 2 : {time.process_time()-start}")
