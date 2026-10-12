class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        root_color = image[sr][sc]
        if root_color == color:
            return image
        queue = deque()
        queue.append((sr,sc))
        m = len(image)       # number of rows
        n = len(image[0])    # number of columns
        # 2x1
        while queue:
            x, y = queue.popleft()
            if (image[x][y] == root_color):
                image[x][y] = color
            else:
                continue
            left = (x-1,y)
            right = (x+1,y)
            up = (x,y+1)
            down = (x,y-1)
            if (x-1>=0):
                queue.append(left)
            if (y-1>=0):
                queue.append(down)
            if x + 1 < m:
                queue.append(right)
            if y + 1 < n:
                queue.append(up)
        return image
