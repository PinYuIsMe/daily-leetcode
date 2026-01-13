class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        
        n = len(temps)
        answer = [0] * n
        stack = [] # idx of first temperature

        for right in range(n):
            while stack and (temps[right] > temps[stack[-1]]):
                left = stack.pop()
                answer[left] = right - left
            stack.append(right)

        for i in stack:
            answer[i] = 0

        return answer
        
            