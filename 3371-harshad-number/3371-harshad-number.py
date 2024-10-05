class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        num = x
        sum_digit = 0
        while x!=0:
            sum_digit += x%10
            x= x//10

        if num%sum_digit ==0:
            return sum_digit
        else:
            return -1
    