class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        value = []
        for i in freq.keys():
            if freq[i]<=1:
                value.append(i)
        print(value)
        if len(value)>=k:
            return value[k-1]
        return ""
        