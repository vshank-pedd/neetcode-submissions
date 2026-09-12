class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        left = 0
        right = len(num)-1
        while (right>left):
            if(num[left] != num[right]):
                return False
            left += 1
            right -= 1
        return True
        