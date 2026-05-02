class Solution(object):
    def rotatedDigits(self, n):
        count = 0
        
        for i in range(1, n + 1):
            num = str(i)
            valid = True
            changed = False
            
            for digit in num:
                if digit in ['3', '4', '7']:
                    valid = False
                    break
                if digit in ['2', '5', '6', '9']:
                    changed = True
            
            if valid and changed:
                count += 1
                
        return count
        