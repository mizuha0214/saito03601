def sift_down(nums: list[int], parent: int, size: int):
    while True:
        left = parent * 2 + 1
        right = parent * 2 + 2

        # 子がいない
        if left >= size:
            break

        # 小さい子を選ぶ
        child = left
        if right < size and nums[right] < nums[left]:
            child = right

        # すでに正しい位置
        if nums[parent] <= nums[child]:
            break

        # 親と子を交換
        nums[parent], nums[child] = nums[child], nums[parent]
        parent = child