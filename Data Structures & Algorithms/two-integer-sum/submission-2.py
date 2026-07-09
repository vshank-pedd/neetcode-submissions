class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            if (check.get(target-num) == None):
                check[num] = i
            else:
                return [check.get(target-num),i]
        return [0,0]