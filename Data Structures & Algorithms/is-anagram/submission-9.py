class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = 1
            else:
                first[s[i]] = first[s[i]] + 1
            if t[i] not in second:
                second[t[i]] = 1
            else:
                second[t[i]] = second[t[i]] + 1
        if (first == second):
            return True
        return False 
        