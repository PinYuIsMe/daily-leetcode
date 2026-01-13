class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        Ans = 0
        def markVisited(m: int, n: int) -> None:
            if m < 0 or m >= M or n < 0 or n >= N:
                return
            if grid[m][n] == "1":
                grid[m][n] = "0"
                markVisited(m-1, n)
                markVisited(m+1, n)
                markVisited(m, n-1)
                markVisited(m, n+1)
            return


        for m in range(M):
            for n in range(N):
                if grid[m][n] == "1":
                    markVisited(m, n)
                    Ans += 1

        return Ans
        