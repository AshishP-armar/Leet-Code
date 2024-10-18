class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_count = {}
        nums.sort()
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1 
        max_count = 0
        for key, value in num_count.items():
            if value>max_count:
                max_count = value
        print(max_count)
          
        if max_count==1:
            return len(set(nums))
        
        count = 0
        for key, value in num_count.items():
            if value==max_count:
                count+=max_count
        return count