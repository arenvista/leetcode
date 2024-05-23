# @leet start
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False for _ in rooms]
        seen[0] = True

        keys = deque(rooms[0])
        while keys:
            key = keys.popleft()
            if not seen[key]:
                seen[key] = True
                for k in rooms[key]:
                    keys.append(k)

        return not False in seen
        
# @leet end
