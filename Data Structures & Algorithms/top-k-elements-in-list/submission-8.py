class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency = {}

        # for num in nums:
        #     frequency[num] = frequency.get(num, 0) + 1

        # sorted_numbers = sorted(
        #     frequency,
        #     key=frequency.get,
        #     reverse=True
        # )

        # return sorted_numbers[:k]

        # bucket solution with O(n) complexity
        freq_list =  {}
        for i in range(len(nums)):
            num = nums[i]
            upd_count = freq_list.get(num,0)+1
            freq_list[num] = upd_count
        
        buckets=[]
        for i in range(len(nums)+1):
            buckets.append([])
        
        for num in freq_list:
            buckets[freq_list[num]].append(num)
        
        results = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                results.append(num)
            if len(results) == k :
                return results
