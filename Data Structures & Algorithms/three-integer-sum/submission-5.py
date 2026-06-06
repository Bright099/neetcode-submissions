class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                
                while left < right:           
                    sum_up = nums[i] + nums[left] + nums[right]
                    if sum_up == 0:
                        output.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif sum_up < 0:
                        left += 1
                    elif sum_up > 0:
                        right -= 1
        return output
        