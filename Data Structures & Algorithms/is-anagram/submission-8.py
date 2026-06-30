class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        second_check = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in check:
                check[s[i]] = 1
            elif s[i] in check:
                check[s[i]] = check[s[i]] + 1
            if t[i] in second_check:
                second_check[t[i]] = second_check[t[i]] + 1
            elif t[i] not in second_check:
                second_check[t[i]] = 1
        if check == second_check:
            return True
        print (check, second_check)
        return False
        