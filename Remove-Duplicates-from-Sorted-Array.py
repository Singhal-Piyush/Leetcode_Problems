1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        # define pointer
4        left = 0
5        right = 0
6        count = 1
7
8        # itterate over the nums
9        for right in range(len(nums)-1):
10            if nums[left] == nums[right]:
11                right += 1
12            if nums[left]< nums[right]:
13                left +=1
14                nums[left] = nums[right]
15                count +=1
16        return count
17
18        