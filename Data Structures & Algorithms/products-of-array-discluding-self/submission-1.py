class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            s[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            s[i] *= suffix
            suffix *= nums[i]

        return s