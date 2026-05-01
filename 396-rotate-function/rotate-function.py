class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        
        total_sum = sum(nums)
        
        # Calculate F(0)
        F = sum(i * nums[i] for i in range(n))
        
        max_value = F
        
        # Compute F(1) to F(n-1)
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_value = max(max_value, F)
        
        return max_value
        