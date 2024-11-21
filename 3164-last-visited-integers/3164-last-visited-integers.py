class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for num in nums:
            if num!=-1:
                seen = [num]+seen
                k=0
            elif num==-1 and k<len(seen):
                ans.append(seen[k])
                k+=1
            elif k>=len(seen):
                ans.append(-1)
        return ans