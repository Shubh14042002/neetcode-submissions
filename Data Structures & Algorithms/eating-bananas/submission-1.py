import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound_k = max(piles)
        lower_bound_k = 1 
        answer = upper_bound_k
        while lower_bound_k <= upper_bound_k:

            mid_k = (lower_bound_k + upper_bound_k)//2
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile/mid_k)
            if hours_spent <= h:
                # This speed works.
                # Save it, but try a SMALLER speed.
                answer = mid_k
                upper_bound_k = mid_k - 1

            else:
                # This speed is too slow.
                # We need to eat FASTER.
                lower_bound_k = mid_k + 1

        return answer
