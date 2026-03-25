class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n
        
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        max_points = 0
        
        for i in range(n):
            slopes = {}
            current_max = 0
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                # Simplify the slope using GCD to avoid float precision issues
                g = get_gcd(dx, dy)
                slope = (dx // g, dy // g)
                
                slopes[slope] = slopes.get(slope, 0) + 1
                current_max = max(current_max, slopes[slope])
            
            # The result for this anchor is current_max + 1 (the anchor itself)
            max_points = max(max_points, current_max + 1)
            
        return max_points
        