class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        count = 0 
        print(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<k:
                nums.pop()
                count +=1
            elif nums[i]>k:
                break



        return count