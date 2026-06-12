class Solution(object):
    def subsets(self, nums):
        n=len(nums)
        subset=1<<n
        ans=[]

        for i in range(subset):
            temp=[]
            for j in range (n):
            
                if(i& (1<<j)):
                
                    temp.append(nums[j])
                           
            
            ans.append(temp)
        
        return ans
