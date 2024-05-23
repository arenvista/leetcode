# @leet start
class Solution:
    def reverse(self, x: int) -> int:
        sign: int = [1, -1][x < 0]
        x: int = abs(x)
        rev: int = 0 # Placeholder for reversed number
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1: 
                return 0 
        return sign * rev


      # @leet end
