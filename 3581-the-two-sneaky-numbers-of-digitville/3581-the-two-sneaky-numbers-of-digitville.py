class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        temp = set()

        result = []

        for num in nums:
            if num not in temp:
                temp.add(num)
            else:
                result.append(num)
        return result
