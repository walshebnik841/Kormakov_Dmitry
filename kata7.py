def find_missing_numbers(arr):
    if not arr:
        return[]
    m = []
    for i in range(arr[0], arr[-1]+1):
        if i not in arr:
            m.append(i)
    return m
print(find_missing_numbers([-3,-2,1,5]))
