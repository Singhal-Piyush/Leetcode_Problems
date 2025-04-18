class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        i = 0
        j = 0
        while j<len(s):
            if s[j] == " ":
                s[i:j] = reversed(s[i:j])
                i = j+1
            j +=1
            if j ==len(s):
                s[i:j] = reversed(s[i:j])
        return "".join(s)
