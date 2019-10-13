def bin_search(l, low, high, target):
    ss = hh = -1
    if low < high:
        mid = (low + high) // 2
        if target < l[mid]:
            bin_search(l, low, mid - 1, target)
        elif target > l[mid]:
            bin_search(l, mid + 1, high, target)
        else:
            ss = hh = mid
            t1 = bin_search(l, low, mid - 1, target)
            t2 = bin_search(l, mid + 1, high, target)
            if t1 != -1:
                ss = t1
            if t2 != -1:
                hh = t2
        print("{0}   {1}".format(ss, hh))
        return mid
    else:
        return -1


print(bin_search([5, 7, 7, 8, 8, 10], 0, 6, 8))
