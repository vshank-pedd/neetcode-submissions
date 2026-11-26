class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = []
        for num in temperatures:
            sol.append(0)
        for i,val in enumerate(temperatures):
            if (stack):
                while (stack):
                    idx = stack[-1]
                    if (val>temperatures[idx]):
                        stack.pop()
                        sol[idx] = i-idx
                    else:
                    
                        break
                stack.append(i)
            else:
                stack.append(i)
        return sol

            