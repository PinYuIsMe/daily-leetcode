class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = ['(', '{', '[']
        close_bracket = [')', '}', ']']
        stack = []
        for c in s:
            if c in open_bracket:
                stack.append(c)
            elif c in close_bracket:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                top_idx = open_bracket.index(top)
                c_idx = close_bracket.index(c)
                if top_idx != c_idx or len(stack) == 0:
                    return False
                stack.pop()

        if len(stack) != 0:
            return False
        else:
            return True