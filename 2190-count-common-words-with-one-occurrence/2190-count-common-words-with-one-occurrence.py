class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_freq = Counter(words1)
        words2_freq = Counter(words2)

        string = set(words1_freq.keys())|set(words2_freq.keys())
        count = 0
        for i in string:
            if (words1_freq[i]==1) and (words2_freq[i]==1):
                count+=1
        return count
        