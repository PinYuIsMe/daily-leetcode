from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        minute = 0
        fresh = False
        
        queue = deque()

        # push first batch of rotten orange into queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 2
                elif grid[i][j] == 2:
                    queue.append((i, j))
                else:
                    fresh = True

        print(f"queue: {queue}")

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # rotting
        while queue and fresh:
            print(f"minute: {minute}")

            batch_size = len(queue)
            impacted = False
            for _ in range(batch_size):
                curr_i, curr_j = queue.popleft()
                for d_i, d_j in directions:
                    target_i = curr_i + d_i
                    target_j = curr_j + d_j
                    if not(0 <= target_i < m) or not(0 <= target_j < n):
                        continue
                    if grid[target_i][target_j] == 1:
                       grid[target_i][target_j] = 2
                       queue.append((target_i, target_j))
                       impacted = True
            if impacted:
                minute += 1

        total_value = sum(sum(v) for v in grid)

        print(f"Final: {grid}")

        if total_value != 2 * m * n:
            return -1
        else:
            return minute

        