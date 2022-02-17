def print_binary(number_length):
    result = []
    get_binary_helper(number_length, [], result)
    return result

def get_binary_helper(length, path, result):
    if length == 0:
        result.append(list(path))
        
    else:
        for i in range(2):
            path.append(i)
            get_binary_helper(length - 1, path, result)
            path.pop()


x = print_binary(4)
print(x)
