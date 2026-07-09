class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for num in nums:
            if check.get(num) == None:
                check [num] = num
            else:
                return True
        return False