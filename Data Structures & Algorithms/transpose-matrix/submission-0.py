class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        sol = []
        for num in range(len(matrix[0])):

            temp = []
            for row in range(len(matrix)):
                temp.append(matrix[row][num])

            sol.append(temp)
        return sol