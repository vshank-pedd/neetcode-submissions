class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        left = 0
        right = 1
        for i in range(len(prices)-1):
            sol = max(sol, prices[right]-prices[left])
            if (prices[right]<prices[left]):
                left = right
                right += 1
                continue
            right = right + 1
        return sol
