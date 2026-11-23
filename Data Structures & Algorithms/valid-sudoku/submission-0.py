class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for row in board:
            seen  = set()
            for val in row:
                if (val in seen):
                    return False
                if (val != "."):
                    seen.add(val)
        #cols
        for col in range(9):
            seen = set()
            for row in range (9):
                val = board[row][col]
                if (val in seen):
                    return False
                if (val != "."):
                    seen.add(val)
        sets = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                index =  (row//3)*3+(col//3)
                val  = board[row][col]
                if (val in sets[index]):
                    return False
                if (val != "."):
                    sets[index].add(val)
    

        return True
