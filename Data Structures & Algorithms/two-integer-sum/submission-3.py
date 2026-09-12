class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for index, number in enumerate(nums):
            if number in check:
                return[check[number], index]
            else:
                check[target-number] = index
        return []