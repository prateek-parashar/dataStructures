import heapq


def kth_smallest(arr, k):
    min_heap = []
    for i in arr:
        heapq.heappush(min_heap, i)

    return min_heap[k - 1]
