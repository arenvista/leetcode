// @leet start

#include <cmath>
#include <iostream>
class Solution {
public:
    int reverse(int x) {
        long reversed = 0;
        int pop;
        while (x != 0){
            pop = x % 10;
            x /= 10;
            reversed = (reversed*10)+pop;
            if (reversed < (pow(2,31)*-1) || reversed > pow(2,31))
            {
                return 0;
            }
        }
        return reversed;
    }
};
// @leet end
