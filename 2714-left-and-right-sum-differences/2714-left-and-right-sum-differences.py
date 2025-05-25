class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        prefix_sum = [0]*(len(nums)+1)

        for i in range(1, len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        result = [0]*len(nums)

        for i in range(len(nums)):
            left_sum= prefix_sum[i]
            right_sum = prefix_sum[len(prefix_sum)-1] - prefix_sum[i+1]
            result[i] = abs(left_sum-right_sum)
        return result

        