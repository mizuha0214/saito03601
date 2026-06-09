from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = defaultdict(int)
        for char in s:
            char_count[char] += 1

        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index

        return -1
