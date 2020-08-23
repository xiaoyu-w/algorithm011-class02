class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """ 最长上升子序列"""
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)