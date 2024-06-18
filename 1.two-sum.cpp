#include <vector>
using namespace std;
class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        vector<int> res;
        int slow = 0;
        int fast = 1;

        while (slow < fast && slow < nums.size()-1){
            if (nums[fast] + nums[slow] == target)
            {
                res.push_back(slow);
                res.push_back(fast);
                return res;
            }
            if (fast >= nums.size()-1){
                slow++;
                fast = slow+1;
            } else if (fast < nums.size()-1) {
                fast++;
            }
        }
        return res;
    }
};
