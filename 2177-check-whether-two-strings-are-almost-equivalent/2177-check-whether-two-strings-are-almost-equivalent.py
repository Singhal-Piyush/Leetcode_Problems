class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1_freq = Counter(sorted(word1))
        word2_freq = Counter(sorted(word2))

        total_letter = set(word1_freq.keys()) | set(word2_freq.keys())
        print(total_letter)
        for i in total_letter:
            diff = abs(word1_freq[i]-word2_freq[i])
            if diff>3:
                return False
        return True

        

        