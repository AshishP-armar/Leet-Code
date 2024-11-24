class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num

        while len(str(num))!=1:
            num = self.digitSum(num)
        return num

    def digitSum(self,n):
        sum = 0
        while n!=0:
            sum += n%10
            n = n//10
        return sum

        