class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        tempArea = 0
        while left < right:
            if heights[left] < heights[right]:
                tempArea = heights[left] * (right - left)
            else:
                tempArea = heights[right] * (right - left)
            if tempArea > maxArea:
                maxArea = tempArea
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea