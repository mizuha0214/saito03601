from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} # {"abc": ["acb", "abc"]}

        for word in strs:
            # alphabet26文字のカウントをする
            char_count = defaultdict(int)

            for char in word:
                char_count[char] += 1

            key = tuple(sorted(char_count.items()))

            if key not in result:
                result[key] = []

            result[key].append(word)

        result_list = list(result.values())

        return result_list

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print("result:", result)

