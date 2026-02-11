class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height) # maximum from the left 
        suffix = [0] * len(height)

        curr_max = 0 
        for i in range(0, len(height)): 
            prefix[i] = curr_max
            if height[i] > curr_max:
                curr_max = height[i]

        curr_max = 0 
        n = len(height)
        for i in range(n - 1, -1, -1): 
            suffix[i] = curr_max 
            if height[i] > curr_max: 
                curr_max = height[i]

        running_total = 0 
        for i in range(0, len(height)): 
            water = min(prefix[i], suffix[i]) - height[i]
            if water > 0:  # Only add positive water amounts
                running_total += water

        return running_total