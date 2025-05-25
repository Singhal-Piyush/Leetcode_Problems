class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        prefix_sum = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        total_sum = prefix_sum[len(prefix_sum)-1]

        for i in range(1,len(nums)):
            left_subarray_sum = prefix_sum[i]
            right_subarray_sum = total_sum - prefix_sum[i]
            if abs(left_subarray_sum - right_subarray_sum)%2 == 0:
                count +=1
        return count 