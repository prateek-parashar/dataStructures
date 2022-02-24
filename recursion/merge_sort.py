from turtle import right


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid_point = len(arr) // 2

    left_sorted = merge_sort(arr[0 : mid_point])
    righ_sorted = merge_sort(arr[mid_point : ])
    return combined(left_sorted, righ_sorted)

def combined(left_sorted, right_sorted):
    result = []
    left_index = 0
    right_index = 0

    # Iterate over the 2 indexes to compare and append the smaller element to the result
    while left_index < len(left_sorted) and right_index < len(right_sorted):
        if left_sorted[left_index] < right_sorted[right_index]:
            result.append(left_sorted[left_index])
            left_index += 1
        else:
            result.append(right_sorted[right_index])
            right_index += 1
    
    # Append the remaining elements to the result
    result.extend(left_sorted[left_index : ])
    result.extend(right_sorted[right_index : ])

    return result



a = [3,6,8,23,345,1,1,3,4,5,78,5,34,0,45,-1,-334]

print(merge_sort(a))







