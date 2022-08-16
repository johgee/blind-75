# MEDIUM

# given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# the distance between two adjacent cells is 1. 

# input: mat = [[0,0,0], [0,1,0], [0,0,0]]
# output: [[0,0,0], [0,1,0], [0,0,0]]

# input: mat = [[0,0,0], [0,1,0], [1,1,1]]
# output: [[0,0,0], [0,1,0], [1,2,1]]

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0,1,0,-1,0]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1 # marked as not processed yet 
        
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue 
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat 

mat = [[0,0,0], [0,1,0], [0,0,0]]
ob1 = Solution()
print(ob1.updateMatrix(mat))