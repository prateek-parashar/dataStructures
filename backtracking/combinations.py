
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







