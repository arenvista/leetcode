# @leet start
def opp(c):
    if c == '}':
        return '{'
    elif c == ']':
        return '['
    elif c == ')':
        return '('
    return None

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False
        stack = [s[0]]
        for c in s[1:]:
            if c in ['{', '[', '(']:
                stack.append(c)
            elif c in ['}', ']', ')']:
                if len(stack) == 0 or stack[-1] != opp(c):
                    return False
                if stack[-1] == opp(c):
                    stack.pop()
        return len(stack) == 0
                
# @leet end
