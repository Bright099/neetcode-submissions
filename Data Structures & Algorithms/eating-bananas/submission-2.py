from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        low = 1
        while low <= max_k:
            mid = (low + max_k) // 2
            sums = 0
            for num in piles:
                sums += ceil(num / mid)
            if sums > h:
                low = mid + 1
            elif sums <= h:
                max_k = mid - 1
        return low


        
        