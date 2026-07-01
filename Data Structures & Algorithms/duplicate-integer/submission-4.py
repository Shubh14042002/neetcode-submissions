class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        match = False
        if len(nums)<2:
            return False
        while i < len(nums):
             if nums[i]==nums[i-1]:
                match= True
             i+=1
        if match:
            return True
        else:
            return False
        
        