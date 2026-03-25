class Solution(object):
    def palindromePairs(self, words):
        # Map word to its index for O(1) lookups
        word_to_idx = {word: i for i, word in enumerate(words)}
        results = []
        
        for i, word in enumerate(words):
            n = len(word)
            # We iterate through every possible split point in the word
            # j goes up to n inclusive to handle empty prefix/suffix cases
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # Case 1: Prefix is palindrome, check if reverse(suffix) exists
                if self.is_palindrome(prefix):
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_to_idx and word_to_idx[rev_suffix] != i:
                        results.append([word_to_idx[rev_suffix], i])
                
                # Case 2: Suffix is palindrome, check if reverse(prefix) exists
                # j < n prevents duplicate results when j=0 (empty prefix)
                if j < n and self.is_palindrome(suffix):
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_to_idx and word_to_idx[rev_prefix] != i:
                        results.append([i, word_to_idx[rev_prefix]])
                        
        return results

    def is_palindrome(self, s):
        return s == s[::-1]