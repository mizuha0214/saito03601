class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        unclosed_opens = []

        for ch in s:
            if ch in open_to_close.keys():
                unclosed_opens.append(ch)
                continue

            if not unclosed_opens:
                return False

            expected_close = open_to_close[unclosed_opens[-1]]
            if ch != expected_close:
                return False

            unclosed_opens.pop()

        if unclosed_opens:
            return False

        return True
