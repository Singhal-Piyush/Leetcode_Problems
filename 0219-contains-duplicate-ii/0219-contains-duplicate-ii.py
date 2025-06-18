class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # # brute force method
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]== nums[j]:
        #             if abs(i-j)<= k:
        #                 return True
        # return False

        # sliding window
        ## define two pointers
        start = 0
        hashset = set()
        for start in range(len(nums)):
            if nums[start] in hashset:
                return True
            hashset.add(nums[start])

            if len(hashset) > k:
                hashset.remove(nums[start-k])
        return False
        
                
                
