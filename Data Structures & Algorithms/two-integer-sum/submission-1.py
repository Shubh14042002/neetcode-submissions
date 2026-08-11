class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            needed = target - num
            if needed in seen :
                return [seen[needed], i]
            seen[num] = i
        # while i < length :
        #     other_possible_number = target - nums[i]
        #     j = i+1
        #     while j < length:
        #         if nums[j] == other_possible_number:
        #             return [i,j]
        #         j+=1
        #     i+=1
