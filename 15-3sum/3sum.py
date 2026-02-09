class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the list 
        res = []

        for i in range(len(nums)): 
            # things to note: duplicates through the i value 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue 

            l = i + 1 
            r = len(nums) - 1 

            while l < r: 
                if nums[i] + nums[l] + nums[r] == 0: 
                    res.append([nums[i], nums[l], nums[r]])

                    # duplicates in the left value 
                    while l < r and nums[l] == nums[l + 1]: 
                        l += 1 
                    # duplicates in the right value 
                    while l < r and nums[r] == nums[r - 1]: 
                        r -= 1 

                    l += 1 
                    r -= 1 
                elif -nums[i] > nums[l] + nums[r]: 
                    l += 1 
                else: 
                    r -= 1

                
        return res



        
        