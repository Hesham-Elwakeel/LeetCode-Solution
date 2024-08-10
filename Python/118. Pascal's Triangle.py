Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

                 1
               1   1
             1   2   1
           1   3   3   1
         1   4   6   4   1
       1   5  10   10  5   1
     1   6  15  20   15  6   1
   1   7  21  35   35  21  7   1
 1   8  28  56  70   56   28  8   1


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

class Solution:
    def generate(self, numRows):
        triangles = []
        for i in range(numRows):
            triangles.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    triangles[i].append(1)
                else:
                    triangles[i].append(triangles[i - 1][j - 1] + triangles[i - 1][j])
        return triangles
