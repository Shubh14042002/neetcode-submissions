class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            current_num = nums[i]
            needed_num = target - current_num
            if needed_num in seen :
                return [seen[needed_num],i]
            seen[current_num] = seen.get(current_num,i)