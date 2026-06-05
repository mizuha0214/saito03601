from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 存在しないキーaにアクセスしたら、list()つまり[]が入る。
        anagram_groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            anagram_groups[key].append(word)

        return list(anagram_groups.values())

