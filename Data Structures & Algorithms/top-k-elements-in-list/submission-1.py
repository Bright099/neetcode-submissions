from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        numbers = Counter(nums)
        for _ in range(k):
            checker = nums[0]
            for key in numbers.keys():
                if numbers[key] > numbers[checker]:
                    checker = key
            output.append(checker)
            del numbers[checker]
        return output

            
        