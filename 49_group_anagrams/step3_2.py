from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            char_count = defaultdict(int)

            for char in word:
                char_count[char] += 1

            key = tuple(sorted(char_count.items()))
            result[key].append(word)

        return list(result.values())

