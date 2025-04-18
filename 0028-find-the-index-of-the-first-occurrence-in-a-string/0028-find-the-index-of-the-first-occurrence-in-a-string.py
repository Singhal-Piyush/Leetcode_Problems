class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pointer_1 = 0
        pointer_2 = len(needle)

        while pointer_1 <= len(haystack)-len(needle):
            if haystack[pointer_1: pointer_2] == needle:
                return pointer_1
            pointer_1 +=1
            pointer_2 +=1
        return -1