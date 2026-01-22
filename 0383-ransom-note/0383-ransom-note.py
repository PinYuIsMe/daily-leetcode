from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Counter creates a frequency map automatically
        # Subtracting them keeps only the counts that are still needed
        return not (Counter(ransomNote) - Counter(magazine))