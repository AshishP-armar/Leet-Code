class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            result.append(self.SumofDigit(num))

        return min(result)
            

    def SumofDigit(self,num):
        sumdigit = 0
        while num!=0:
            sumdigit+= num%10
            num = num//10
        return sumdigit
