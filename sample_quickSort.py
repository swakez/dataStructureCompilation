import random


def partition(sort_list, low, high):
    i = (low -1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1], sort_list[high] = sort_list[high], sort_list[i+1]
    return i+1


def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi-1)
        quick_sort(sort_list, pi+1, high)


k_min = 1
k_max = 50
nums = 100
lst = []
for i in range(nums):
    lst.append(random.randint(k_min, k_max))
low = 0
high = len(lst) - 1
quick_sort(lst, low, high)
print(lst)
