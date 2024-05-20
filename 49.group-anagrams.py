# @leet start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            print(ans)
            ans[tuple(sorted(s))].append(s)
# @leet end
