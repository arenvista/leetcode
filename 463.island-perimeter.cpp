// @leet start
#include <vector>
class Solution {
public:
    int islandPerimeter(std::vector<std::vector<int>>& grid) 
    {
        int rows = grid.size();
        int cols = grid[0].size();
        int perimeter = 0;

        for (int r = 0; r < rows; r++) 
        {
            for (int c = 0; c < cols; c++) 
            {
                if (grid[r][c] == 1)
                {
                    int up, down, left, right = 0;
                    if(r == 0){ //@ first row
                        up = 0;
                    }
                    else{
                        up = grid[r-1][c];
                    }

                    if (r == rows-1) //@ last row
                    {
                        down = 0;
                    }
                    else
                    {
                        down = grid[r+1][c];
                    }

                    if (c == 0) //@first col
                    {
                        left = 0;
                    }
                    else
                    {
                        left = grid[r][c-1]; //@ left
                    }

                    if (c == cols-1) //@ last col
                    {
                        right = 0;
                    }
                    else
                    {
                        right = grid[r][c+1]; //@ right
                    }


                    perimeter += 4 - (up + down + left + right);
                }
            }
        } 

        return perimeter;
    }

};
// @leet end
