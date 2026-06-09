from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_to_count = defaultdict(int)
        for character in s:
            character_to_count[character] += 1

        for index, character in enumerate(s):
            if character_to_count[character] == 1:
                return index

        return -1
