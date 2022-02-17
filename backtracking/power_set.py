def power_set(arr):
    result = []
    power_set_helper(arr, 0, [], result)
    return result


def power_set_helper(arr, index, path, result):
    if index == len(arr):
        result.append(list(path))
    
    else:
        path.append(arr[index])
        power_set_helper(arr, index + 1, path, result)
        path.pop()
        power_set_helper(arr, index + 1, path, result)


arr = ['a', 'b', 'c']
a = power_set(arr)
print(a)
