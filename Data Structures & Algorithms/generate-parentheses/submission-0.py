class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = n
        right = n
        seen = set()
        sol = []
        def isValid(parenthesis: str,)->bool:
            stack = []
            match = {"(":")"}
            for character in parenthesis:
                if (character == "("):
                    stack.append(character)
                else:
                    if (not stack): return False
                    stack.pop()
                
            if (not stack):
                return True
            return False
        def recursion(test: str, left: int, right: int):
            queue = deque()
            print(test)
            if (isValid(test) and test not in seen and left == 0 and right == 0):
                seen.add(test)
                sol.append(test)
                return True
            if (left == 0 and right == 0 and test not in seen):
                seen.add(test)
                return False
            if (left>0):
                recursion(test + "(", left - 1, right)
            if (right>0):
                recursion(test + ")", left, right - 1)
        recursion("",n,n)
        return sol

