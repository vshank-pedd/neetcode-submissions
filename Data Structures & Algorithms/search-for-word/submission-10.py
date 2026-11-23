class Solution:
    def exist(self, board, word):
        vert = len(board) - 1
        hor = len(board[0]) - 1
        seen = set()
        length = len(word) - 1

        def dfs(cord, index):
            r, l = cord
            if r != 0:
                up = (r-1, l)
                if up not in seen and board[up[0]][up[1]] == word[index]:
                    seen.add(up)
                    if length == index or dfs(up, index+1):
                        return True
                    seen.remove(up)
            if r != vert:
                down = (r+1, l)
                if down not in seen and board[down[0]][down[1]] == word[index]:
                    seen.add(down)
                    if length == index or dfs(down, index+1):
                        return True
                    seen.remove(down)
            if l != 0:
                left = (r, l-1)
                if left not in seen and board[left[0]][left[1]] == word[index]:
                    seen.add(left)
                    if length == index or dfs(left, index+1):
                        return True
                    seen.remove(left)
            if l != hor:
                right = (r, l+1)
                if right not in seen and board[right[0]][right[1]] == word[index]:
                    seen.add(right)
                    if length == index or dfs(right, index+1):
                        return True
                    seen.remove(right)
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if length == 0:
                        return True
                    seen.add((r, c))
                    if dfs((r, c), 1):
                        return True
                    seen.remove((r, c))
        return False