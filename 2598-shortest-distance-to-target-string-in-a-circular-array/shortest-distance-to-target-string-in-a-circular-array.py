class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        min_dist = n
        
        for i in range(n):
            if words[i] == target:
                forward_dist = abs(i - startIndex)
                backward_dist = n - forward_dist
                min_dist = min(min_dist, forward_dist, backward_dist)
        
        return min_dist if min_dist != n else -1