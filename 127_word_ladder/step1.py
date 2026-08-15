from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_one_diff(target: str, hikaku: str):
            diff = 0
            for i in range(len(target)):
                if target[i] != hikaku[i]:
                    diff += 1

            return diff == 1

        if endWord not in wordList:
            return 0

        queue = deque([beginWord])
        visited = set([beginWord])
        count = 1

        while queue:
            queue_size = len(queue)

            for _ in range(queue_size):
                target = queue.popleft()

                if target == endWord:
                    return count

                for word in wordList:
                    if word not in visited and is_one_diff(target, word) == True:
                        visited.add(word)
                        queue.append(word)
            count += 1

        return 0
