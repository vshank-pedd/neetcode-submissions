class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for i,string in enumerate(strs):
            strs[i] = "".join(sorted(string))
            if strs[i] not in check:
                check[strs[i]] = [string]
            else:
                check[strs[i]].append(string)
        
        return list(check.values())