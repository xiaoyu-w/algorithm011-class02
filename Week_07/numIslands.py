class Solution:
    def getIndex(self, i, j):
        return i*self.n+j

    def numIslands(self, grid: List[List[str]]) -> int: 
        """
        岛屿数量
        """
        if grid == [] or grid == [[]]:
            return 0
        self.m, self.n = len(grid), len(grid[0])
        num = self.m * self.n
        uf = UnionFind(num+1)
        directions = [[0, 1], [1, 0]]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '0':
                    uf.union(self.getIndex(i,j), num)
                    continue
                for d in directions:
                    new_i, new_j = i + d[0], j + d[1]
                    if new_i < self.m and new_j < self.n:
                        if grid[new_i][new_j] == '1':
                            uf.union(self.getIndex(i, j), self.getIndex(new_i, new_j))

        return uf.getNum()-1


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.total = n

    def find(self, index):
        if(self.parent[index] != index):
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def isConnected(self, i, j):
        return self.find(i) == self.find(j)

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id != j_id:
            self.parent[i_id] = j_id

    def getNum(self):
        res = 0
        for index, parent in enumerate(self.parent):
            if parent == index:
                res += 1
        return res