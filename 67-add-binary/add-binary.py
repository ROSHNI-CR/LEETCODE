class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        # Continue as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Add digit from string 'a' if available
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            # Add digit from string 'b' if available
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # Current digit is total % 2 (e.g., 2 % 2 = 0, 3 % 2 = 1)
            result.append(str(total % 2))
            
            # Update carry (e.g., 2 // 2 = 1, 3 // 2 = 1)
            carry = total // 2

        # The result is built backwards, so reverse it and join into a string
        return "".join(result[::-1])
        