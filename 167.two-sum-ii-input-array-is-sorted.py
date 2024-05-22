# @leet start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a_p: int = 0
        b_p: int = len(numbers)-1

        while (a_p <= b_p):
            print(a_p, b_p)
            sum = numbers[a_p] + numbers[b_p]
            if (sum > target):
                b_p -= 1
            elif sum < target:
                a_p += 1

            else:
                return [a_p+1, b_p+1]
            
        return [a_p+1, b_p+1]
                
        
# @leet end
