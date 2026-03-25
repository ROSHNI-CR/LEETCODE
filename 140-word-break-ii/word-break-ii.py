class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        memo = {}

        def dfs(remaining_s):
            # If we've already solved for this suffix, return it
            if remaining_s in memo:
                return memo[remaining_s]
            
            # Base case: if the string is empty, return a list with an empty string
            if not remaining_s:
                return [""]
            
            res = []
            # Try every possible split point
            for i in range(1, len(remaining_s) + 1):
                prefix = remaining_s[:i]
                if prefix in wordSet:
                    # Recursively find sentences for the rest of the string
                    suffixes = dfs(remaining_s[i:])
                    for suffix in suffixes:
                        # Join prefix and suffix with a space if suffix isn't empty
                        if suffix:
                            res.append(prefix + " " + suffix)
                        else:
                            res.append(prefix)
            
            # Cache the result before returning
            memo[remaining_s] = res
            return res

        return dfs(s)