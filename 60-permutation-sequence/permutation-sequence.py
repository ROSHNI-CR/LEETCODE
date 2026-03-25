import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 1. Create a list of available numbers: [1, 2, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]
        
        # 2. Pre-calculate factorials
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
            
        # 3. Adjust k to be 0-indexed
        k -= 1
        result = []
        
        # 4. Determine each digit one by one
        for i in range(n - 1, -1, -1):
            # Index of the number to pick from the available list
            idx = k // factorials[i]
            k %= factorials[i]
            
            # Add picked number to result and remove from available list
            result.append(numbers.pop(idx))
            
        return "".join(result)
        