class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close_pair = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        stack = []

        for ch in s:
            if ch in open_to_close_pair.keys():
                stack.append(ch)
                continue

            if not stack:
                return False

            expected_close = open_to_close_pair[stack[-1]]
            if ch != expected_close:
                return False

            stack.pop()

        if stack:
            return False

        return True