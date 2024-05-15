# @leet start
def roman_to_int(c:str) -> int:
    if c == 'I':
        return 1
    elif c == 'V':
        return 5
    elif c == 'X':
        return 10
    elif c == 'L':
        return 50
    elif c == 'C':
        return 100
    elif c == 'D':
        return 500
    elif c == 'M':
        return 1000
    else:
        return 0

def solution(x: int, romans: str, total:int): 
     #Find L[x] L[x+1]
    next_term = 0
    current_term = roman_to_int(romans[x])
    if x < len(romans)-1:
        next_term = roman_to_int(romans[x+1])
     # If L[x+1] > L[x]
    if next_term > current_term:
        total += next_term - current_term
        x += 2
    else: #Elif L[x+1] =< L[x]
        # Return L[x]; update pointer x+1
        total += current_term
        x += 1
    if x < len(romans): #Recurse until at the end
    return total

# @leet end
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        total = solution(0, s, total)
        if total != None:
            total: int = total
        else: 
            raise Exception("Error")
        return total

# @leet end
