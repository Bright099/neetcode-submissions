from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        numbers = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for key, value in numbers.items():
            buckets[value].append(key)
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
            
        