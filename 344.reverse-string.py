# @leet start
class Solution:
    from collections import deque
    def reverseString(self, s: List[str]) -> None:
        stack = deque(s)
        while stack:
            s.append(stack.pop())
            s.pop(0)
        return s
# @leet end
