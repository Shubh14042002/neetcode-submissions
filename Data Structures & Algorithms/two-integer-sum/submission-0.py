class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        i = 0
        while i < length :
            other_possible_number = target - nums[i]
            j = i+1
            while j < length:
                if nums[j] == other_possible_number:
                    return [i,j]
                j+=1
            i+=1
