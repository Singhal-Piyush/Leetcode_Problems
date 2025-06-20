class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        start = 0
        end = 0
        substring = ''
        count = 0

        while end < len(s):
            substring += s[end]
            if end-start+1 == 3:
                substring_set = set(substring)
                if len(substring_set) == 3:
                    count +=1
                substring = substring[1:3]
                start+=1
            if end-start+1 <= 3:
                end += 1
        return count
        