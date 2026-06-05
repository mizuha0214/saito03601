from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for word in strs:
            sorted_list = sorted(word)
            sorted_str = "".join(sorted_list)

            if sorted_str in result_dict:
                result_dict[sorted_str].append(word)
            else:
                result_dict[sorted_str] = [word]

        return list(result_dict.values())


