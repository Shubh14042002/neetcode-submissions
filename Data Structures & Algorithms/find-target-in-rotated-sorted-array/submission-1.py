class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1

        while left <= right :
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            if left == right:
                return -1
            elif nums[mid] >= nums[left]: ##compare to the left hand side , if left smaller then we are in the sorted section and havent reached the pivot
                ### we are in the sorted section of list 
                if nums[left] <= target < nums[mid]:## if the target lies in the sorted range we have our new indexes as the sorted range so far. so shrink the right index 
                    right = mid - 1 
                else:## check the right hand side which has pivot 
                    left = mid + 1 
                
            elif nums[mid] <= nums[left]:##mid number is in the pivot region
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1 
        return -1

                


                

