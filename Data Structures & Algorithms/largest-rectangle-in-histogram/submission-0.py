class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        elif len(heights) == 1:
            return heights[0]
        heights.append(0)
        max_area = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped = stack.pop()
                h = heights[popped]
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                width = i - left - 1
                area = width * h
                if area > max_area:
                    max_area = area
            stack.append(i)
        return max_area    