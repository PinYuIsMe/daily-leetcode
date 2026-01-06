class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) <= 1:
            return [nums]

        permutations = []

        for i, n in enumerate(nums):
            sub_nums = nums[:i] + nums[i + 1:]
            sub_permutations = self.permute(sub_nums)
            for p in sub_permutations:
                permutations.append([n] + p)
        
        return permutations
            




        