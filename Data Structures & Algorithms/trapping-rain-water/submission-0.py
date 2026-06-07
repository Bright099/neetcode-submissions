class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * (len(height))
        prefix[0] = height[0]
        suffix = [0] * (len(height))
        suffix[-1] = height[-1]
        trapped = 0
        left = height[0]
        right = height[-1]
        for i in range(1, len(height)):
            if height[i] > left:
                prefix[i] = height[i]
                left = height[i]
            else:
                prefix[i] = left
        for j in range(len(height)-2, -1, -1):
            if height[j] > right:
                suffix[j] = height[j]
                right = height[j]
            else:
                suffix[j] = right
        for i in range(len(height)):
            trapped += min(prefix[i], suffix[i]) - height[i]
        return trapped

