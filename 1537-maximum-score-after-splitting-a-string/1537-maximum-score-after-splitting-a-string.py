class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum = [0]*len(s)

        for i in range(1,len(s)):
            left_zero_count = s[0:i].count('0')
            right_one_count = s[i:len(s)].count('1')

            prefix_sum[i] = left_zero_count + right_one_count

        return max(prefix_sum)
        