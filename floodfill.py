from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc:int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image 
        n, m = len(image), len(image[0])

        def fillColor(i, j, target):
            image[i][j] = color 
            adjacent = [(i+1, j), (j-1, j), (i, j+1), (i, j-1)]
            for ni, nj in adjacent:
                if -1 < ni < n and -1 < nj < m and image[ni][nj] == target:
                    fillColor(ni, nj, target)
        
        fillColor(sr, sc, image[sr][sc])
        return image
  
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2 
ob1 = Solution()
print(ob1.floodFill(image, sr, sc, color))