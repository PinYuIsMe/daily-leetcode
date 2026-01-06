class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s = sorted(s)
            t = sorted(t)
            print(f"s: {s}")
            print(f"t: {t}")
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False
            return True
        else:
            return False