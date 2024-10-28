class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums) 
        streaks = {}  
        max_streak = -1  

        for num in nums:
            if num not in streaks:  
                length = 1
                current = num
                while current * current in nums_set:
                    length += 1
                    current *= current
                    streaks[current] = length
                streaks[num] = length
                if length >= 2:
                    max_streak = max(max_streak, length)

        return max_streak
