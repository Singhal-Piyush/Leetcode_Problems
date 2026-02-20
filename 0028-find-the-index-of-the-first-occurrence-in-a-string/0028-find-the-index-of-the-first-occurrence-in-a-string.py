class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) >= len(needle):

            left = 0
            right = 0

            while (left < len(haystack)) & (right<len(needle)):
                if haystack[left] == needle[right] :
                    left += 1
                    right +=1 

                    if right == len(needle):
                        return left - right
                else:
                    left = left - right+1
                    right = 0
            return -1
        else:
            return -1
        