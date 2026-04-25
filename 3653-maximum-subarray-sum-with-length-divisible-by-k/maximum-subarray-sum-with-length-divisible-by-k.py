class Solution(object):
    def maxSubarraySum(self, nums, k):
        n = len(nums)
        
        prefix = 0
        ans = float('-inf')
        
        # min prefix for each remainder
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0   # important base case
        
        for i in range(1, n + 1):
            prefix += nums[i - 1]
            
            r = i % k
            
            if min_prefix[r] != float('inf'):
                ans = max(ans, prefix - min_prefix[r])
            
            min_prefix[r] = min(min_prefix[r], prefix)
        
        return ans