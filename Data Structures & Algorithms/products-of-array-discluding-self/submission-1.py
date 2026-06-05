class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        value = 1
        for i in range(len(nums)):
            output.append(value)
            value *= nums[i]
        value = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= value
            value *= nums[i]
        return output

        