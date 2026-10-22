class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        number = n*n
        curr = 1
        prev = "r"
        coord = [0,0]
        n
        def fill(cord: List[int], prev: str):
            nonlocal curr
            grid[cord[0]][cord[1]] = curr
            if (number == curr):
                return True
            curr = curr +1
            if (prev == "r"):
                if ((cord[1] + 1 == n)or(grid[cord[0]][cord[1]+1]!=0)):
                    new_cord = cord
                    new_cord[0] = new_cord[0] + 1
                    fill(new_cord, "d")
                else:
                    cord[1] = cord[1]+1
                    fill(cord,"r")
            if (prev == "d"):
                if ((cord[0] + 1 == n)or (grid[cord[0]+1][cord[1]]!=0)):
                    new_cord = cord
                    new_cord[1] = new_cord[1]-1
                    fill(new_cord, "l")
                else:
                    cord[0] = cord[0]+1
                    fill(cord,"d")
            if (prev == "l"):
                if ((cord[1] - 1<0)or(grid[cord[0]][cord[1]-1]!=0)):
                    new_cord = cord
                    new_cord[0] = new_cord[0]-1
                    fill(new_cord, "u")
                else:
                    cord[1] = cord[1]-1
                    fill(cord,"l")
            if (prev == "u"):
                if ((cord[0] - 1<0) or (grid[cord[0]-1][cord[1]] != 0)):
                    new_cord = cord
                    new_cord[1] = new_cord[1]+1
                    fill(new_cord, "r")
                else:
                    cord[0] = cord[0]-1
                    fill(cord,"u")
        fill(coord,"r")
        return grid