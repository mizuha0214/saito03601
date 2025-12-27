class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['{', '(', '[']
        close_brackets = ['}', ')', ']']
        bracket_pair = [('(', ')'), ('{', '}'), ('[', ']')]
        stack_list = []

        for char in s:
            if char in open_brackets:
                stack_list.append(char)
            if char in close_brackets:
                if not stack_list:
                    return False
                last_bracket = stack_list.pop()
                if (last_bracket, char) not in bracket_pair:
                    return False

        if stack_list:
            return False

        return True


