class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        # 1. Sort to handle duplicates easily
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(current_path):
            # Base case: if the path length matches nums, we found a permutation
            if len(current_path) == len(nums):
                results.append(list(current_path))
                return
            
            for i in range(len(nums)):
                # Skip if this specific index is already in our path
                if used[i]:
                    continue
                
                # --- The Duplicate-Skip Logic ---
                # If nums[i] == nums[i-1] and we haven't used nums[i-1] 
                # in this branch, it means we've already processed this 
                # duplicate's entire subtree. Skip to avoid duplicates.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # Choose
                used[i] = True
                current_path.append(nums[i])
                
                # Explore
                backtrack(current_path)
                
                # Backtrack (Un-choose)
                current_path.pop()
                used[i] = False
                
        backtrack([])
        return results
        