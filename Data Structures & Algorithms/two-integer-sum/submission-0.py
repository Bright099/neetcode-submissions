class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in vals.keys():
                return [vals[diff], i]
            else:
                vals[nums[i]] = i     