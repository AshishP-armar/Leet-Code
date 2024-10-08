class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums.sort()
        nums1 = set()
        nums2 = set()
        flag = True
        for num in nums:
            if num not in nums1 and flag:
                nums1.add(num)
                flag = False
            elif num not in nums2 and not flag:
                nums2.add(num)
                flag = True
            else:
                return False   
            
        return True