class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictionary = {0:1}
        total = 0 
        count = 0 

        for i in range(len(nums)): 
            total += nums[i]
            if total - k in dictionary: 
                count += dictionary[total - k]
            dictionary[total] = dictionary.get(total, 0) + 1

        return count
            
                
            
        