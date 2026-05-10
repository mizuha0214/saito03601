from utility import sift_down

def heapify(nums: list[int]):
    # 下から順に、各親ごとにheapにする。
    last_parent = len(nums) // 2 - 1
    size = len(nums)

    for i in range(last_parent, -1, -1):
        sift_down(nums, i, size)


if __name__ == '__main__':
    target_list = [5, 3, 6, 10, 1, 11]
    heapify(target_list)
    print(target_list)
