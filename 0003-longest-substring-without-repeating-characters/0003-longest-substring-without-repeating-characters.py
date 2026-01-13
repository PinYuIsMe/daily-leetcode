class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIdx = {}
        maxLen = 0
        left = 0
        
        for right, c in enumerate(s):
            # 如果字元已存在，且它的索引在當前視窗 [left, right] 之內
            if c in charIdx and charIdx[c] >= left:
                # 移動左指標到重複字元的下一個位置
                left = charIdx[c] + 1
            
            # 更新字元最新的位置索引
            charIdx[c] = right
            
            # 每一輪都更新最大長度：視窗大小為 (right - left + 1)
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen