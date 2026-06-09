class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        result = [0] * len(temperatures)
        stack = [[temperatures[0], 0]]
        for i in range(1, len(temperatures)):
            if not stack:
                stack.append([temperatures[i], i])
            else:
                while True:
                    if not stack:
                        stack.append([temperatures[i], i])
                        break
                    elif temperatures[i] <= stack[-1][0]:
                        stack.append([temperatures[i], i])
                        break
                    else:
                        result[stack[-1][1]] = i - stack[-1][1]
                        stack.pop()
                    
        return result
            