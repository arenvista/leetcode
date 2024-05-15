# @leet start
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #filter out non-alphanumeric characters
        s = ''.join(e for e in s if e.isalnum()).lower()
        #check odd or even
        is_even: bool = (len(s) % 2 == 0)
        mid: int = len(s) // 2
        if is_even:
            print(s[:mid], "".join(reversed(s[mid:])))
            return s[:mid] == "".join(reversed(s[mid:]))
        else:
            print (s[:mid], "".join(reversed(s[mid+1:])))
            return s[:mid] == "".join(reversed(s[mid+1:]))
# @leet end
