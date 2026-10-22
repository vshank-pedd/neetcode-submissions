class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        for character in s:
            if (l>=r):
                break
            s[l] = s[r]
            s[r] = character
            l = l+1
            r -= 1
        