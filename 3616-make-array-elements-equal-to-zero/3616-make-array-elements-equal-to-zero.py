class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        suffix_sum = sum(nums)
        prefix_sum = 0
        res = 0

        for i in nums:
            if i == 0:
                if suffix_sum == prefix_sum:
                    res +=2
                elif suffix_sum == prefix_sum -1 or suffix_sum == prefix_sum +1:
                    res +=1
            
            prefix_sum += i
            suffix_sum -= i
        return res
