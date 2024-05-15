from collections import Counter
# @leet start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteC = Counter(ransomNote)
        magazineC = Counter(magazine)
        return (ransomNoteC - magazineC == {})
# @leet end
