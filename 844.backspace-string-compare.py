# @leet start
from collections import deque
class Solution:
    def parse(self, s: str) -> str:
        stack = deque()
        for c in s:
            if c == "#":
                stack.pop() if stack else None
            else:
                stack.append(c)
        return "".join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.parse(s) == self.parse(t)
# @leet end
