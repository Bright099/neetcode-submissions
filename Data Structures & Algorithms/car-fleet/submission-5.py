class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0] * len(position)
        wait_arr = [[]] * len(position)
        for i in range(len(position)):
            wait_arr[i] = [position[i], speed[i]]
        wait_arr = sorted(wait_arr)
        for i in range(len(position)):
            time[i] = (target - wait_arr[i][0]) / wait_arr[i][1]
        output = 0
        if len(time) > 1:
            hold = time[-1]
            output += 1
            for i in range(len(time) -2, -1, -1):
                if time[i] > hold:
                    output += 1
                    hold = time[i]
            return output
        elif len(time) == 1:
            return 1
        else:
            return 0