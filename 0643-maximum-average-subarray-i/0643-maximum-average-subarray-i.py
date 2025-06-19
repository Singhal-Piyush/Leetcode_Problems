class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = 0
        num_sum = 0
        max_avg = float('-inf')

        while end < len(nums):
            num_sum += nums[end]

            if end-start +1 == k:
                max_avg = max(max_avg, num_sum/k)
                num_sum -= nums[start]
                start += 1

            if end-start+1 <= k:
                end += 1
        return max_avg
        