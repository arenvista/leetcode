# @leet start
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #sort array
        str = sorted(strs)
        ans = ""
        #compare the two most different strings [0] and [-1]
        fs = str[0]
        ls = str[-1]
        #compare the two strings char by char
        LENGTH_MIN_STR = min(len(fs), len(ls))
        for i in range(LENGTH_MIN_STR):
            if fs[i] != ls[i]:
                return fs[:i] #stop when the two strings are different
            else:
                ans += fs[i]
        return ans #return the common prefix

# @leet end
