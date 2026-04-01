class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the array has 2 or fewer elements, it already meets the criteria
        if len(nums) <= 2:
            return len(nums)
        
        # k represents the index where the next valid element will be placed
        # We start at 2 because the first two elements are always allowed
        k = 2
        
        # Iterate through the array starting from the third element
        for i in range(2, len(nums)):
            # Compare the current element with the element two positions 
            # before the current 'write' pointer k
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k
        