class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)-1
        for index, num in enumerate(nums):
            nums.append(num)
            if (length == index):
                return nums
        return nums