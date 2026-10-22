class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sol = ""
        length = len(strs[0])
        shortest = strs[0]
        for word in strs:
            if (len(word)<length):
                shortest = word
                length = len(word)
        
        for i in range(length):
            letter = shortest[i]
            for words in strs:
                if (letter != words[i]):
                    return sol
            sol = sol + letter
        return sol

