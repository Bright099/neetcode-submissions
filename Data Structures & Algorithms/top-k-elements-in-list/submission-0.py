from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        numbers = Counter()
        for num in nums:
            numbers[num] += 1
        for _ in range(k):
            checker = nums[0]
            for key in numbers.keys():
                if numbers[key] > numbers[checker]:
                    checker = key
            output.append(checker)
            del numbers[checker]
        return output

            
        