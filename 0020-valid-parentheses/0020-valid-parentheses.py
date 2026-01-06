class Solution:
    def isValid(self, s: str) -> bool:
        # 建立映射關係：Key 是右括號，Value 是對應的左括號
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # 如果是右括號
            if char in bracket_map:
                # 彈出棧頂元素，如果棧是空的，給一個永遠配對不上的 dummy char
                top_element = stack.pop() if stack else '#'
                
                # 直接比對，不需要算索引
                if bracket_map[char] != top_element:
                    return False
            else:
                # 如果是左括號，直接入棧
                stack.append(char)

        # 只要檢查棧是否為空即可
        return not stack