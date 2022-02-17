def permutations(arr):
    if len(arr) == 0:
        return [[]]
    else:
        result = []
        copyA = []
        first_element = arr.pop(0)
        permutation_rest = permutations(arr)

        for i in permutation_rest:
            for j in range(len(i) + 1):
                copyA = i[:]
                copyA.insert(j, first_element)
                result.append(copyA)
        return result