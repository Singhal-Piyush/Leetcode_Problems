class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        i = 0
        j = 2*k

        while i <len(s):
            if len(s[i:j])<k:
                s[i:j] = reversed(s[i:j])
            elif k<=len(s[i:i+k])<2*k:
                s[i:i+k] = reversed(s[i:i+k])
            
            i +=2*k
            j += 2*k
            if j>len(s):
                j = len(s)
        return "".join(s)