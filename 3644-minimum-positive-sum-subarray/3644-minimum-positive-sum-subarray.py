class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        if not nums or l>r or l<=0:
            return -1

        n = len(nums)
        prefix_sum = [0] *(n+1)

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        min_positive_sum = float('inf')

        for length in range(l, r+1):
            for i in range(n-length+1):
                sum_sub = prefix_sum[i+length] - prefix_sum[i]

                if 0<sum_sub<min_positive_sum:
                    min_positive_sum = sum_sub
        return min_positive_sum if min_positive_sum != float('inf') else -1