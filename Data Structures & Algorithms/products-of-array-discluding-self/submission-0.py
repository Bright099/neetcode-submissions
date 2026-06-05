class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            check = 1
            for j in range(len(nums)):
                if i != j:
                    check *= nums[j]
            output.append(check)
        return output

        