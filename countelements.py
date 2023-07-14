def count_elements_greater(array):
    size = len(array)
    max_value = -float('inf')
    for num in array:
        if num > max_value:
            max_value = num
    count = 0
    for num in array:
        if max_value == num:
            count += 1
    return size - count

array = list(map(int, input().split()))
print(count_elements_greater(array))
