class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #update
        index =0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index] = nums[i]
                index +=1
        return index

    
        