class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        first_char = word[0]
        rows, cols = len(board), len(board[0])
        seen = set()
        listy = []
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == first_char:
                    listy.append((row, col))
        if not listy:
            return False

        def bfs(coord: tuple, index: int) -> bool:
            r, c = coord
            if board[r][c] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            seen.add(coord)
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                    if bfs((nr, nc), index + 1):
                        return True
            seen.remove(coord)
            return False

        for coords in listy:
            if bfs(coords, 0):
                return True
        return False