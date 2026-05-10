def heappush(heap: list[int], num: int):
    # リストの最後にくっつける
    heap.append(num)

    child = len(heap) - 1

    while child > 0:
        parent = (child - 1)//2

        if heap[parent] <= heap[child]:
            break

        heap[child], heap[parent] = heap[parent], heap[child]
        child = parent

    return heap

if __name__ == '__main__':
    target_heap = [1, 3, 10, 4, 12, 11, 20]
    result = heappush(target_heap, 1)
    print(result)

