# @leet start
from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s = (sorted  ( list(Counter(s).values()) ) )
        t = (sorted ( list(Counter(t).values()) ) )
        print(s)
        print(t)
        return s == t
# @leet end
