# @leet start
from collections import deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        s_pointer: int = 0
        t_pointer: int = 0

        while (t_pointer < len(t)):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
                if s_pointer == len(s):
                    return True
            t_pointer += 1
            
        return False
# @leet end
