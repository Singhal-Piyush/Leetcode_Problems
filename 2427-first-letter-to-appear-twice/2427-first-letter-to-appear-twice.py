class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict_s = {}
        for i in s:
            if i in dict_s.keys():
                return i
            else:
                dict_s[i]=1
        