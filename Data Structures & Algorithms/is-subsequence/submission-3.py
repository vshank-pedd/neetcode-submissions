class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = 0
        length = len(s)
        if (s == ""):
            return True
        if (len(t)<len(s)):
            return False
        for char in t:
            if (char == s[curr]):
                curr = curr+1
            if (curr == length):
                return True
        return False
        