class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for index, num in enumerate(nums):
            right = len(nums)-1
            left = index + 1
            target = 0-num
            if (index>=1 and num == nums[index-1]):
                continue
            while (left<right):
                if (nums[left] + nums[right] == target):
                    if ([num, nums[left], nums[right]] not in solution):
                        solution.append([num, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    continue
                # -1 -1 0 1
                # -1<1
                if (nums[left]+nums[right]>target):
                    right -= 1
                    continue
                elif (nums[left]+nums[right]<target):
                    left+=1
                    continue 
                else:
                    break
        return solution