"""This is disgusting!!!!!!"""
from unittest import result


def combination_naive(arr):
    result = []
    size = len(arr)
    for i in range(size):
        result.append(arr[i])
        for j in range(i + 1, size):
            result.append([arr[i], arr[j]])
    result.append(arr)
    result.append([])

    return result

def combination(arr):
    if len(arr) == 0:
        return [[]]
    else:
        first_element = arr[0]
        combination_remaining = combination(arr[1:])
        copy = [x[:] for x in combination_remaining]
        result = []

        for i in combination_remaining:
            i.append(first_element)
            result.append(i)

        for i in copy:
            result.append(i)
        
        return result

        
        

print(combination(['a', 'b', 'c']))







