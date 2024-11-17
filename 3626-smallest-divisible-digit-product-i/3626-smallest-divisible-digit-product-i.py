class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if self.productDigit(n)%t==0:
                return n
            n +=1
    def productDigit(self,num):
        ans = 1
        while num!=0:
            ans = ans * (num%10)
            num = num//10
        return ans
            
        