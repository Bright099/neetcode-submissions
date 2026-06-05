class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        lengths = []
        nums = list(sorted(set(nums)))
        value = nums[0]
        checker = 1
        for i in range(1, len(nums)):
            if (nums[i] - value) == 1:
                checker += 1
            elif (nums[i] - value) > 1:
                lengths.append(checker)
                checker = 1
            value = nums[i]
        lengths.append(checker)
        return max(lengths)