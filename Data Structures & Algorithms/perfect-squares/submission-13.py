import math

class Solution:
    def numSquares(self, n: int) -> int:
        sol = n
        if (n%math.sqrt(n)==0):
                return 1
        temp = n 
        memo = {}
        def bfs (num: int, curr: int):
            stack = []
            num = num - (curr*curr)
            if (num == 0):
                return 0
            if (num in memo):
                return memo[num]
            if (num%math.sqrt(num)==0):
                memo[num] = 1
                return 1
            temp = num
            for number in range(1, math.floor(math.sqrt(num))+1):
                stack.append(number)
            while (stack):
                temp = min(temp, 1+bfs(num, stack.pop()))
            memo[num] = temp
            return temp
        return bfs(n,0)