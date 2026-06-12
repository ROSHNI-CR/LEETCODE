class Solution(object):
    def numSteps(self, s):
       nums=int(s,2)
       steps=0
       while(nums!=1):
            if(nums%2==0):
                nums=nums//2
                
            else:
                nums=nums+1
            steps+=1
       return steps