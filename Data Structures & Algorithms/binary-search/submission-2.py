class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        for i in range(len(nums)):
            mid_index = (left + right)//2
            mid_number = nums[mid_index]
        # can divide into two arrays (0,index split-1),(index split,len(nums)-1)
            if target < mid_number :
                right = mid_index-1
            elif target > mid_number :
                left = mid_index+1
            elif target == mid_number:
                return mid_index
        return -1;
            
        
        
