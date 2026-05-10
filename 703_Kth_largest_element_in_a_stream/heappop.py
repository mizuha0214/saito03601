from utility import sift_down

def heappop(heap: list):
    # firstとlastの交換
    heap[0], heap[-1], = heap[-1], heap[0]
    min_value = heap.pop()

    parent = 0
    size = len(heap)
    sift_down(heap, parent, size)

    return min_value

if __name__ == '__main__':
    target_heap = [1, 3, 10, 4, 12, 11, 20]
    for i in range(7):
        min_value = heappop(target_heap)
        print(min_value)

