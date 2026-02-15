1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        left = 0
4        right  = 0
5        count = 0
6
7        while right < len(nums):
8
9            if nums[right] == val:
10                right +=1
11            else:
12                nums[left] = nums[right]
13
14                right += 1
15                left +=1
16                count +=1
17        return count
18        