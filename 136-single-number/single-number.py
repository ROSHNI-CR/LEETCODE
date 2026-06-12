class Solution(object):
    def singleNumber(self, nums):
        n=len(nums)
        res=0
        for i in range(n):
            res^=nums[i]
        return res
        