class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # define pointer
        left = 0
        right = 0
        count = 1

        # itterate over the nums
        for right in range(len(nums)-1):
            if nums[left] == nums[right]:
                right += 1
            if nums[left]< nums[right]:
                left +=1
                nums[left] = nums[right]
                count +=1
        return count

        