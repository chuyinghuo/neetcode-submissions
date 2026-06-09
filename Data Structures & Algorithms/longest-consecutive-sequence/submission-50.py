class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0 
        numbers_set = set(nums)

        for number in nums:
            current_number = number 
            current_streak = 0 

            while current_number in numbers_set:
                current_streak += 1
                current_number += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
        return longest_streak
