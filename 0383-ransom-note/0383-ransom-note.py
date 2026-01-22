from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineHash = defaultdict(int)
        for letter in magazine:
            if letter in magazineHash:
                magazineHash[letter] += 1
            else:
                magazineHash[letter] = 1

        for letter in ransomNote:
            if letter in magazineHash:
                magazineHash[letter] -= 1
                if magazineHash[letter] == 0:
                    del magazineHash[letter]
            else:
                return False
        return True