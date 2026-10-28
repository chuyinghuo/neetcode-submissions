class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] = 
        n = len(nums)
        seq = [1]*n
        # #dp base case: only one element in the sequence
        # seq[0] = 1
        # seq[1] = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    seq[i] = max(seq[i], seq[j]+1)
        return max(seq)
            

