from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0

        def isValid(coords: tuple) -> bool:
            r, c = coords
            return 0 <= r < len(grid) and 0 <= c < len(grid[r])

        def bfs(start):
            queue = deque()
            seen = set()
            queue.append(start)
            while (queue):
                curr = queue.popleft()
                up = (curr[0]-1,curr[1])
                down = (curr[0]+1, curr[1])
                right = (curr[0],curr[1]+1)
                left = (curr[0], curr[1]-1)
                if (grid[curr[0]][curr[1]]=="1"):
                    grid[curr[0]][curr[1]] = "0"
                    if (isValid(up) and up not in seen):
                        queue.append(up)
                    if (isValid(down) and down not in seen):
                        queue.append(down)
                    if (isValid(right) and right not in seen):
                        queue.append(right)
                    if (isValid(left) and left not in seen):
                        queue.append(left)
                seen.add(curr)
            return 1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    total += bfs((r, c))

        return total