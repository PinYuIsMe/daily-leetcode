class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        left, right = 0, n-1
        maxAmount = 0

        while (right - left) > 0:
            lower = right if height[right] <= height[left] else left
            currAmount = (right - left) * height[lower]
            maxAmount = max(maxAmount, currAmount)

            if lower == left:
                left += 1
            else:
                right -= 1

        return maxAmount


            

