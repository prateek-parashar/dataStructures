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


def power_set_duplicate(arr):
    result = set()
    arr.sort()
    dup_power_set_helper(arr, 0, [] , result)
    answer = [list(x) for x in result]
    return answer


def dup_power_set_helper(arr, index, path, result):
    if index == len(arr):
        result.add(tuple(path))
    
    else:
        path.append(arr[index])
        dup_power_set_helper(arr, index + 1, path, result)
        path.pop()
        dup_power_set_helper(arr, index + 1, path, result)

arr = ['a', 'b', 'a']
a = power_set_duplicate(arr)
print(a)
