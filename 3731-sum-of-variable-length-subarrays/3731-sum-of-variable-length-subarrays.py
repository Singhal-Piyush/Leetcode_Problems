class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix_sum = [0]*(len(nums)+1)

        for i in range(1,len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
        total = 0

        for i in range(len(nums)):
            start = max(0,i-nums[i])
            total += prefix_sum[i+1]- prefix_sum[start]
        return total
        